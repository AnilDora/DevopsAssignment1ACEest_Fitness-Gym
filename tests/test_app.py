import pytest
from app import app, workouts


@pytest.fixture
def client():
    # Flask provides a test client for simulating requests
    app.config["TESTING"] = True
    with app.test_client() as client:
        # clear workouts before each test to ensure isolation
        workouts.clear()
        yield client

def test_homepage_loads(client):
    """Homepage should return 200 and contain welcome text"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to ACEest Fitness & Gym" in response.data

def test_add_workout_valid(client):
    """Valid workout should be added and redirected to workouts page"""
    response = client.post("/add", data={
        "workout": "Push-ups",
        "duration": "15"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Push-ups" in response.data
    assert b"15 minutes" in response.data
    assert len(workouts) == 1

def test_add_workout_missing_fields(client):
    """Missing input should flash an error and not add a workout"""
    response = client.post("/add", data={
        "workout": "",
        "duration": ""
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Please enter both workout and duration." in response.data
    assert len(workouts) == 0

def test_add_workout_invalid_duration(client):
    """Non-numeric duration should flash an error"""
    response = client.post("/add", data={
        "workout": "Jogging",
        "duration": "abc"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Duration must be a number." in response.data
    assert len(workouts) == 0

def test_view_workouts_empty(client):
    """View workouts should display message when no workouts logged"""
    response = client.get("/workouts")
    assert response.status_code == 200
    assert b"No workouts logged yet." in response.data

def test_view_workouts_with_data(client):
    """View workouts should display logged workouts"""
    workouts.append({"workout": "Squats", "duration": 20})
    response = client.get("/workouts")
    assert response.status_code == 200
    assert b"Squats" in response.data
    assert b"20 minutes" in response.data
