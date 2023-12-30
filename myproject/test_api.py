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
    assert response.status_code == 200
    response_data = response.json()
    assert "message" in response_data
    assert response_data["message"] == 'Festival created successfully'

def test_read_festivals():
    response = requests.get(f"{base_url}/festivals")
    assert response.status_code == 200
    festivals = response.json()
    assert isinstance(festivals, list)

def test_read_festival():
    # Assuming there is at least one festival in the database
    response = requests.get(f"{base_url}/festivals/1")
    assert response.status_code == 200
    festival = response.json()
    assert isinstance(festival, dict)

def test_update_festival():
    festival_data = {
        "naam": "Updated Festival",
        "locatie": "Updated Location",
        "start_datum": "2023-01-01",
        "eind_datum": "2023-01-02",
        "land_id": 1
    }
    response = requests.put(f"{base_url}/festivals/1", json=festival_data)
    assert response.status_code == 200
    updated_festival = response.json()
    assert updated_festival["naam"] == festival_data["naam"]

def test_delete_festival():
    response = requests.delete(f"{base_url}/festivals/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Festival deleted successfully"}
