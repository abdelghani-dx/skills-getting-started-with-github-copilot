# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey abdelghani-dx!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/abdelghani-dx/skills-getting-started-with-github-copilot/issues/1)

---

## Running Tests

This project includes a comprehensive test suite for the FastAPI backend. Tests follow the AAA (Arrange-Act-Assert) pattern for clarity and maintainability.

### Test Structure

Tests are organized in the `tests/` directory by feature:

- **`tests/test_root.py`** — Tests for the root endpoint (`GET /`)
- **`tests/test_activities.py`** — Tests for the activities endpoint (`GET /activities`)
- **`tests/test_signup.py`** — Tests for student signup (`POST /activities/{activity_name}/signup`)
- **`tests/test_unregister.py`** — Tests for student unregistration (`DELETE /activities/{activity_name}/unregister`)
- **`tests/conftest.py`** — Shared pytest fixtures and test configuration

### Running Tests

Before running tests, ensure dependencies are installed:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run tests with coverage report:

```bash
pytest --cov=src --cov-report=term-missing
```

Run a specific test file:

```bash
pytest tests/test_activities.py
```

Run a specific test:

```bash
pytest tests/test_signup.py::test_signup_success
```

### Test Coverage

The test suite provides comprehensive coverage including:

- **Happy path scenarios** — Successful operations
- **Error cases** — Invalid activities, duplicate signups, unregistration errors
- **Edge cases** — Multiple participants, signing up for multiple activities
- **Data integrity** — Verification that changes persist correctly

Target coverage is >80% of the backend code.

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

