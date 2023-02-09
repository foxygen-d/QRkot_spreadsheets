![repo size](https://img.shields.io/github/repo-size/foxygen-d/QRkot_spreadsheets)
![py version](https://img.shields.io/pypi/pyversions/3)


# Отчёт в Google Sheets для QRKot


![alt text](https://pictures.s3.yandex.net/resources/140_1656321007.png)


## Описание проекта

Проект расширяет возможности приложения QRKot и формирует отчёт в гугл-таблице

В таблице отображаются закрытые проекты, отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму



## Инструкция по развёртыванию проекта

* клонировать проект на компьютер `git clone https://github.com/foxygen-d/QRkot_spreadsheets.git`
* создание виртуального окружения `python3 -m venv venv`
* запуск виртуального окружения `. venv/bin/activate`
* установить зависимости из файла requirements.txt `pip install -r requirements.txt`
<!-- * запуск сервера `uvicorn main:app`
* запуск сервера с автоматическим рестартом `uvicorn main:app --reload`
* инициализируем Alembic в проекте `alembic init --template async alembic`
* создание файла миграции `alembic revision --autogenerate -m "migration name"`
* применение миграций `alembic upgrade head`
* отмена миграций `alembic downgrade` -->
* запуск тестов `pytest`


## Системные требования

* Python 3.7
* FastAPI 0.7.0
* Works on Linux, Windows, macOS