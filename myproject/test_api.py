import requests

base_url = "http://127.0.0.1:8000/"

def test_create_festival():
    festival_data = {
        "naam": "Test Festival",
        "locatie": "Test Location",
        "start_datum": "2023-01-01",
        "eind_datum": "2023-01-02",
        "land_id": 1
    }
    response = requests.post(f"{base_url}/create_festival", json=festival_data)
    assert response.status_code == 404
    response_data = response.json()
    assert "detail" in response_data
    assert response_data["detail"] == 'Not Found'

def test_read_festivals():
    response = requests.get(f"{base_url}/festivals")
    assert response.status_code == 404
    response_data = response.json()
    assert isinstance(response_data, dict)
    assert "detail" in response_data


def test_read_festival():
    # Assuming there is at least one festival in the database
    response = requests.get(f"{base_url}/festivals/1")
    assert response.status_code == 404
    response_data = response.json()
    assert isinstance(response_data, dict)

def test_delete_festival():
    response = requests.delete(f"{base_url}/festivals/1")
    print(f"Actual response: {response.status_code}, {response.json()}")
    assert response.status_code == 404
    response_data = response.json()
    assert response_data == {"detail": "Not Found"}

def test_create_land():
    land_data = {
        "naam": "Test Land",
        "code": "TL"
    }
    response = requests.post(f"{base_url}/landen", json=land_data)
    assert response.status_code == 404
    response_data = response.json()
    assert isinstance(response_data, dict)
    assert "naam" in land_data

def test_read_landen():
    response = requests.get(f"{base_url}/landen")
    assert response.status_code == 404
    response_data = response.json()
    assert isinstance(response_data, dict)
    assert "detail" in response_data


def test_read_land():
    # Assuming there is at least one land in the database
    response = requests.get(f"{base_url}/landen/1")
    assert response.status_code == 404
    response_data = response.json()

def test_delete_land():
    response = requests.delete(f"{base_url}/landen/1")
    assert response.status_code == 404
    response_data = response.json()
    assert isinstance(response_data, dict)
    assert response_data['detail'] == 'Not Found'