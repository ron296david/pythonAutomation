"""Test Case 1: Register User (https://www.automationexercise.com/test_cases)."""

from blocks.navigation import click_top_tab, open_home
from blocks.signup import (
    continue_after_account_created,
    continue_after_account_deleted,
    create_account,
    delete_account,
    fill_account_information,
    fill_address_information,
    signup,
    verify_new_user_signup_visible,
)
from entities.menu import SIGNUP_LOGIN
from entities.user import User
from web.web_actions import WebActions


def test_register_user(web: WebActions, user_to_register: User):
    user = user_to_register
    open_home(web)                                # 1-3. Launch, navigate, home page visible
    click_top_tab(web, SIGNUP_LOGIN)              # 4. Click 'Signup / Login'
    verify_new_user_signup_visible(web)           # 5. 'New User Signup!' visible
    signup(web, user)                             # 6-8. Enter name and email, Signup, 'ENTER ACCOUNT INFORMATION' visible
    fill_account_information(web, user)           # 9-11. Title, name, email, password, birth date, both checkboxes
    fill_address_information(web, user)           # 12. Address details
    create_account(web)                           # 13-14. Create Account, 'ACCOUNT CREATED!' visible
    continue_after_account_created(web, user)     # 15-16. Continue, 'Logged in as username' visible
    delete_account(web)                           # 17-18. Delete Account, 'ACCOUNT DELETED!' visible
    continue_after_account_deleted(web)           # 18. Click 'Continue'
