from playwright.sync_api import sync_playwright
import config
import time

def create_affine_note(text: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config.IS_DEBUG is False)
        page = browser.new_page()

        page.goto(config.AFFINE_WORKSPACE_URL)

        page.fill('input[placeholder="Enter your email address"]', config.AFFINE_USER_EMAIL)
        page.click('[data-testid="continue-login-button"]')
        page.fill('input[data-testid="password-input"]', config.AFFINE_USER_PASSWORD)
        page.click('button[data-testid="sign-in-button"]')
        page.click('button[data-testid="modal-close-button"]')
        page.click('div[data-testid="slider-bar-journals-button"]')
        page.click('div[data-testid="page-editor-blank"]')
        locator = page.locator('div[data-testid="page-editor-blank"]')
        locator.focus()
        locator.press_sequentially(text)
        locator.press('Enter')

        time.sleep(10)
        browser.close()