import allure
import pytest

@pytest.fixture(autouse=True)
def common_allure_labels():
    allure.dynamic.suite("API (FEATURE)")
    allure.dynamic.story("Общие проверки API (STORY)")
