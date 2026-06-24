import pytest

from app import create_app
from config import TestConfig
from src.models import db

from services.turmas_service import adicionar_turmas

@pytest.fixture
def app():

    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()

        adicionar_turmas()

        yield app

        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()