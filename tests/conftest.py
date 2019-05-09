import pytest
import os
from app import create_app, db
from config import Config


basedir = os.path.abspath(os.path.dirname(__file__))


class TestConfig(Config):
    # in-memory SQLite database
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True
    IMAGES_FOLDER = os.path.join(basedir, "testimages/")


@pytest.fixture(scope="module")
def client():
    test_app = create_app(TestConfig)
    context = test_app.app_context()
    context.push()
    db.create_all()

    yield test_app.test_client()

    db.drop_all()
    context.pop()
