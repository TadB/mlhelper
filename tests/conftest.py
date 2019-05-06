import pytest
from app import create_app
from app.config import Config


class TestConfig(Config):
    # in-memory SQLite database
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True


@pytest.fixture(scope="module")
def client():
    test_app = create_app(TestConfig)
    context = test_app.app_context()
    context.push()

    yield test_app.test_client()

    context.pop()
