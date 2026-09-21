"""Shared verification helpers for building blocks. Each raises a clear AssertionError on failure."""

from urllib.parse import urlparse

from web.web_actions import WebActions


def expect_url_path(web: WebActions, block: str, path: str) -> None:
    if not web.wait_for_url(lambda url: urlparse(url).path == path):
        raise AssertionError(f"{block}: expected URL path '{path}', found URL '{web.current_url()}'")


def expect_text(web: WebActions, block: str, selector: str, expected: str) -> None:
    if not web.wait_for_visible(selector):
        raise AssertionError(
            f"{block}: expected '{expected}' to be visible at '{selector}', "
            f"element was not found (URL '{web.current_url()}')"
        )
    actual = web.read_text(selector).strip()
    if actual != expected:
        raise AssertionError(f"{block}: expected text '{expected}' at '{selector}', found '{actual}'")


def expect_not_visible(web: WebActions, block: str, selector: str, description: str) -> None:
    if not web.wait_for_hidden(selector):
        raise AssertionError(
            f"{block}: expected {description} ('{selector}') not to be visible, "
            f"it is visible with text '{web.read_text(selector).strip()}'"
        )


def expect_value(web: WebActions, block: str, field: str, selector: str, expected: str) -> None:
    actual = web.read_value(selector)
    if actual != expected:
        raise AssertionError(f"{block}: expected field '{field}' to be '{expected}', found '{actual}'")


def fill_field(web: WebActions, block: str, field: str, selector: str, value: str) -> None:
    web.write(selector, value)
    expect_value(web, block, field, selector, value)


def select_field(web: WebActions, block: str, field: str, selector: str, value: str) -> None:
    web.select(selector, value)
    expect_value(web, block, field, selector, value)


def check_box(web: WebActions, block: str, field: str, selector: str) -> None:
    web.check(selector)
    if not web.is_checked(selector):
        raise AssertionError(f"{block}: expected '{field}' to be checked, it is not checked")
