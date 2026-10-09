import pytest
from playwright.sync_api import Page

@pytest.fixture
def context(context):
    context.set_default_timeout(10_000)
    return context

@pytest.fixture
def timer_app_page(page: Page):
    """Öppnar Timer app."""
    page.goto("https://lejonmanen.github.io/timer-vue/")
    return page