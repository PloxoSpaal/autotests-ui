from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')

    def check_visible(self, email: str | None = None, username: str | None = None, password: str | None = None):
        expect(self.email_input).to_be_visible()
        if email is not None:
            expect(self.email_input).to_have_value(email)

        expect(self.username_input).to_be_visible()
        if username is not None:
            expect(self.username_input).to_have_value(username)

        expect(self.password_input).to_be_visible()
        if password is not None:
            expect(self.password_input).to_have_value(password)

    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.email_input.fill(username)
        expect(self.email_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)
