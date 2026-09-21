"""Building blocks for moving around the site. Every block verifies its own result."""

from urllib.parse import urlparse

from entities.menu import HOME, VIDEO_TUTORIALS, TopMenuTab
from repository.top_menu import ACTIVE_TAB_STYLE
from web.web_actions import WebActions


def open_home(web: WebActions) -> None:
    web.open(HOME.path)
    verify_on_tab(web, HOME, block="open_home")


def click_top_tab(web: WebActions, tab: TopMenuTab) -> None:
    web.click(tab.link)
    verify_on_tab(web, tab, block=f"click_top_tab('{tab.name}')")


def click_video_tutorials(web: WebActions) -> None:
    block = "click_video_tutorials"
    target = VIDEO_TUTORIALS
    web.click(target.link)

    def is_target(url: str) -> bool:
        parsed = urlparse(url)
        return parsed.hostname == target.host and parsed.path == target.path

    if not web.wait_for_url(is_target):
        raise AssertionError(
            f"{block}: expected URL 'https://{target.host}{target.path}', found URL '{web.current_url()}'"
        )

    if not web.wait_for_visible(target.page_title):
        raise AssertionError(
            f"{block}: expected title element '{target.page_title}' to be visible, "
            f"it was not found (URL '{web.current_url()}')"
        )

    title = web.read_text(target.page_title).strip()
    if title != target.expected_title:
        raise AssertionError(f"{block}: expected title '{target.expected_title}', found '{title}'")


def go_back_to_tab(web: WebActions, tab: TopMenuTab) -> None:
    web.go_back()
    verify_on_tab(web, tab, block=f"go_back_to_tab('{tab.name}')")


def verify_on_tab(web: WebActions, tab: TopMenuTab, block: str) -> None:
    """Verify the browser is on the tab's page: URL, page element, and highlighted tab."""
    if not web.wait_for_url(lambda url: urlparse(url).path == tab.path):
        raise AssertionError(
            f"{block}: expected URL path '{tab.path}', found URL '{web.current_url()}'"
        )

    if not web.wait_for_visible(tab.page_marker):
        raise AssertionError(
            f"{block}: expected '{tab.name}' page element '{tab.page_marker}' to be visible, "
            f"it was not found (URL '{web.current_url()}')"
        )

    style = web.read_attribute(tab.link, "style") or ""
    if ACTIVE_TAB_STYLE not in style:
        raise AssertionError(
            f"{block}: expected tab '{tab.name}' to be highlighted with '{ACTIVE_TAB_STYLE}', "
            f"found style '{style}'"
        )
