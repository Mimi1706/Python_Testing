import pytest
import server
from server import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


@pytest.fixture
def clubs(monkeypatch):
    clubs = [
        {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"},
    ]

    monkeypatch.setattr(server, "clubs", clubs)
    return clubs


@pytest.fixture
def competitions(monkeypatch):
    competitions = [
        {
            "name": "Spring Festival",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "25",
        },
        {"name": "Fall Classic", "date": "2024-10-22 13:30:00", "numberOfPlaces": "2"},
        {
            "name": "Past Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25",
        },
    ]

    monkeypatch.setattr(server, "competitions", competitions)
    return competitions
