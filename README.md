# UI Автотесты для SauceDemo

Репозиторий содержит end-to-end UI автотесты для [SauceDemo](https://www.saucedemo.com/) с использованием Playwright, pytest и Allure, построенные по паттерну Page Object Model (POM).

## Содержание

* [Возможности](#возможности)
* [Структура проекта](#структура-проекта)
* [Требования](#требования)
* [Настройка окружения](#настройка-окружения)
* [Установка](#установка)
* [Запуск тестов локально](#запуск-тестов-локально)
* [Генерация отчётов Allure](#генерация-отчётов-allure)
* [Интеграция с Jenkins](#интеграция-с-jenkins)
* [Настройка параметров запуска](#настройка-параметров-запуска)
* [Логирование](#логирование)
* [Контакты](#контакты)

## Возможности

* Автотесты на Python + Playwright (sync API)
* Page Object Model для читаемости и поддержки
* Конфигурация через файл `.env`
* Логирование в консоль и в файл с ротацией
* Интеграция с Allure для богатых HTML-отчётов
* Конвейер Jenkins с Docker-агентом
* Скриншоты при падении тестов

## Структура проекта

```
├── .env                   # переменные окружения (URL, ENV, креды)
├── .gitignore
├── Jenkinsfile            # описание pipeline Jenkins
├── requirements.txt       # зависимости Python
├── pytest.ini             # конфигурация pytest (марки, логирование, Allure)
├── playwright.config.py   # настройки Playwright
├── conftest.py            # фикстуры и хуки pytest (Playwright, скриншоты)
├── src/
│   ├── config/
│   │   └── environment.py # загрузка .env
│   ├── auth/
│   │   └── auth_config.py # загрузка логина/пароля
│   ├── utils/
│   │   ├── logger.py      # настройка логгера
│   │   └── assertions.py  # кастомные проверки
│   └── pages/
│       ├── base_page.py
│       ├── login_page.py
│       ├── all_products_page.py
│       ├── product_page.py
│       └── cart_page.py
├── locators/
│   ├── auth_locators.py
│   ├── all_products_locators.py
│   ├── product_locators.py
│   └── cart_locators.py
├── data/
│   └── users.json         # тестовые данные (необязательно)
├── tests/
│   ├── test_login.py
│   ├── test_all_products.py
│   ├── test_product.py
│   └── test_cart.py
├── reports/
│   └── allure-results/    # сырые данные Allure
└── logs/
    └── test_run.log       # ротационный лог-файл
```

## Требования

* Python 3.8+
* pip
* Node.js (для Playwright)
* Allure Command-Line (для локальной генерации отчётов)

## Настройка окружения

1. Создайте файл `.env` в корне проекта:

   ```ini
   TEST_URL=https://www.saucedemo.com/
   ENV=test
   TEST_AUTH_LOGIN=standard_user
   TEST_AUTH_PASSWORD=secret_sauce
   LOG_LEVEL=INFO       # опционально
   LOG_DIR=logs         # опционально
   ```
2. Классы `Environment` и `AuthConfig` загрузят значения автоматически.

## Установка

```bash
git clone <repo_url>
cd saucedemo-ui-tests
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 -m playwright install
```

## Запуск тестов локально

```bash
# Все тесты
pytest

# С параметрами
pytest --browser=chrome --h=False --slow=200
```

## Генерация отчётов Allure

```bash
# Сбор результатов
pytest --alluredir=allure-results

# Интерактивный просмотр
allure serve allure-results

# Статический отчёт
allure generate allure-results -o allure-report
allure open allure-report
```

## Интеграция с Jenkins

* Используется официальный Docker-агент Playwright
* Параметры: ENV, BROWSER, HEADLESS, SLOW
* Credentials Binding для логина/пароля
* Шаги: подготовка `.env`, установка зависимостей, запуск тестов
* Post: поправка прав, публикация отчёта Allure

## Настройка параметров запуска

* **BROWSER**: `chrome` или `firefox`
* **HEADLESS** (`--h`): `True` / `False`
* **SLOW**: задержка в ms для `slow_mo`
* **ENV**: окружение из `.env` или Jenkins-параметра

## Логирование

* Консоль и файл `logs/test_run.log`
* Конфиг в `src/utils/logger.py` с ротацией файлов

## Контакты

По вопросам и предложениям обращайтесь к QA-команде.
