import pytest
from playwright.sync_api import Playwright, Page


pytest_plugins = (
    "fixtures.browsers",
    "fixtures.pages"
)
