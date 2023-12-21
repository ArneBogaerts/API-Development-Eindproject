import requests
import json
from datetime import datetime
import random
import string

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


def unique_name(prefix="Artiest"):
    """Genereert een unieke naam door een tijdstempel en willekeurige letters toe te voegen."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_str = ''.join(random.choices(string.ascii_letters, k=5))
    return f"{prefix}_{timestamp}_{random_str}"

def test_create_artist():
    unique_artist_name = unique_name()
    artist_data = {"name": unique_artist_name}
    create_response = requests.post(f"{BASE_URL}/artists/", json=artist_data)
    assert create_response.status_code == 200, "Artiest kon niet worden aangemaakt"
    artist_id = create_response.json()['id']
    #Hier verwijder ik de zonet aangemaakte artist, om de database niet te verzadigen en om de test
    #meermaals te kunnen runnen
    delete_response = requests.delete(f"{BASE_URL}/artists/{artist_id}")
    assert delete_response.status_code == 200, "Artiest kon niet worden verwijderd"

def test_delete_artist():
    # Stap 1: Maak een nieuwe, unieke artiest aan
    unique_artist_name = unique_name()
    artist_data = {"name": unique_artist_name}
    create_response = requests.post(f"{BASE_URL}/artists/", json=artist_data)
    assert create_response.status_code == 200, "Artiest kon niet worden aangemaakt"
    artist_id = create_response.json()['id']

    # Stap 2: Verwijder de zojuist aangemaakte artiest
    delete_response = requests.delete(f"{BASE_URL}/artists/{artist_id}")
    assert delete_response.status_code == 200, "Artiest kon niet worden verwijderd"

    # Stap 3: Controleer of de artiest daadwerkelijk is verwijderd
    get_response = requests.get(f"{BASE_URL}/artists/{artist_id}")
    assert get_response.status_code == 404, "Artiest lijkt niet verwijderd te zijn na DELETE-verzoek"

def test_update_review():
    # Stap 1: Maak een nieuwe artiest en CD aan voor de review
    artist_name = unique_name("Artiest")
    cd_title = unique_name("CD")
    artist_response = requests.post(f"{BASE_URL}/artists/", json={"name": artist_name})
    assert artist_response.status_code == 200, "Artiest kon niet worden aangemaakt voor de test"
    artist_id = artist_response.json()['id']
    cd_response = requests.post(f"{BASE_URL}/cds/", json={"title": cd_title, "artist_name": artist_name})
    assert cd_response.status_code == 200, "CD kon niet worden aangemaakt voor de test"
    cd_id = cd_response.json()['id']

    # Stap 2: Maak een nieuwe review aan voor de CD
    review_data = {"rating": 4.5, "comment": "Geweldige CD!", "cd_id": cd_id}
    create_response = requests.post(f"{BASE_URL}/reviews/", json=review_data)
    assert create_response.status_code == 200, "Review kon niet worden aangemaakt voor de test"
    review_id = create_response.json()['id']

    # Stap 3: Definieer de nieuwe gegevens voor de review
    updated_review_data = {"rating": 5.0, "comment": "Echt fantastisch!", "cd_id": cd_id}

    # Stap 4: Stuur een PUT verzoek om de review bij te werken
    update_response = requests.put(f"{BASE_URL}/reviews/{review_id}", json=updated_review_data)
    assert update_response.status_code == 200, "Kon de review niet bijwerken"

    # Stap 5: Haal de bijgewerkte review op en controleer de wijzigingen
    get_response = requests.get(f"{BASE_URL}/reviews/{review_id}")
    assert get_response.status_code == 200, "Kon de bijgewerkte review niet ophalen"
    updated_review = get_response.json()
    assert updated_review['rating'] == updated_review_data['rating'], "De rating van de review is niet correct bijgewerkt"
    assert updated_review['comment'] == updated_review_data['comment'], "De commentaar van de review is niet correct bijgewerkt"

    # Optioneel: Opruimen
    delete_cd_response = requests.delete(f"{BASE_URL}/cds/{cd_id}")
    assert delete_cd_response.status_code == 200, "Kon de test CD niet opruimen"
    delete_artist_response = requests.delete(f"{BASE_URL}/artists/{artist_id}")
    assert delete_artist_response.status_code == 200, "Kon de test artiest niet opruimen"
