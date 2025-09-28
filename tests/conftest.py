import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture
def initialize_browser_state(chromium_page):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    email_input.fill('test@gmail.com')
    username_input.fill('TestTestovich')
    password_input.fill('g00dPa$$w0rd')
    registration_button.click()
    chromium_page.context.storage_state(path="browser-state.json")

@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    yield context.new_page()
    context.close()
    browser.close()