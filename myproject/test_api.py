from datetime import date
from fastapi.testclient import TestClient

from myproject.main import app
from myproject.models import Festival

client = TestClient(app)

# Define testing headers with token
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

def test_create_festival():
    """Test creating a new festival."""
    festival_data = {
        "naam": "Test Festival",
        "locatie": "Test Location",
        "start_datum": str(date.today()),
        "eind_datum": str(date.today()),
        "land_id": 1
    }

    response = client.post("/festivals", json=festival_data, headers=headers)

    assert response.status_code == 201
    created_festival = response.json()
    assert isinstance(created_festival, Festival)
    assert created_festival.naam == festival_data["naam"]

def test_get_festivals():
    """Test getting a list of festivals."""
    response = client.get("/festivals", headers=headers)

    assert response.status_code == 200
    festivals = response.json()
    assert isinstance(festivals, list)
    assert all(isinstance(festival, Festival) for festival in festivals)

def test_get_festival():
    """Test getting a specific festival by ID."""
    response = client.get("/festivals/1", headers=headers)

    assert response.status_code == 200
    festival = response.json()
    assert isinstance(festival, Festival)

def test_update_festival():
    """Test updating an existing festival."""
    festival_data = {
        "naam": "Updated Festival",
        "locatie": "Updated Location",
        "start_datum": str(date.today()),
        "eind_datum": str(date.today()),
        "land_id": 1
    }

    response = client.put("/festivals/1", json=festival_data, headers=headers)

    assert response.status_code == 200
    updated_festival = response.json()
    assert isinstance(updated_festival, Festival)
    assert updated_festival.naam == festival_data["naam"]

def test_delete_festival():
    """Test deleting a festival by ID."""
    response = client.delete("/festivals/1", headers=headers)

    assert response.status_code == 200
    assert response.json() == {"message": "Festival deleted successfully"}
