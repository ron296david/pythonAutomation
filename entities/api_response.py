from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ApiResponse:
    http_status: int
    body: dict[str, Any]
