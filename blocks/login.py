"""Building blocks for logging in and out through the UI."""

from entities.user import User
from repository import login as l
from repository import signup as s
from repository.top_menu import SIGNUP_LOGIN
from web.web_actions import WebActions

from blocks.checks import expect_not_visible, expect_text, expect_url_path, fill_field
from blocks.navigation import verify_on_tab


def login(web: WebActions, user: User) -> None:
    block = "login"
    _submit_login(web, block, user)
    expect_url_path(web, block, "/")
    expect_text(web, block, s.LOGGED_IN_AS, s.LOGGED_IN_AS_TEXT.format(name=user.name))


def login_with_incorrect_credentials(web: WebActions, user: User) -> None:
    block = "login_with_incorrect_credentials"
    _submit_login(web, block, user)
    expect_url_path(web, block, l.LOGIN_PATH)
    expect_text(web, block, l.LOGIN_ERROR, l.LOGIN_ERROR_TEXT)
    expect_not_visible(web, block, s.LOGGED_IN_AS, "'Logged in as' in the top menu")


def logout(web: WebActions) -> None:
    block = "logout"
    web.click(l.LOGOUT_LINK)
    verify_on_tab(web, SIGNUP_LOGIN, block)
    expect_not_visible(web, block, s.LOGGED_IN_AS, "'Logged in as' in the top menu")


def _submit_login(web: WebActions, block: str, user: User) -> None:
    fill_field(web, block, "Login email", l.LOGIN_EMAIL, user.email)
    fill_field(web, block, "Login password", l.LOGIN_PASSWORD, user.password)
    web.click(l.LOGIN_BUTTON)
