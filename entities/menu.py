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


HOME = TopMenuTab("Home", '.shop-menu a[href="/"]', "/", 'h2.title:text-is("Features Items")')
PRODUCTS = TopMenuTab("Products", '.shop-menu a[href="/products"]', "/products", 'h2.title:text-is("All Products")')
CART = TopMenuTab("Cart", '.shop-menu a[href="/view_cart"]', "/view_cart", '.breadcrumb li.active:text-is("Shopping Cart")')
SIGNUP_LOGIN = TopMenuTab("Signup / Login", '.shop-menu a[href="/login"]', "/login", 'h2:text-is("Login to your account")')
TEST_CASES = TopMenuTab("Test Cases", '.shop-menu a[href="/test_cases"]', "/test_cases", 'h2.title b:text-is("Test Cases")')
API_TESTING = TopMenuTab("API Testing", '.shop-menu a[href="/api_list"]', "/api_list", 'h2.title b:text-is("APIs List for practice")')
CONTACT_US = TopMenuTab("Contact us", '.shop-menu a[href="/contact_us"]', "/contact_us", 'h2.title:text-is("Get In Touch")')

VIDEO_TUTORIALS = ExternalMenuLink(
    "Video Tutorials",
    '.shop-menu a[href="https://www.youtube.com/c/AutomationExercise"]',
    "www.youtube.com",
    "/c/AutomationExercise",
    "yt-page-header-renderer h1",
    "AutomationExercise",
)
