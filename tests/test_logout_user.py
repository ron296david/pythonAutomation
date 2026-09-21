"""Test Case 4: Logout User (https://www.automationexercise.com/test_cases)."""

from blocks.login import login, logout
from blocks.navigation import click_top_tab, open_home
from entities.menu import SIGNUP_LOGIN
from entities.user import User
from web.web_actions import WebActions


def test_logout_user(web: WebActions, registered_user: User):
    open_home(web)                                # 1-3. Launch, navigate, home page visible
    click_top_tab(web, SIGNUP_LOGIN)              # 4-5. Click 'Signup / Login', 'Login to your account' visible
    login(web, registered_user)                   # 6-8. Enter email and password, Login, 'Logged in as username' visible
    logout(web)                                   # 9-10. Click 'Logout', navigated to login page
