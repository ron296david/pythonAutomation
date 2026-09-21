"""Building blocks for registering a user, and deleting the account through the UI."""

from entities.user import User
from repository import signup as s
from web.web_actions import WebActions

from blocks.checks import check_box, expect_text, expect_url_path, expect_value, fill_field, select_field


def verify_new_user_signup_visible(web: WebActions) -> None:
    expect_text(web, "verify_new_user_signup_visible", s.NEW_USER_SIGNUP_TITLE, s.NEW_USER_SIGNUP_TEXT)


def signup(web: WebActions, user: User) -> None:
    block = "signup"
    _submit_signup(web, block, user)
    expect_url_path(web, block, s.SIGNUP_PATH)
    expect_text(web, block, s.ACCOUNT_INFO_TITLE, s.ACCOUNT_INFO_TEXT)


def signup_with_existing_email(web: WebActions, user: User) -> None:
    block = "signup_with_existing_email"
    _submit_signup(web, block, user)
    expect_url_path(web, block, s.SIGNUP_PATH)
    expect_text(web, block, s.SIGNUP_ERROR, s.SIGNUP_ERROR_EXISTING_EMAIL_TEXT)


def _submit_signup(web: WebActions, block: str, user: User) -> None:
    fill_field(web, block, "Signup name", s.SIGNUP_NAME, user.name)
    fill_field(web, block, "Signup email", s.SIGNUP_EMAIL, user.email)
    web.click(s.SIGNUP_BUTTON)


def fill_account_information(web: WebActions, user: User) -> None:
    block = "fill_account_information"
    title_radio = s.TITLE_RADIO[user.title]
    check_box(web, block, f"Title {user.title}", title_radio)
    fill_field(web, block, "Name", s.NAME, user.name)
    # The site fills the email from the signup step and does not allow editing it.
    expect_value(web, block, "Email", s.EMAIL, user.email)
    fill_field(web, block, "Password", s.PASSWORD, user.password)
    select_field(web, block, "Birth day", s.BIRTH_DAY, user.birth_day)
    select_field(web, block, "Birth month", s.BIRTH_MONTH, user.birth_month)
    select_field(web, block, "Birth year", s.BIRTH_YEAR, user.birth_year)
    if user.newsletter:
        check_box(web, block, "Sign up for our newsletter!", s.NEWSLETTER)
    if user.special_offers:
        check_box(web, block, "Receive special offers from our partners!", s.SPECIAL_OFFERS)


def fill_address_information(web: WebActions, user: User) -> None:
    block = "fill_address_information"
    fill_field(web, block, "First name", s.FIRST_NAME, user.first_name)
    fill_field(web, block, "Last name", s.LAST_NAME, user.last_name)
    fill_field(web, block, "Company", s.COMPANY, user.company)
    fill_field(web, block, "Address", s.ADDRESS1, user.address1)
    fill_field(web, block, "Address 2", s.ADDRESS2, user.address2)
    select_field(web, block, "Country", s.COUNTRY, user.country)
    fill_field(web, block, "State", s.STATE, user.state)
    fill_field(web, block, "City", s.CITY, user.city)
    fill_field(web, block, "Zipcode", s.ZIPCODE, user.zipcode)
    fill_field(web, block, "Mobile number", s.MOBILE_NUMBER, user.mobile_number)


def create_account(web: WebActions) -> None:
    block = "create_account"
    web.click(s.CREATE_ACCOUNT_BUTTON)
    expect_url_path(web, block, s.ACCOUNT_CREATED_PATH)
    expect_text(web, block, s.ACCOUNT_CREATED_TITLE, s.ACCOUNT_CREATED_TEXT)


def continue_after_account_created(web: WebActions, user: User) -> None:
    block = "continue_after_account_created"
    web.click(s.CONTINUE_BUTTON)
    expect_url_path(web, block, "/")
    expect_text(web, block, s.LOGGED_IN_AS, s.LOGGED_IN_AS_TEXT.format(name=user.name))


def delete_account(web: WebActions) -> None:
    block = "delete_account"
    web.click(s.DELETE_ACCOUNT_LINK)
    expect_url_path(web, block, s.ACCOUNT_DELETED_PATH)
    expect_text(web, block, s.ACCOUNT_DELETED_TITLE, s.ACCOUNT_DELETED_TEXT)


def continue_after_account_deleted(web: WebActions) -> None:
    block = "continue_after_account_deleted"
    web.click(s.CONTINUE_BUTTON)
    expect_url_path(web, block, "/")
