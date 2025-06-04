Настройка:
```
В корне проекта(директория "core") рядом с manage.py вам нужно будет создать .env,
где нужно указать настрйки вашей BD(postgres).Пример этих настроек есть в файле .env.example,
вам нужно будет указать DB_NAME, DB_USER и DB_PASSWORD
```
Команды для запуска проекта:
```
cd .\core\
docker build -t cattask .
docker run -p 8000:8000 cattask
```
Коллекция для postman находится в файле "TaskCat.postman_collection.json"