"""Test Case 2: Login User with correct email and password (https://www.automationexercise.com/test_cases)."""

from blocks.login import login
from blocks.navigation import click_top_tab, open_home
from blocks.signup import delete_account
from entities.user import User
from repository.top_menu import SIGNUP_LOGIN
from web.web_actions import WebActions


def test_login_user_with_correct_email_and_password(web: WebActions, registered_user: User):
    open_home(web)                                # 1-3. Launch, navigate, home page visible
    click_top_tab(web, SIGNUP_LOGIN)              # 4-5. Click 'Signup / Login', 'Login to your account' visible
    login(web, registered_user)                   # 6-8. Enter email and password, Login, 'Logged in as username' visible
    delete_account(web)                           # 9-10. Delete Account, 'ACCOUNT DELETED!' visible
