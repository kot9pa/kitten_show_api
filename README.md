# Сборка приложения
1. Клонировать репозиторий и перейти в корень приложения
2. Запустить сборку образа приложения:  
`docker build -t app_kitten_show .`  
3. Запустить контейнеры БД и приложения (веб-сервер)  
`docker compose up -d`

# REST API
Web-server по адресу http://localhost:8080  
Swagger UI http://localhost:8080/docs  

1. Получение списка пород (breeds)  
`GET localhost:8080/api/v1/breeds`

Пример Response:  
`{
    "title": "Абиссинская",
    "id": 1
}`

Таблица breeds содержит список пород, загруженных через миграцию Alembic  
`migration\versions\2024-10-04_initial_revision.py`

2. Получение списка всех котят (kittens)  
`GET localhost:8080/api/v1/kittens`

3. Получение списка котят определенной породы по фильтру  
`GET localhost:8080/api/v1/kittens/by_breed/{id}`

Пример: `GET localhost:8080/api/v1/kittens/by_breed/1`

4. Получение подробной информации о котенке  
`GET localhost:8080/api/v1/kittens/{id}`

Пример: `GET localhost:8080/api/v1/kittens/1`

5. Добавление информации о котенке  
`POST localhost:8080/api/v1/kittens`

Пример Body:  
`{
    "name": "Kitten name 1",
    "age": 1,
    "color": "Kitten color 1",
    "breed_id": 1,
    "description": "Kitten description 1"
}`

6. Изменение информации о котенке (полное и частичное)  
`PUT localhost:8080/api/v1/kittens/{id}`  
`PATCH localhost:8080/api/v1/kittens/{id}`

Пример: `PATCH localhost:8080/api/v1/kittens/1`

Пример Body:  
`{
    "name": "My updated Kitten name 1",
    "age": 2,
    "color": "My updated Kitten color 1",
    "breed_id": 1,
    "description": "My updated Kitten description 1"
}`

7. Удаление информации о котенке (всех или по Id)  
`DELETE localhost:8080/api/v1/kittens/`  
`DELETE localhost:8080/api/v1/kittens/{id}`

Пример: `DELETE localhost:8080/api/v1/kittens/1`
