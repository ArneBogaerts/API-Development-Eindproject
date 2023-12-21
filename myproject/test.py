import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def get_access_token():
    # Vervang deze met geldige inloggegevens
    username = "Arne"
    password = "abc123!"
    response = requests.post(f"{BASE_URL}/token", data={"username": username, "password": password})
    assert response.status_code == 200
    return response.json().get("access_token")

def test_read_cds():
    response = requests.get(f"{BASE_URL}/cds/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Hier verwacht ik een lijst van CDs

def test_read_artists():
    response = requests.get(f"{BASE_URL}/artists/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Hier verwacht ik een lijst van artiesten

def test_read_reviews_by_cd():
    cd_id = 3
    response = requests.get(f"{BASE_URL}/cds/{cd_id}/reviews/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Hier verwacht ik een lijst van reviews voor een specifieke CD


def test_read_users():
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/users/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)