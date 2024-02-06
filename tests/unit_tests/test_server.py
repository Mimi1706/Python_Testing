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
        competition_name = competitions[1]["name"] # competition 2 has 13 places
        club_name = clubs[0]["name"] # club 1 only has 13 balance points
        places_to_book = 10

        response = client.post("/purchasePlaces", data={"club": club_name, "competition": competition_name, "places": places_to_book})

        assert b"Great, booking complete!" in response.data

    def test_invalid_purchase_not_enough_points(self, client, clubs, competitions):
        competition_name = competitions[0]["name"]
        club_name = clubs[1]["name"] # club 2 only has 4 balance points
        places_to_book = 5

        response = client.post("/purchasePlaces", data={"club": club_name, "competition": competition_name, "places": places_to_book})

        assert b"Your point balance is not enough." in response.data
        assert b"Points available: 4" in response.data

    def test_invalid_purchase_not_enough_places(self, client, clubs, competitions):
        competition_name = competitions[1]["name"] # competition 2 has 3 places left after test_valid_purchase
        club_name = clubs[2]["name"] # club 3 has 12 balance points
        places_to_book = 10

        response = client.post("/purchasePlaces", data={"club": club_name, "competition": competition_name, "places": places_to_book})

        assert b"Not enough places available for the quantity you requested." in response.data

    def test_invalid_purchase_invalid_value(self, client, clubs, competitions):
        competition_name = competitions[1]["name"] # competition 2 has 3 places left after test_valid_purchase
        club_name = clubs[2]["name"] # club 3 has 12 balance points
        places_to_book = -2

        response = client.post("/purchasePlaces", data={"club": club_name, "competition": competition_name, "places": places_to_book})

        assert b"Incorrect value." in response.data
