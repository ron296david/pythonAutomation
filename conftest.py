from typing import Iterator

import pytest
from playwright.sync_api import Page, Playwright

from repository.blocked_hosts import AD_HOSTS
from web.api_actions import ApiActions
from web.web_actions import WebActions


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict) -> dict:
    return {**browser_type_launch_args, "args": ["--start-maximized"]}


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    # No fixed viewport, so the page fills the maximized window.
    return {**browser_context_args, "no_viewport": True}


@pytest.fixture
def web(page: Page) -> WebActions:
    web = WebActions(page)
    web.block_hosts(AD_HOSTS)
    return web


@pytest.fixture
def api(playwright: Playwright, base_url: str) -> Iterator[ApiActions]:
    request = playwright.request.new_context(base_url=base_url)
    yield ApiActions(request)
    request.dispose()
