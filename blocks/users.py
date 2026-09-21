"""Building blocks for preparing and cleaning up users through the API."""

import dataclasses
import uuid

from entities.api_response import ApiResponse
from entities.user import EMAIL_DOMAIN, NEW_USER, User
from repository import account_api as a
from web.api_actions import ApiActions


def new_unique_user() -> User:
    """A new user with an email that no other test run uses."""
    return dataclasses.replace(NEW_USER, email=f"auto_{uuid.uuid4().hex}@{EMAIL_DOMAIN}")


def create_account_via_api(api: ApiActions, user: User) -> None:
    block = f"create_account_via_api('{user.email}')"

    created = api.post(
        a.CREATE_ACCOUNT,
        {
            "name": user.name,
            "email": user.email,
            "password": user.password,
            "title": user.title,
            "birth_date": user.birth_day,
            "birth_month": user.birth_month,
            "birth_year": user.birth_year,
            "firstname": user.first_name,
            "lastname": user.last_name,
            "company": user.company,
            "address1": user.address1,
            "address2": user.address2,
            "country": user.country,
            "zipcode": user.zipcode,
            "state": user.state,
            "city": user.city,
            "mobile_number": user.mobile_number,
        },
    )
    _expect_response_code(block, "create account", created, a.RESPONSE_CREATED)

    if _get_user_response_code(api, block, user) != a.RESPONSE_OK:
        raise AssertionError(f"{block}: account not found after the create API reported success")


def verify_account_does_not_exist(api: ApiActions, user: User) -> None:
    block = f"verify_account_does_not_exist('{user.email}')"
    if _get_user_response_code(api, block, user) != a.RESPONSE_NOT_FOUND:
        raise AssertionError(f"{block}: expected no account with this email, but one exists")


def delete_account_if_exists(api: ApiActions, user: User) -> None:
    block = f"delete_account_if_exists('{user.email}')"

    if _get_user_response_code(api, block, user) == a.RESPONSE_NOT_FOUND:
        return

    deleted = api.delete(a.DELETE_ACCOUNT, {"email": user.email, "password": user.password})
    _expect_response_code(block, "delete account", deleted, a.RESPONSE_OK)

    if _get_user_response_code(api, block, user) != a.RESPONSE_NOT_FOUND:
        raise AssertionError(f"{block}: account still exists after the delete API reported success")


def _get_user_response_code(api: ApiActions, block: str, user: User) -> int:
    response = api.get(a.GET_USER_DETAIL_BY_EMAIL, {"email": user.email})
    code = response.body.get("responseCode")
    if response.http_status != 200 or code not in (a.RESPONSE_OK, a.RESPONSE_NOT_FOUND):
        raise AssertionError(
            f"{block}: unexpected answer from get user detail: "
            f"HTTP {response.http_status}, body {response.body}"
        )
    return code


def _expect_response_code(block: str, action: str, response: ApiResponse, expected: int) -> None:
    code = response.body.get("responseCode")
    if response.http_status != 200 or code != expected:
        raise AssertionError(
            f"{block}: expected {action} responseCode {expected}, "
            f"found HTTP {response.http_status}, body {response.body}"
        )
