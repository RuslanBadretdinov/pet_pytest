import allure
import pytest


@pytest.fixture(autouse=True)
def get_specific_labels():
    allure.dynamic.suite("API для GET (FEATURE)")
    allure.dynamic.story("Общие проверки API GET (STORY)")
