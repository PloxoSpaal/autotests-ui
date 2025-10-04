from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import pytest


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    def test_successful_registration(self,
            dashboard_page: DashboardPage, registration_page: RegistrationPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.check_visible()
        registration_page.registration_form.fill(email='email@gmail.com', username='username', password='password')
        registration_page.click_registration_button()
        dashboard_page.toolbar.check_visible()

