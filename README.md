GEO Django Project

📌О проекте

GEO Django Project - это веб-приложение на Django с использованием Django REST Framework (DRF), PostgreSQL, Docker и GeoDjango.

📦 Стек технологий

Backend: Django, Django REST Framework (DRF)

База данных: PostgreSQL

Аутентификация: JWT (djangorestframework-simplejwt)

Контейнеризация: Docker, Docker Compose


🚀 Установка и запуск

git clone <repo-url>
cd geo_django_project/src

🔹 Настройка окружения

Создай файл .env в корне проекта и добавь в него:

DJANGO_SETTINGS_MODULE= core.settings.base
DEBUG=True
POSTGRES_DB=geodb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432


🔹 Запуск в Docker

docker-compose up --build -d

Перед запуском приложения базу непосредственно нужно создать в самом докере командой 

docker exec -it src-db-1 psql -U postgres

если выходит ошибка используем 

\c template1

обновляем версию 
ALTER DATABASE template1 REFRESH COLLATION VERSION;

Создаем базу
create database geodb;

После успешного запуска, API будет доступно по адресу:📌 http://localhost/swagger/ - Swagger UI


🔑 Аутентификация
# Для большинства эндпоинтов стоит разрешение только для чтения если хотим использовать post put delete нужно авторизоваться 

для начала нужно добавить пользователя в базу можно это сделать таким способом

заходим в контейнер src-web-1
docker exec -it src-web-1 python manage.py shell

и просто копируем эту команду 

from django.contrib.auth.models import User
user = User.objects.create_user(username='ahmed2025', password='ahmed2025')
user.is_active = True
user.save()
print("Пользователь создан:", user.username)


можно сделать через swagger по пути 
/token/

{
  "username": "ahmed2025",
  "password": "ahmed2025"
}


📜 API Эндпоинты

GET /api/v1/categories/ - Получение категорий
GET /api/v1/locations/ - Получение локаций
GET /api/v1/places/ - Получение мест
GET /api/v1/reviews/ - Получение отзывов
POST /api/token/ - Получение JWT-токена

🧪 Тестирование

На данный момент тесты реализованы только для категорий и локаций. Можно добавить тестирование для places и reviews.


📌 Дополнительные улучшения

я не до конца провел тесты поэтому можно будет в будущем покрыть тестами оставшиеся 
Реализация тестирования для places и reviews


и добавить базовое логирование на эндпоинты
Добавление логирования через logging и отправка логов через Filebeat на сервер ELC



