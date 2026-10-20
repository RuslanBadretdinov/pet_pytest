#!/usr/bin/env bash
set -e

pytest --alluredir=allure-results --clean-alluredir -v
allure generate allure-results --clean -o allure-report

echo "Отчёт: file://$(pwd)/allure-report/index.html"
