# Currenct Converter REST API

Данный REST API, содержит один эндпоинт, который предназанчен для конвертации валют.

Swagger - http://0.0.0.0:8000/docs
<details>
<summary>ТЗ проекта ↓</summary>
Задание:
Написать сервис "Конвертер валют" который работает по REST-API.
Пример запроса:
GET /api/rates?from=USD&to=RUB&value=1
Ответ:
{

"result": 62.16

}
Любой фреймворк в пределах python.
Данные о текущих курсах валют необходимо получать с внешнего сервиса.
Контейнерезация, документация, и прочее — приветствуется.
</details>

## Используемые технологии
<a name="технологии"></a>

![AppVeyor](https://img.shields.io/badge/Python-3.10.6-green)
![AppVeyor](https://img.shields.io/badge/fastapi-0.103.1-9cf)
![AppVeyor](https://img.shields.io/badge/httpx-0.25.0-9cf)
![AppVeyor](https://img.shields.io/badge/pydantic-2.3.0-9cf)
![AppVeyor](https://img.shields.io/badge/pytest_asyncio-0.21.1-9cf)
![AppVeyor](https://img.shields.io/badge/python_dotenv-1.0.0-9cf)
![AppVeyor](https://img.shields.io/badge/uvicorn-0.23.2-9cf)

![AppVeyor](https://img.shields.io/badge/Docker-24.0.5-green)

![AppVeyor](https://img.shields.io/badge/Poetry-1.5.1-green)

## Запуск

### Локально
1. Клонируем репозиторий:
   ```bash
   git clone https://github.com/Timoha23/currency_converter_api.git
   ```
2. Переходим в директорию backend/:
    ```bash
    cd backend/
    ```
3. В директории backend/ создаем .env файл и заполняем в соответствии с примером (.env.example).
4. Устанавливаем зависимости:
    ```bash
    poetry install
    ```
5. Запускаем REST API сервис:
   ```bash
   python main.py
   ```

###  Докер
1. Клонируем репозиторий:
   ```bash
   git clone https://github.com/Timoha23/currency_converter_api.git
   ```
2. Переходим в директорию backend/:
    ```bash
    cd backend/
    ```
2. Создаем .env файл и заполняем в соответствии с примером (.env.example).
3. Собираем Docker-образ:
   ```bash
   docker build -t backend .
   ```
4. Запускаем контейнер из образа:
   ```bash
   docker run -p 8000:8000 backend
   ```

## Примеры запросов к API

1. Получение товаров из базы данных
   * Endpoint: **host:port/api/rates/**
   * Method: **GET**
   * Params:
    * Query:
      ```json
      {
        "from": "USD",
        "to": "RUB",
        "amount": 10,
      }
      ```
   * Response:
      ```json
      {
        "result": 963.89029
      }
      ``` 
   * Postman
      <details>
     <summary>Спойлер</summary>
      
     [![Пример запроса][1]][1]
      
     [1]: https://imageup.ru/img133/4525637/1.png
     </details>

### Используемые API
---
- Конвертер валют - https://api.apilayer.com
