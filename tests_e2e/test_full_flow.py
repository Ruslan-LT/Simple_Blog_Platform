import pytest
from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:8000"


@pytest.fixture
def test_user_data():
    return {
        "username": "testuser_e2e",
        "password": "StrongPass123",
        "email": "testuser@example.com",
    }


def test_full_user_flow(page: Page, test_user_data):
    page.goto(BASE_URL)
    expect(page).to_have_title("Simple Blog Platform")

    page.click("text=Sign Up")

    page.fill("#id_username", test_user_data["username"])
    page.fill("#id_email", test_user_data["email"])
    page.fill("#id_password1", test_user_data["password"])
    page.fill("#id_password2", test_user_data["password"])
    page.click("text=Register")

    expect(page.locator(".alert-success")).to_contain_text("successfully registered")

    page.click("text=Login")
    page.fill("#id_username", test_user_data["username"])
    page.fill("#id_password", test_user_data["password"])
    page.click("text=Login")

    expect(page.locator("text=Logout")).to_be_visible()

    page.click("text=Create Post")
    page.fill("#id_title", "E2E Test Post")
    page.fill("#id_content", "This is an automated E2E test post.")
    page.click("text=Publish")

    expect(page.locator("text=E2E Test Post")).to_be_visible()
    expect(page.locator("text=This is an automated E2E test post.")).to_be_visible()
