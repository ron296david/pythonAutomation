"""Web access layer: the only layer that calls Playwright."""

from typing import Callable
from urllib.parse import urlparse

from playwright.sync_api import Page, Route
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

DEFAULT_TIMEOUT_MS = 10_000


class WebActions:
    def __init__(self, page: Page, timeout_ms: int = DEFAULT_TIMEOUT_MS):
        self._page = page
        self._timeout_ms = timeout_ms

    def block_hosts(self, hosts: list[str]) -> None:
        """Abort every request to the given hosts and their subdomains."""

        def is_blocked(url: str) -> bool:
            host = urlparse(url).hostname or ""
            return any(host == h or host.endswith("." + h) for h in hosts)

        def abort(route: Route) -> None:
            route.abort()

        self._page.route(is_blocked, abort)

    def open(self, path: str) -> None:
        self._page.goto(path, timeout=self._timeout_ms)

    def go_back(self) -> None:
        self._page.go_back(timeout=self._timeout_ms)

    def click(self, selector: str) -> None:
        self._page.locator(selector).click(timeout=self._timeout_ms)

    def write(self, selector: str, text: str) -> None:
        self._page.locator(selector).fill(text, timeout=self._timeout_ms)

    def select(self, selector: str, value: str) -> None:
        self._page.locator(selector).select_option(value, timeout=self._timeout_ms)

    def check(self, selector: str) -> None:
        self._page.locator(selector).check(timeout=self._timeout_ms)

    def is_checked(self, selector: str) -> bool:
        return self._page.locator(selector).is_checked(timeout=self._timeout_ms)

    def read_value(self, selector: str) -> str:
        return self._page.locator(selector).input_value(timeout=self._timeout_ms)

    def read_text(self, selector: str) -> str:
        return self._page.locator(selector).inner_text(timeout=self._timeout_ms)

    def read_attribute(self, selector: str, name: str) -> str | None:
        return self._page.locator(selector).get_attribute(name, timeout=self._timeout_ms)

    def pause(self) -> None:
        """Stop and open the Playwright Inspector until the user clicks Resume (headed runs only)."""
        self._page.pause()

    def current_url(self) -> str:
        return self._page.url

    def wait_for_url(self, matches: Callable[[str], bool]) -> bool:
        """Return True once the URL matches, False if it does not match within the timeout."""
        try:
            self._page.wait_for_url(matches, timeout=self._timeout_ms)
            return True
        except PlaywrightTimeoutError:
            return False

    def wait_for_hidden(self, selector: str) -> bool:
        """Return True once the element is hidden or absent, False if it is still visible after the timeout."""
        try:
            self._page.locator(selector).wait_for(state="hidden", timeout=self._timeout_ms)
            return True
        except PlaywrightTimeoutError:
            return False

    def wait_for_visible(self, selector: str) -> bool:
        """Return True once the element is visible, False if it is not visible within the timeout."""
        try:
            self._page.locator(selector).wait_for(state="visible", timeout=self._timeout_ms)
            return True
        except PlaywrightTimeoutError:
            return False
