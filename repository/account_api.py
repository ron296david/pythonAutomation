"""Repository: account API endpoints and response codes.

The API always answers HTTP 200; the real result is the "responseCode" field in the body.
"""

GET_USER_DETAIL_BY_EMAIL = "/api/getUserDetailByEmail"
CREATE_ACCOUNT = "/api/createAccount"
DELETE_ACCOUNT = "/api/deleteAccount"

RESPONSE_OK = 200
RESPONSE_CREATED = 201
RESPONSE_NOT_FOUND = 404
