# Курс 6. Курсовая работа

Данная курсовая работа представляет собой backend-часть для сайта объявлений. 

Бэкенд-часть проекта предполагает реализацию следующего функционала:
1. Авторизация и аутентификация пользователей.
2. Распределение ролей между пользователями (пользователь и админ).
3. Восстановление пароля через электронную почту (не обязательно).
4. CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
5. Под каждым объявлением пользователи могут оставлять отзывы.
6. В заголовке сайта можно осуществлять поиск объявлений по названию.

## Стек:
    Python 3, Django, Django REST Framework, PostgreSQL

## Подготовка к запуску

1. Скачать репозиторий.
2. Создать в корневой директории проекта файл .env. Указать в нем значения переменных окружения:
    - DB_ENGINE=django.db.backends.postgresql
    - DB_NAME=...
    - DB_USER=...
    - DB_PASSWORD=...
    - DB_HOST=...
    - DB_PORT=...
    - EMAIL_HOST=...
    - EMAIL_HOST_USER=...
    - EMAIL_HOST_PASSWORD=...
    - EMAIL_PORT=...
3. Произвести развертывание fronend и PostgreSQL с помощью Docker compose. (docker compose up -d)
4. Запустить backend сервер.
