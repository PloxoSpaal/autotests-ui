from playwright.sync_api import sync_playwright, expect, Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(
        dashboard_page: DashboardPage, registration_page: RegistrationPage,
        email: str, username: str, password: str):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email='email@gmail.com', username='username', password='password')
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()

