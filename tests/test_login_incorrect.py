"""Test Case 3: Login User with incorrect email and password (https://www.automationexercise.com/test_cases)."""

from blocks.login import login_with_incorrect_credentials
from blocks.navigation import click_top_tab, open_home
from entities.user import User
from repository.top_menu import SIGNUP_LOGIN
from web.web_actions import WebActions


def test_login_user_with_incorrect_email_and_password(web: WebActions, unregistered_user: User):
    open_home(web)                                          # 1-3. Launch, navigate, home page visible
    click_top_tab(web, SIGNUP_LOGIN)                        # 4-5. Click 'Signup / Login', 'Login to your account' visible
    login_with_incorrect_credentials(web, unregistered_user)  # 6-8. Enter incorrect email and password, Login, error visible
