import pytest
import requests
import allure
import logging

logger = logging.getLogger(__name__)


@allure.feature("User Management")
@allure.story("Negative Scenarios")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("negative")
@pytest.mark.negative
def test_create_user_invalid_token(base_url, end_point):
    """Verify creating a user with an invalid token fails (401)"""
    data = {"name": "invalid_token_user", "email": "invalid@user.com", "gender": "male", "status": "active"}
    bad_headers = {"Authorization": "Bearer invalidtoken123"}

    with allure.step("➡️ Create User with Invalid Token"):
        logger.info("Sending POST with invalid token")
        post_response = requests.post(base_url + end_point, headers=bad_headers, json=data, timeout=10)

        allure.attach(
            f"POST {base_url+end_point}\nHeaders: {bad_headers}\nBody: {data}",
            name="Invalid Token Request",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(str(post_response.text), name="Invalid Token Response", attachment_type=allure.attachment_type.TEXT)

        assert post_response.status_code == 401, f"❌ Expected 401, got {post_response.status_code}"


@allure.feature("User Management")
@allure.story("Negative Scenarios")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("negative")
@pytest.mark.negative
def test_create_user_missing_fields(base_url, headers, end_point):
    """Verify creating a user with missing fields fails (422)"""
    data = {"name": "missing_fields_user"}  # email, gender, status missing

    with allure.step("➡️ Create User with Missing Fields"):
        logger.info("Sending POST with missing fields")
        post_response = requests.post(base_url + end_point, headers=headers, json=data, timeout=10)

        allure.attach(
            f"POST {base_url+end_point}\nHeaders: {headers}\nBody: {data}",
            name="Missing Fields Request",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(str(post_response.text), name="Missing Fields Response", attachment_type=allure.attachment_type.TEXT)

        assert post_response.status_code == 422, f"❌ Expected 422, got {post_response.status_code}"


@allure.feature("User Management")
@allure.story("Negative Scenarios")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("negative")
@pytest.mark.negative
def test_create_user_duplicate_email(base_url, headers, end_point):
    """Verify creating a user with duplicate email fails (422)"""
    email = "duplicate@user.com"
    data = {"name": "first_user", "email": email, "gender": "male", "status": "active"}

    # Create first user
    first_response = requests.post(base_url + end_point, headers=headers, json=data, timeout=10)
    assert first_response.status_code in [201, 422]  # tolerate if user already exists

    with allure.step("➡️ Create User with Duplicate Email"):
        logger.info("Sending POST with duplicate email")
        dup_response = requests.post(base_url + end_point, headers=headers, json=data, timeout=10)

        allure.attach(
            f"POST {base_url+end_point}\nHeaders: {headers}\nBody: {data}",
            name="Duplicate Email Request",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(str(dup_response.text), name="Duplicate Email Response", attachment_type=allure.attachment_type.TEXT)

        assert dup_response.status_code == 422, f"❌ Expected 422, got {dup_response.status_code}"
