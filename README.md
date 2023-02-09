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
* запуск сервера `uvicorn main:app`
* запуск сервера с автоматическим рестартом `uvicorn main:app --reload`
* инициализируем Alembic в проекте `alembic init --template async alembic`
* создание файла миграции `alembic revision --autogenerate -m "migration name"`
* применение миграций `alembic upgrade head`
* отмена миграций `alembic downgrade`
* запуск тестов `pytest`


## Шаблон наполнения .env файла

```
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
FIRST_SUPERUSER_EMAIL=admin@ad.ru
FIRST_SUPERUSER_PASSWORD=111111
TYPE=service_account
PROJECT_ID=mystic-span-375418
PRIVATE_KEY_ID=41c11b704ba84e7ffe65eb71b2576175cc4a4f66
PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDB0nDd4AsACMZK\n/BLlykDGpoPfl9H8aN8sAJjViUGH1kXBRF2DTtK0B+8vPMDiTLkx6DHkHomfwgVf\nhVAy7GhXK2jhSMcE7CXTX1Up7oNPR4m4g57uRhlNiH8Wo4THGJMxtTePeRSiPhph\n8t2F1y0l2OLfIDaWmK7tEElFlZkPMj8txNOqVSpdnzK0hOiOerWI07HO01rRoxHY\nia3JfqLT9/vghCwpofi7kUI256oMhjM3ImZj3V092KH92T/QM+264F5oyFcooAUY\nPwHHWrvuVgtymeRQw9F5hd+AIoTHADG/wyrzLDbfh6K/ju5v+ZVCWHUA5Es5n1Xh\nY2k73/X1AgMBAAECggEAMCx+8xa5hTOpHYATrlubyAQhKNTSU1s5hPVNB14LFJkU\nU1oLqBRSWH7UWzhNdLG/IgFlTR6t9DBEJ5659T4/HNNkSQJOvRF4wVWjlD19E5pj\nR6InQW/Y4CV5+QWBff7ErwksmxNsJnsrEYdMufRme06x7OVTzBB9Ad0XaR0qotTa\nlWxriL6zoy4/dz+BXzoVIi8bt1YQcbvDfZX8b5nz8TPTKcQB02L8uAV9wk3IWnrS\nXQwl6ZzVphjNvwHysDQTbB89k8TL3HPp+Lr/P3qrB4zGpJJMeELnakB+bA81QW9C\nFEELZtxZ7/x68V6P/GLcTWyPtaDA9oFdFKV1hihCbQKBgQDgbBbu5hLMTfizbuHg\nNhmY00AMepo+sij5SVFdvwnNl+QjXldGvCrljcNeqm2nReaH3Mnoz7bYDF1AZost\nBqfUtaZacZcHChY6U5feQekRNc4PIqrLY4dBCubH0Y9GvOp7eVvPhlAzFxNoL2KE\neloLSU3OthHiUAbYga8wjFYSvwKBgQDdGBoppdhHDfh2Wmn9MOSukQRpHRAcJFBx\n1lf69dCjVWJXkGlYyyLdwnm7gdwVubPJ2CEnmXtyNZOmPfauR8BgHfgXT990Fu9n\n51K6T127F/Zrd4oe39MpRN15la/HIwSq63/tRbrrdwGoyGHT0vi3l56VWOl4yB18\nckmlzw2ISwKBgQCJRbR1ZqfC7kKcxstFEPJxR25a87dbeDCV4yHw/MSrTChQ9gje\njISUqzUAt7Cg66HKIuQiEsPdvRphJRgmb3bDJmVd1zMxLBtSjAVN/vToAQhMu8DK\n7dMyls95FBbWhwHKiv38n0R5K7lENg/Fxu1DEBCWy0l/K8I0NocJZB3WEwKBgG86\nEt9k6ZtFcfvInI2drU4M8pUW4+XkdvvuAzDjvWSOLf0zT2w2NYIutiMYv2nGlKY0\nrulHE41vWqpFffZLboJsUUUZD6dNan9xJnNIPjVDZtrFtpy1qXuXg3wJS/b4rP53\nn1H0xIZ0xkbtGBoChtGF22fy5PG4au0Sae6abYplAoGBAKHZdEZkhZeZK82z3cZa\nlnaHwbWieQZnXuOIncoYloiIUqtRodss9/YuVdi20SjLQMFAfqHZq65iGnnHLn3L\nHXZ/5Et6qHWcs9S9dcFbaRp55SmEV0wGK9Vf/U6wuZpiS0JkSQP5WdbvttsDa+ct\n9yiDRUe3BI1vfLihqcrgIG5d\n-----END PRIVATE KEY-----\n
CLIENT_EMAIL=foxygen@mystic-span-375418.iam.gserviceaccount.com
CLIENT_ID=101121506231304671504
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/foxygen%40mystic-span-375418.iam.gserviceaccount.com
EMAIL=your_gmail@gmail.com
```


## Системные требования

* Python 3.7
* FastAPI 0.7.0
* Works on Linux, Windows, macOS