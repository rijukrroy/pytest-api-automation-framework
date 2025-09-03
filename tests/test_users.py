import pytest
import requests
from jsonschema import validate
from libraries.util import read_excel_data

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

user_data = read_excel_data("tests/user_data.xlsx")


@pytest.mark.parametrize("name,email,gender,status", user_data)
def test_can_create_user(base_url, headers, end_point, name, email, gender, status):
    data = {
        "name": name,
        "email": email,
        "gender": gender,
        "status": status
    }

    post_response = requests.post(base_url + end_point, headers=headers, json=data)
    assert post_response.status_code == 201

    user_id = post_response.json()["id"]
    validate(instance=post_response.json(), schema=user_schema)

    delete_response = requests.delete(base_url + end_point + f"{user_id}", headers=headers)
    assert delete_response.status_code == 204
