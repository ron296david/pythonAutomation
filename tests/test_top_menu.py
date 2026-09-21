from blocks.navigation import click_top_tab, click_video_tutorials, go_back_to_tab, open_home
from entities.menu import (
    API_TESTING,
    CART,
    CONTACT_US,
    HOME,
    PRODUCTS,
    SIGNUP_LOGIN,
    TEST_CASES,
)
from web.web_actions import WebActions


def test_click_top_menu_tabs(web: WebActions):
    open_home(web)

    click_top_tab(web, HOME)
    click_top_tab(web, PRODUCTS)
    click_top_tab(web, CART)
    click_top_tab(web, SIGNUP_LOGIN)
    click_top_tab(web, TEST_CASES)
    click_top_tab(web, API_TESTING)
    click_video_tutorials(web)
    go_back_to_tab(web, API_TESTING)
    click_top_tab(web, CONTACT_US)
