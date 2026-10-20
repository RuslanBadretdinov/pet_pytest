from httpbin_api_client import get_endpoint

def test_response_structure():
    resp = get_endpoint("get")
    data = resp.json()

    # Проверяем обязательные поля
    assert "args" in data
    assert "headers" in data
    assert "origin" in data
    assert "url" in data

    # Проверяем типы
    assert isinstance(data["args"], dict)
    assert isinstance(data["headers"], dict)
    assert isinstance(data["origin"], str)
    assert isinstance(data["url"], str)

def test_headers_contain_accept():
    custom_headers = {"Accept": "application/json"}
    resp = get_endpoint("get", headers=custom_headers)
    data = resp.json()

    headers = data["headers"]
    assert headers.get("Accept") == "application/json"
