from httpbin_api_client import get_endpoint

def test_get_status_code():
    resp = get_endpoint("get")
    assert resp.status_code == 200

def test_content_type_header():
    resp = get_endpoint("get")
    assert resp.headers["Content-Type"].startswith("application/json")

def test_url_in_response():
    resp = get_endpoint("get")
    data = resp.json()
    assert data["url"].endswith("/get")
