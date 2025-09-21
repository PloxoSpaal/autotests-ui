from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_button = page.get_by_test_id('registration-page-registration-button')
    email_input.fill('test@gmail.com')
    username_input.fill('TestTestovich')
    password_input.fill('g00dPa$$w0rd')
    registration_button.click()
    text = page.get_by_test_id('dashboard-toolbar-title-text')
    assert text.text_content() == 'Dashboard', 'Text Not Found'
