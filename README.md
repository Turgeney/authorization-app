# authorization-app

Приложение-сервис авторизации, осуществляет:
* регистрацию пользователей
* хранение паролей и других учётных данных
* проверку учётных данных
* выдачу и проверку access JWT-токенов
Имеет вспомогательный веб-интерфейс.

Используются:
 - Python
 - Poetry
 - FastAPI
 - Uvicorn
 - sqlalchemy
 - pydantic
 - jinjatemplates

В файле settings.py хранятся основные настройки приложения.

# Запуск приложения

1. Выполнить при необходимости установку python и poetry

2. Восстановить зависимости:

```bash
poetry install
```

3. Запуск приложения из корневой папки:

```bash
poetry run uvicorn app.main:app --reload
```