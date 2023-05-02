# Ваш собственный путеводитель в мире рецептов Foodoo shop

## Описание сервиса

Наш проект позволяет делиться рецептами и создавать списки продуктов.

## Установка сервиса

* backend - образ бэкенда
* frontend - образ фронтенда
* postgres - образ базы данных PostgreSQL v 12.04
* nginx-proxy - образ веб-сервера nginx
* openssl - образ openssl для генерации сертификатов


## Запуск проекта:
 * Установите Докер
 * Перейдите в папку в проекте infra/
 * Выполните команду:

```
docker-compose up -d --build
```

## Создание суперпользователя:
```bash
- sudo docker-compose exec backend python manage.py createsuperuser
```

## CI/CD
Настроены pipelines для автоматической сборки и публикации образов frontend и backend
* frontend: https://hub.docker.com/repository/docker/maxbstr/foodgram_frontend/general
* backend: https://hub.docker.com/repository/docker/maxbstr/foodgram_backend/general
