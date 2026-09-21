"""Web access layer: the only layer that sends API requests (through Playwright)."""

from playwright.sync_api import APIRequestContext, APIResponse

from entities.api_response import ApiResponse


class ApiActions:
    def __init__(self, request: APIRequestContext):
        self._request = request

    def get(self, path: str, params: dict[str, str]) -> ApiResponse:
        return self._to_response(self._request.get(path, params=params))

    def post(self, path: str, form: dict[str, str]) -> ApiResponse:
        return self._to_response(self._request.post(path, form=form))

    def delete(self, path: str, form: dict[str, str]) -> ApiResponse:
        return self._to_response(self._request.delete(path, form=form))

    @staticmethod
    def _to_response(response: APIResponse) -> ApiResponse:
        return ApiResponse(http_status=response.status, body=response.json())
