from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')
        self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    def click_registration_button(self):
        self.registration_button.click()

    def click_registration_link(self):
        self.login_link.click()
