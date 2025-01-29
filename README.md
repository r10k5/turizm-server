## Системные требования

- Python 3.10
- Docker
- Docker Compose

## Установка и запуск

1. Клонируйте репозиторий
2. Выполните команду `docker compose up -d`
3. Выполните команду `python manage.py migrate`
4. Выполните команду `python manage.py loaddata users.json`
5. Выполните команду `python manage.py runserver`

## Логин и пароль

### Администратор
- Логин: `admin`
- Пароль: `12345678`

### Туроператор
- Логин: `tour_operator`
- Пароль: `12345678`

### Менеджер
- Логин: `manager`
- Пароль: `12345678`