"""Test data fixtures. Each test gets its own user, prepared and cleaned up through the API."""

from typing import Iterator

import pytest

from blocks.users import create_account_via_api, delete_account_if_exists, new_unique_user, verify_account_does_not_exist
from entities.user import User
from web.api_actions import ApiActions


@pytest.fixture
def registered_user(api: ApiActions) -> Iterator[User]:
    """A user whose account already exists on the site."""
    user = new_unique_user()
    create_account_via_api(api, user)
    yield user
    # Removes the account through the API if the test did not delete it.
    delete_account_if_exists(api, user)


@pytest.fixture
def user_to_register(api: ApiActions) -> Iterator[User]:
    """A user with no account yet, for tests that create the account through the UI."""
    user = new_unique_user()
    verify_account_does_not_exist(api, user)
    yield user
    # Removes the account through the API if the test did not delete it.
    delete_account_if_exists(api, user)


@pytest.fixture
def unregistered_user(api: ApiActions) -> User:
    """A user with no account on the site."""
    user = new_unique_user()
    verify_account_does_not_exist(api, user)
    return user
