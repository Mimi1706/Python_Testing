class TestPurchasePlaces:
    def test_valid_purchase(self, client, clubs, competitions):
        competition = competitions[0]["name"]
        club = clubs[0]["name"]
        places_to_book = 10

        response = client.post("/purchasePlaces", data={"club": club, "competition": competition, "places": places_to_book})

        assert response.status_code == 200
        assert b"Great, booking complete!" in response.data
        assert b"Points available: 3" in response.data
