# conftest.py
import os
import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Generate environment.properties for Allure reports"""
    allure_results = config.getoption("--alluredir")
    if allure_results and os.path.exists(allure_results):
        env_file = os.path.join(allure_results, "environment.properties")
        with open(env_file, "w") as f:
            f.write(f"BASE_URL={os.getenv('BASE_URL')}\n")
            f.write(f"AUTH_TOKEN={os.getenv('AUTH_TOKEN')}\n")

@pytest.fixture(scope="session")
def base_url():
    """Fixture to provide base URL from environment variable"""
    return os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def auth_token():
    """Fixture to provide Authorization token from environment variable"""
    return os.getenv("AUTH_TOKEN")


@pytest.fixture(scope="session")
def headers(auth_token):
    """Fixture to provide request headers with Authorization"""
    return {"Authorization": auth_token}


@pytest.fixture(scope="session")
def end_point():
    """Fixture for the users API endpoint"""
    return "/public/v2/users/"
