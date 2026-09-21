from pathlib import Path
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item: pytest.Item) -> Iterator[None]:
    yield
    # Playwright saves a failed test's video as video.webm once the test's browser closes.
    # Tests run one at a time, so any video*.webm still there belongs to this test.
    output = item.config.rootpath / item.config.getoption("--output")
    videos = sorted(Path(output).glob("*/video*.webm"))
    for index, video in enumerate(videos, start=1):
        suffix = "" if len(videos) == 1 else f"-{index}"
        video.rename(video.with_name(f"{item.originalname}{suffix}.webm"))
