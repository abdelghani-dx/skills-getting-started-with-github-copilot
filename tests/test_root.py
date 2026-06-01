"""
Tests for the root endpoint (GET /).

This module tests that the root endpoint correctly redirects to the static index.html file.
"""

import pytest


def test_root_redirect(client):
    """
    Test that GET / redirects to /static/index.html
    
    Arrange: Prepare the test client
    Act: Send GET request to /
    Assert: Verify redirect status and location header
    """
    # Arrange
    # client fixture is provided by conftest.py
    
    # Act
    response = client.get("/", follow_redirects=False)
    
    # Assert
    assert response.status_code in [307, 308]  # Temporary or permanent redirect
    assert response.headers["location"] == "/static/index.html"


def test_root_redirect_follow(client):
    """
    Test that following the redirect from GET / leads to success
    
    Arrange: Prepare the test client
    Act: Send GET request to / with follow_redirects=True
    Assert: Verify final response is successful (200 or similar)
    """
    # Arrange
    # client fixture is provided by conftest.py
    
    # Act
    response = client.get("/", follow_redirects=True)
    
    # Assert
    assert response.status_code == 200
