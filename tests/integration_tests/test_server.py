import server


def test_server(client, monkeypatch, competitions, clubs):
    monkeypatch.setattr(server, "competitions", competitions)
    monkeypatch.setattr(server, "clubs", clubs)

    response_index = client.get("/")
    assert b"Please enter your secretary email to continue" in response_index.data

    response_point_board = client.get("/pointBoard")
    assert response_point_board.status_code == 200
    assert b"Clubs point board" in response_point_board.data

    response_show_summary = client.post(
        "/showSummary", data={"email": clubs[0]["email"]}
    )
    assert response_show_summary.status_code == 200

    response_purchase_places = client.post(
        "/purchasePlaces",
        data={
            "club": clubs[0]["name"],
            "competition": competitions[0]["name"],
            "places": 10,
        },
    )
    assert b"Great, booking complete!" in response_purchase_places.data
    assert b"Number of Places: 15" in response_purchase_places.data

    response_logout = client.get("/logout")
    assert response_logout.status_code == 302  # redirected http code
