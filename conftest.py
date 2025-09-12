import pytest
import logging
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logging.basicConfig(
        filename="logs/test.log",
        filemode="w",  # overwrite each run
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO
    )
    logging.getLogger().addHandler(logging.StreamHandler())  # also show in console
    logging.info("✅ Logging initialized")


@pytest.fixture(scope="session")
def logger():
    """Provide a logger instance for tests"""
    return logging.getLogger("pytest_api_framework")


# --- Allure environment.properties setup ---
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Generate environment.properties for Allure reports"""
    allure_results = config.getoption("--alluredir")
    if allure_results and os.path.exists(allure_results):
        env_file = os.path.join(allure_results, "environment.properties")
        with open(env_file, "w") as f:
            f.write(f"BASE_URL={os.getenv('BASE_URL')}\n")
            f.write(f"AUTH_TOKEN={os.getenv('AUTH_TOKEN')}\n")


# --- Log test start and finish ---
def pytest_runtest_setup(item):
    logging.info(f"🚀 Starting test: {item.name}")

def pytest_runtest_teardown(item, nextitem):
    logging.info(f"✅ Finished test: {item.name}")


# --- Fixtures for API tests ---
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
