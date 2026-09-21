"""Repository: top menu selectors and the data that identifies each tab's page."""

from entities.menu import ExternalMenuLink, TopMenuTab


# The site marks the tab of the current page with this inline style.
ACTIVE_TAB_STYLE = "color: orange"

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
