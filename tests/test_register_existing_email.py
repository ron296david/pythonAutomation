"""Test Case 5: Register User with existing email (https://www.automationexercise.com/test_cases)."""

from blocks.navigation import click_top_tab, open_home
from blocks.signup import signup_with_existing_email, verify_new_user_signup_visible
from entities.user import User
from repository.top_menu import SIGNUP_LOGIN
from web.web_actions import WebActions


def test_register_user_with_existing_email(web: WebActions, registered_user: User):
    open_home(web)                                    # 1-3. Launch, navigate, home page visible
    click_top_tab(web, SIGNUP_LOGIN)                  # 4. Click 'Signup / Login'
    verify_new_user_signup_visible(web)               # 5. 'New User Signup!' visible
    signup_with_existing_email(web, registered_user)  # 6-8. Enter name and registered email, Signup, error visible
