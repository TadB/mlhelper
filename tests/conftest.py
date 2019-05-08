import pytest
from app import create_app, db
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
    db.create_all()

    yield test_app.test_client()

    db.drop_all()
    context.pop()
