import requests
import json

BASE_URL = "https://api-arnebogaerts.cloud.okteto.net"
# BASE_URL = "http://127.0.0.1:8000"


def create_test_user():
    username = "testuser"
    password = "testpassword"
    response = requests.post(f"{BASE_URL}/users/", json={"username": username, "password": password})
    assert response.status_code == 200, f"Fout bij het aanmaken van testgebruiker: {response.text}"
    user_id = response.json()["id"]
    return username, password, user_id

username, password, user_id = create_test_user()

def get_access_token(username, password):
    response = requests.post(f"{BASE_URL}/token", data={"username": username, "password": password})
    assert response.status_code == 200, f"Fout bij het ophalen van token: {response.text}"
    return response.json()["access_token"]

token = get_access_token(username, password)

def test_read_users():
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/users/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

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

def delete_test_user(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert response.status_code in [200, 204], f"Fout bij het verwijderen van testgebruiker: {response.status_code}, {response.text}"

delete_test_user(user_id)