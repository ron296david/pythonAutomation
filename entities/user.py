from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    email: str
    password: str
    title: str  # "Mr" or "Mrs"
    birth_day: str
    birth_month: str  # month number, e.g. "5" for May
    birth_year: str
    newsletter: bool
    special_offers: bool
    first_name: str
    last_name: str
    company: str
    address1: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str
    mobile_number: str


# Template for new users. The email is replaced with a unique one for every test run.
NEW_USER = User(
    name="Auto Tester",
    email="",
    password="Auto#Pass123",
    title="Mr",
    birth_day="10",
    birth_month="5",
    birth_year="1990",
    newsletter=True,
    special_offers=True,
    first_name="Auto",
    last_name="Tester",
    company="Test Company",
    address1="1 Test Street",
    address2="Suite 2",
    country="United States",
    state="California",
    city="San Francisco",
    zipcode="94105",
    mobile_number="5551234567",
)

EMAIL_DOMAIN = "example.com"
