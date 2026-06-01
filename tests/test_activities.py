"""
Tests for the activities endpoint (GET /activities).

This module tests that the activities endpoint returns all activities with correct structure and data.
"""

import pytest


def test_get_all_activities(client):
    """
    Test that GET /activities returns all 9 activities
    
    Arrange: Prepare the test client
    Act: Send GET request to /activities
    Assert: Verify response status and activity count
    """
    # Arrange
    expected_count = 9
    
    # Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == expected_count


def test_activities_response_structure(client):
    """
    Test that activities have correct data structure
    
    Arrange: Prepare the test client
    Act: Send GET request to /activities
    Assert: Verify each activity has required fields
    """
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}
    
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert response.status_code == 200
    for activity_name, activity_data in data.items():
        assert isinstance(activity_name, str)
        assert isinstance(activity_data, dict)
        assert required_fields.issubset(set(activity_data.keys()))


def test_activities_specific_data(client):
    """
    Test that specific activities contain expected data
    
    Arrange: Prepare the test client
    Act: Send GET request to /activities
    Assert: Verify Chess Club and Programming Class data
    """
    # Arrange
    # client fixture is provided by conftest.py
    
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert response.status_code == 200
    
    # Verify Chess Club exists and has correct data
    assert "Chess Club" in data
    chess_club = data["Chess Club"]
    assert chess_club["max_participants"] == 12
    assert "michael@mergington.edu" in chess_club["participants"]
    assert "daniel@mergington.edu" in chess_club["participants"]
    assert len(chess_club["participants"]) == 2
    
    # Verify Programming Class exists and has correct data
    assert "Programming Class" in data
    prog_class = data["Programming Class"]
    assert prog_class["max_participants"] == 20
    assert "emma@mergington.edu" in prog_class["participants"]
    assert "sophia@mergington.edu" in prog_class["participants"]


def test_activities_participants_list_type(client):
    """
    Test that participants are stored as a list
    
    Arrange: Prepare the test client
    Act: Send GET request to /activities
    Assert: Verify participants field is a list
    """
    # Arrange
    # client fixture is provided by conftest.py
    
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert response.status_code == 200
    for activity_name, activity_data in data.items():
        assert isinstance(activity_data["participants"], list)
        for participant in activity_data["participants"]:
            assert isinstance(participant, str)
