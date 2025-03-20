
# SkyTest

SkyTest – это Django-проект, демонстрирующий базовую функциональность для работы с товарами, заказами и пользователями. 
Проект упакован в Docker и использует PostgreSQL, Gunicorn, Whitenoise для раздачи статических файлов,
а также автоматическое создание суперпользователя и заполнение базы начальными данными.

## Структура проекта

```
skytest/
├── Dockerfile
├── compose.yml          # Docker Compose файл
├── .env                 # Файл с переменными окружения (не включается в репозиторий)
├── manage.py
├── requirements.txt     # Зависимости проекта
├── entrypoint.sh        # Скрипт для применения миграций, сборки статики, загрузки фикстур и создания суперпользователя
├── skytest/             # Django-проект (settings.py, urls.py, wsgi.py, etc.)
├── products/            # Приложение для работы с товарами
└── users/               # Приложение для управления пользователями и авторизации
```


## Настройка окружения

1. **Клонирование репозитория:**

   ```bash
   git clone https://github.com/sounditbox/skytest.git
   cd skytest
   ```

2. **Создание файла переменных окружения (.env):**

   Создайте файл `.env` в корневой папке проекта (его не должно быть в репозитории). Пример содержимого:

   ```env
   # PostgreSQL
   POSTGRES_DB=shopdb
   POSTGRES_USER=shopuser
   POSTGRES_PASSWORD=shoppass
   POSTGRES_HOST=db
   POSTGRES_PORT=5432

   # Django
   DEBUG=0
   SECRET_KEY=your-secret-key

   # Суперпользователь Django
   DJANGO_SUPERUSER_USERNAME=admin
   DJANGO_SUPERUSER_PASSWORD=admin
   DJANGO_SUPERUSER_EMAIL=admin@example.com
   ```

## Запуск проекта

Проект упакован в Docker. Для запуска используйте:

```bash
docker compose up --build
```

Контейнер `web`:
- Автоматически применяет миграции.
- Собирает статические файлы (включая статику админки) через Whitenoise.
- Загружает фикстуру `dummy_data.json`.
- Создаёт суперпользователя.
- Запускает приложение через Gunicorn (WSGI).

Контейнер `db` использует официальный образ PostgreSQL и хранит данные в volume.


## Dockerfile и entrypoint

Проект использует entrypoint-скрипт (`entrypoint.sh`), который выполняет следующие действия при старте контейнера:
- Применение миграций
- Сбор статики
- Загрузка фикстур
- Создание суперпользователя
- Запуск Gunicorn
