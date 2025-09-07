import pytest
import requests
from jsonschema import validate
from libraries.util import read_excel_data
import logging
import allure

logger = logging.getLogger(__name__)

# JSON schema
user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "gender": {"type": "string", "enum": ["male", "female"]},
        "status": {"type": "string", "enum": ["active", "inactive"]}
    },
    "required": ["id", "name", "email", "gender", "status"]
}

# Safe Excel load
try:
    user_data = read_excel_data("tests/user_data.xlsx")
except Exception as e:
    logger.error(f"❌ Failed to load Excel data: {e}")
    user_data = [("dummy", "dummy@example.com", "male", "active")]  # fallback
@allure.feature("User Management")
@allure.story("Create User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("positive")
@pytest.mark.parametrize("name,email,gender,status", user_data)
def test_can_create_user(base_url, headers, end_point, name, email, gender, status):
    allure.dynamic.title(f"Create user → {name}")
    allure.dynamic.description_html(f"""
    <b>Test Objective:</b> Verify that a user can be created, retrieved, and deleted.<br>
    <b>Parameters:</b> {name}, {email}, {gender}, {status}
    """)

    data = {"name": name, "email": email, "gender": gender, "status": status}

    with allure.step("➡️ Create User (POST)"):
        logger.info(f"➡️ Sending POST request to {base_url+end_point} with data: {data}")
        post_response = requests.post(base_url + end_point, headers=headers, json=data, timeout=10)

        allure.attach(
            f"POST {base_url+end_point}\nHeaders: {headers}\nBody: {data}",
            name="Request Details",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(str(post_response.json()), name="Response Data", attachment_type=allure.attachment_type.JSON)

        assert post_response.status_code == 201, f"❌ POST failed: {post_response.text}"
        response_json = post_response.json()
        user_id = response_json["id"]
        validate(instance=response_json, schema=user_schema)

    with allure.step("➡️ Get User (GET)"):
        logger.info(f"➡️ Sending GET request to {base_url}{end_point}{user_id}")
        get_response = requests.get(f"{base_url}{end_point}{user_id}", headers=headers, timeout=10)

        allure.attach(
            f"GET {base_url}{end_point}{user_id}\nHeaders: {headers}",
            name="GET Request",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(str(get_response.json()), name="GET Response", attachment_type=allure.attachment_type.JSON)

        assert get_response.status_code == 200, f"❌ GET failed: {get_response.text}"
        validate(instance=get_response.json(), schema=user_schema)

    with allure.step("➡️ Delete User (DELETE)"):
        logger.info(f"🗑️ Deleting user with ID {user_id}")
        delete_response = requests.delete(f"{base_url}{end_point}{user_id}", headers=headers, timeout=10)

        allure.attach(
            f"DELETE {base_url}{end_point}{user_id}\nHeaders: {headers}",
            name="DELETE Request",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(str(delete_response.text), name="DELETE Response", attachment_type=allure.attachment_type.TEXT)

        assert delete_response.status_code == 204, f"❌ DELETE failed: {delete_response.text}"
