from dataclasses import dataclass


@dataclass(frozen=True)
class TopMenuTab:
    name: str
    link: str  # selector of the tab link in the top menu
    path: str  # URL path the tab leads to
    page_marker: str  # selector of an element unique to the tab's page


@dataclass(frozen=True)
class ExternalMenuLink:
    name: str
    link: str  # selector of the link in the top menu
    host: str  # host the link leads to
    path: str  # URL path the link leads to
    page_title: str  # selector of the title element on the external page
    expected_title: str  # exact text of that title
