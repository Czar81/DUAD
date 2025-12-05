import pytest


def test_register_address(client, get_token_user):
    token = get_token_user
    location = "1600 Pennsylvania Avenue NW"
    expected_result = {"message": "Address created", "data": {"id": 1}}

    response = client.post(
        "/me/address",
        json={"location": location},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    assert response.json == expected_result


def test_get_address(client, get_token_user):
    token = get_token_user
    expected_result = {
        "data": [
            {"id": 1, "id_user": 1, "location": "1600 Pennsylvania Avenue NW"},
        ]
    }

    response = client.get("/me/address", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert response.json == expected_result


def test_get_one_address(client, get_token_user):
    token = get_token_user
    id_address = 1
    expected_result = {
        "data": [
            {"id": 1, "id_user": 1, "location": "1600 Pennsylvania Avenue NW"},
        ]
    }

    response = client.get(
        f"/me/address/{id_address}", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json == expected_result


def test_update_address(client, get_token_user):
    token = get_token_user
    id_address = 1
    new_location = "200 New Jersey Avenue NY"
    expected_update_result = {"message": "Address updated"}
    expected_get_result = {
        "data": [
            {"id": 1, "id_user": 1, "location": "200 New Jersey Avenue NY"},
        ]
    }

    response_update = client.put(
        f"/me/address/{id_address}",
        json={"location": "200 New Jersey Avenue NY"},
        headers={"Authorization": f"Bearer {token}"},
    )
    response_get = client.get(
        "/me/address", headers={"Authorization": f"Bearer {token}"}
    )
    assert response_update.status_code == 200
    assert response_get.status_code == 200
    assert response_get.json == expected_get_result
    assert response_update.json == expected_update_result


def test_delete_address(client, get_token_user):
    token = get_token_user
    id_address = 1
    expected_delete_result = {"message": "Address deleted"}
    expected_get_result = {"data": "Not address found"}

    response_delete = client.delete(
        f"/me/address/{id_address}",
        headers={"Authorization": f"Bearer {token}"},
    )
    response_get = client.get(
        "/me/address", headers={"Authorization": f"Bearer {token}"}
    )

    assert response_delete.status_code == 200
    assert response_get.status_code == 200
    assert response_get.json == expected_get_result
    assert response_delete.json == expected_delete_result
