import pytest
import requests       # ✅ missing earlier
import allure         # ✅ missing earlier
import logging
from jsonschema import validate
# Schemas
error_schema_object = {
    "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"]
}

error_schema_array = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "field": {"type": "string"},
            "message": {"type": "string"}
        },
        "required": ["message"]
    }
}

@allure.feature("User Management")
@allure.story("Negative Scenarios")
@pytest.mark.negative
def test_create_user_invalid_token(base_url, end_point):
    """Verify creating a user with an invalid token fails (401)"""
    data = {"name": "invalid_user", "email": "invalid@user.com", "gender": "male", "status": "active"}
    bad_headers = {"Authorization": "Bearer invalidtoken123"}

    post_response = requests.post(base_url + end_point, headers=bad_headers, json=data, timeout=10)
    response_json = post_response.json()

    allure.attach(str(response_json), name="Invalid Token Response", attachment_type=allure.attachment_type.JSON)

    assert post_response.status_code == 401
    validate(instance=response_json, schema=error_schema_object)  # ✅ use object schema here


@allure.feature("User Management")
@allure.story("Negative Scenarios")
@pytest.mark.negative
def test_create_user_missing_fields(base_url, headers, end_point):
    """Verify creating a user with missing fields fails (422)"""
    data = {"name": "missing_fields_user"}  # missing fields

    post_response = requests.post(base_url + end_point, headers=headers, json=data, timeout=10)
    response_json = post_response.json()

    allure.attach(str(response_json), name="Missing Fields Response", attachment_type=allure.attachment_type.JSON)

    assert post_response.status_code == 422
    validate(instance=response_json, schema=error_schema_array)  # ✅ use array schema


@allure.feature("User Management")
@allure.story("Negative Scenarios")
@pytest.mark.negative
def test_create_user_duplicate_email(base_url, headers, end_point):
    """Verify creating a user with duplicate email fails (422)"""
    email = "duplicate@user.com"
    data = {"name": "first_user", "email": email, "gender": "male", "status": "active"}

    # Create first user
    requests.post(base_url + end_point, headers=headers, json=data, timeout=10)

    dup_response = requests.post(base_url + end_point, headers=headers, json=data, timeout=10)
    response_json = dup_response.json()

    allure.attach(str(response_json), name="Duplicate Email Response", attachment_type=allure.attachment_type.JSON)

    assert dup_response.status_code == 422
    validate(instance=response_json, schema=error_schema_array)  # ✅ use array schema
