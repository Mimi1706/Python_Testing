import server 

class TestShowSummary:
    def test_show_summary_valid_email(self, monkeypatch, client, clubs, competitions):
        monkeypatch.setattr(server, "competitions", competitions)
        monkeypatch.setattr(server, "clubs", clubs)
        
        response = client.post("/showSummary", data={"email": "john@simplylift.co"})

        assert response.status_code == 200

    def test_show_summary_invalid_email(self, monkeypatch, client, clubs, competitions):
        monkeypatch.setattr(server, "competitions", competitions)
        monkeypatch.setattr(server, "clubs", clubs)

        response = client.post("/showSummary", data={"email": "user@test.com"})

        assert response.status_code == 200
        assert b"Email not found." in response.data
        
class TestPurchasePlaces:
    def test_valid_purchase(self, client, clubs, competitions):
        competition = competitions[0]["name"]
        club = clubs[0]["name"]
        places_to_book = 10

        response = client.post("/purchasePlaces", data={"club": club, "competition": competition, "places": places_to_book})

        assert response.status_code == 200
        assert b"Great, booking complete!" in response.data
        assert b"Points available: 3" in response.data
