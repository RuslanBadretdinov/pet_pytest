import requests
from typing import Any, Dict

BASE_URL = "https://httpbin.org"

def get_endpoint(
    endpoint: str,
    params: Dict[str, Any] | None = None,
    headers: Dict[str, str] | None = None
) -> requests.Response:
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, params=params, headers=headers, timeout=10)
    return response
