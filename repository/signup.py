"""Repository: selectors and expected texts for signup, account and logged-in pages."""

# Signup / Login page
NEW_USER_SIGNUP_TITLE = ".signup-form h2"
NEW_USER_SIGNUP_TEXT = "New User Signup!"
SIGNUP_NAME = '[data-qa="signup-name"]'
SIGNUP_EMAIL = '[data-qa="signup-email"]'
SIGNUP_BUTTON = '[data-qa="signup-button"]'
SIGNUP_ERROR = ".signup-form form p"
SIGNUP_ERROR_EXISTING_EMAIL_TEXT = "Email Address already exist!"

# Account information page
SIGNUP_PATH = "/signup"
ACCOUNT_INFO_TITLE = 'h2.title:has-text("Enter Account Information")'
ACCOUNT_INFO_TEXT = "ENTER ACCOUNT INFORMATION"
TITLE_RADIO = {"Mr": "#id_gender1", "Mrs": "#id_gender2"}
NAME = '[data-qa="name"]'
EMAIL = '[data-qa="email"]'
PASSWORD = '[data-qa="password"]'
BIRTH_DAY = '[data-qa="days"]'
BIRTH_MONTH = '[data-qa="months"]'
BIRTH_YEAR = '[data-qa="years"]'
NEWSLETTER = "#newsletter"
SPECIAL_OFFERS = "#optin"

# Address information (same page)
FIRST_NAME = '[data-qa="first_name"]'
LAST_NAME = '[data-qa="last_name"]'
COMPANY = '[data-qa="company"]'
ADDRESS1 = '[data-qa="address"]'
ADDRESS2 = '[data-qa="address2"]'
COUNTRY = '[data-qa="country"]'
STATE = '[data-qa="state"]'
CITY = '[data-qa="city"]'
ZIPCODE = '[data-qa="zipcode"]'
MOBILE_NUMBER = '[data-qa="mobile_number"]'
CREATE_ACCOUNT_BUTTON = '[data-qa="create-account"]'

# Account created page
ACCOUNT_CREATED_PATH = "/account_created"
ACCOUNT_CREATED_TITLE = '[data-qa="account-created"]'
ACCOUNT_CREATED_TEXT = "ACCOUNT CREATED!"
CONTINUE_BUTTON = '[data-qa="continue-button"]'

# Logged-in top menu
LOGGED_IN_AS = '.shop-menu a:has-text("Logged in as")'
LOGGED_IN_AS_TEXT = "Logged in as {name}"
DELETE_ACCOUNT_LINK = '.shop-menu a[href="/delete_account"]'

# Account deleted page
ACCOUNT_DELETED_PATH = "/delete_account"
ACCOUNT_DELETED_TITLE = '[data-qa="account-deleted"]'
ACCOUNT_DELETED_TEXT = "ACCOUNT DELETED!"
