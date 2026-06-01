"""
Tests for the signup endpoint (POST /activities/{activity_name}/signup).

This module tests student signup functionality including happy path and error cases.
"""

import pytest


def test_signup_success(client):
    """
    Test successful student signup to an activity
    
    Arrange: Prepare test client and test data
    Act: Send POST request to signup endpoint
    Assert: Verify response status and student added to activity
    """
    # Arrange
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"
    
    # Verify student was added by checking activities
    activities_response = client.get("/activities")
    activities_data = activities_response.json()
    assert email in activities_data[activity_name]["participants"]


def test_signup_activity_not_found(client):
    """
    Test signup fails when activity does not exist
    
    Arrange: Prepare test client with non-existent activity name
    Act: Send POST request to signup endpoint
    Assert: Verify 404 error is returned
    """
    # Arrange
    activity_name = "Non-existent Activity"
    email = "student@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_duplicate_student(client):
    """
    Test signup fails when student is already signed up
    
    Arrange: Prepare test client with student already in activity
    Act: Send POST request to signup endpoint for existing participant
    Assert: Verify 400 error is returned
    """
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already in Chess Club
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"


def test_signup_multiple_activities(client):
    """
    Test student can sign up for multiple different activities
    
    Arrange: Prepare test client and unique email
    Act: Sign up for two different activities
    Assert: Verify student is in both activities
    """
    # Arrange
    email = "multi.student@mergington.edu"
    activity1 = "Chess Club"
    activity2 = "Programming Class"
    
    # Act - signup for first activity
    response1 = client.post(
        f"/activities/{activity1}/signup",
        params={"email": email}
    )
    
    # Act - signup for second activity
    response2 = client.post(
        f"/activities/{activity2}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response1.status_code == 200
    assert response2.status_code == 200
    
    # Verify student is in both activities
    activities_response = client.get("/activities")
    activities_data = activities_response.json()
    assert email in activities_data[activity1]["participants"]
    assert email in activities_data[activity2]["participants"]


def test_signup_different_students_same_activity(client):
    """
    Test multiple students can sign up for the same activity
    
    Arrange: Prepare test client with two different emails
    Act: Sign up both students for same activity
    Assert: Verify both are in the activity
    """
    # Arrange
    activity_name = "Drama Club"
    email1 = "student1@mergington.edu"
    email2 = "student2@mergington.edu"
    
    # Act - first student signup
    response1 = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email1}
    )
    
    # Act - second student signup
    response2 = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email2}
    )
    
    # Assert
    assert response1.status_code == 200
    assert response2.status_code == 200
    
    # Verify both students are in the activity
    activities_response = client.get("/activities")
    activities_data = activities_response.json()
    assert email1 in activities_data[activity_name]["participants"]
    assert email2 in activities_data[activity_name]["participants"]
