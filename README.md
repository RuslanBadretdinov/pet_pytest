# pet_pytest

Учебный проект на Python + pytest для тестирования HTTP API (httpbin.org).  
Проект демонстрирует структуру реального проекта, параметризацию тестов и генерацию профессиональных отчётов (Allure).

## Цели проекта

- Показать понимание структуры Python‑проекта (src, tests, conftest).
- Продемонстрировать навыки написания автотестов на pytest.
- Проверить HTTP‑аспекты: статус‑коды, заголовки, валидацию JSON.
- Научиться генерировать и читать отчёты Allure.
- Понять, как тесты интегрируются в CI (JUnit XML, покрытие кода).

## Стек

- Python 3.14
- pytest 9.1.1
- requests 2.32.3
- allure-pytest 3.3.0
- Allure CommandLine 2.23.0 (Java‑based)

## Как запустить

### 1. Создать и активировать виртуальное окружение


```bash
python -m venv .venv
source .venv/bin/activate

### 2. Установить зависимости
bash

pip install -r requirements.txt

### 3. Запустить тесты и собрать Allure‑отчёт
bash

pytest --alluredir=allure-results --clean-alluredir -v
allure generate allure-results --clean -o allure-report

### 4. Открыть отчёт

Открой в браузере файл ():
../pet_pytest/allure-report/index.html


### Запуск через bash script
chmod +x run_tests.sh
./run_tests.sh