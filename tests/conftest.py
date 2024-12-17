import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function", params=["standard_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"])
def test_user(request):
    """Фикстура для передачи текущего юзера"""
    return request.param

@pytest.fixture(scope="function", params=["chromium", "firefox",])
def browser_page(request):
    """Фикстура для запуска тестов в разных браузерах."""
    browser_type = request.param
    with sync_playwright() as playwright:
        browser = getattr(playwright, browser_type).launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()
