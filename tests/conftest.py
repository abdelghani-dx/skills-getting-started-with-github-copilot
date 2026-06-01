"""
Pytest configuration and shared fixtures for FastAPI tests.

This module provides reusable fixtures for testing the Mergington High School API.
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """
    Fixture that provides a TestClient instance for the FastAPI app.
    
    This fixture automatically resets the in-memory activities database
    to its initial state before each test to ensure test isolation.
    """
    # Reset activities to initial state before each test
    initial_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Soccer Team": {
            "description": "Join the school soccer team for training and matches",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 22,
            "participants": ["sam@mergington.edu", "alex@mergington.edu"]
        },
        "Swimming Club": {
            "description": "Practice swimming techniques and prepare for competitions",
            "schedule": "Mondays, Wednesdays, 5:00 PM - 6:30 PM",
            "max_participants": 18,
            "participants": ["mia@mergington.edu", "noah@mergington.edu"]
        },
        "Art Club": {
            "description": "Explore drawing, painting, and other visual arts",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": ["lily@mergington.edu", "jack@mergington.edu"]
        },
        "Drama Club": {
            "description": "Rehearse plays and perform drama productions",
            "schedule": "Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 20,
            "participants": ["ava@mergington.edu", "ethan@mergington.edu"]
        },
        "Debate Team": {
            "description": "Prepare for debate competitions and practice public speaking",
            "schedule": "Mondays and Fridays, 3:30 PM - 4:30 PM",
            "max_participants": 16,
            "participants": ["sophia@mergington.edu", "oliver@mergington.edu"]
        },
        "Science Olympiad": {
            "description": "Work on science and engineering challenges for tournaments",
            "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["chloe@mergington.edu", "liam@mergington.edu"]
        }
    }
    
    # Clear current activities
    activities.clear()
    
    # Reset to initial state
    activities.update(initial_activities)
    
    # Return test client
    return TestClient(app)
