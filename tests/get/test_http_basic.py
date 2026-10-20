from httpbin_api_client import get_endpoint
import allure

@allure.title("Проверка статус кода для /get")
def test_get_status_code():
    resp = get_endpoint("get")
    assert resp.status_code == 200

@allure.title('Проверка Content-Type = "application/json" для /get')
def test_content_type_header():
    resp = get_endpoint("get")
    assert resp.headers["Content-Type"].startswith("application/json")
