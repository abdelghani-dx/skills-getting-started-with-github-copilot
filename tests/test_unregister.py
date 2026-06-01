"""
Tests for the unregister endpoint (DELETE /activities/{activity_name}/unregister).

This module tests student unregistration functionality including happy path and error cases.
"""

import pytest


def test_unregister_success(client):
    """
    Test successful student unregistration from an activity
    
    Arrange: Prepare test client and existing participant
    Act: Send DELETE request to unregister endpoint
    Assert: Verify response status and student removed from activity
    """
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already in Chess Club
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    
    # Verify student was removed
    activities_response = client.get("/activities")
    activities_data = activities_response.json()
    assert email not in activities_data[activity_name]["participants"]


def test_unregister_activity_not_found(client):
    """
    Test unregister fails when activity does not exist
    
    Arrange: Prepare test client with non-existent activity name
    Act: Send DELETE request to unregister endpoint
    Assert: Verify 404 error is returned
    """
    # Arrange
    activity_name = "Non-existent Activity"
    email = "student@mergington.edu"
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_student_not_signed_up(client):
    """
    Test unregister fails when student is not signed up for activity
    
    Arrange: Prepare test client with student not in activity
    Act: Send DELETE request to unregister endpoint
    Assert: Verify 400 error is returned
    """
    # Arrange
    activity_name = "Chess Club"
    email = "not.signed.up@mergington.edu"
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student not signed up for this activity"


def test_unregister_then_signup_again(client):
    """
    Test student can unregister and sign up again
    
    Arrange: Prepare test client with existing participant
    Act: Unregister student, then sign up again
    Assert: Verify student is back in activity
    """
    # Arrange
    activity_name = "Programming Class"
    email = "emma@mergington.edu"  # Already in Programming Class
    
    # Act - unregister
    response1 = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )
    
    # Verify unregistered
    activities_response = client.get("/activities")
    activities_data = activities_response.json()
    assert email not in activities_data[activity_name]["participants"]
    
    # Act - signup again
    response2 = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response1.status_code == 200
    assert response2.status_code == 200
    
    # Verify student is back in activity
    activities_response = client.get("/activities")
    activities_data = activities_response.json()
    assert email in activities_data[activity_name]["participants"]


def test_unregister_one_of_many_participants(client):
    """
    Test unregistering one student doesn't affect other students in activity
    
    Arrange: Prepare test client with multiple participants
    Act: Unregister one student
    Assert: Verify other students remain in activity
    """
    # Arrange
    activity_name = "Chess Club"
    email_to_remove = "michael@mergington.edu"
    email_to_keep = "daniel@mergington.edu"
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email_to_remove}
    )
    
    # Assert
    assert response.status_code == 200
    
    # Verify removed student is gone
    activities_response = client.get("/activities")
    activities_data = activities_response.json()
    assert email_to_remove not in activities_data[activity_name]["participants"]
    
    # Verify other student is still there
    assert email_to_keep in activities_data[activity_name]["participants"]


def test_unregister_duplicate_attempt(client):
    """
    Test that attempting to unregister twice fails on second attempt
    
    Arrange: Prepare test client with existing participant
    Act: Unregister student, then attempt to unregister again
    Assert: Verify second attempt fails with 400 error
    """
    # Arrange
    activity_name = "Gym Class"
    email = "john@mergington.edu"  # Already in Gym Class
    
    # Act - first unregister
    response1 = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )
    
    # Act - attempt second unregister
    response2 = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )
    
    # Assert
    assert response1.status_code == 200
    assert response2.status_code == 400
    assert response2.json()["detail"] == "Student not signed up for this activity"
