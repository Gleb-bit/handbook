# handbook

Сервис терминологии и REST API к нему

# Запуск с использованием Docker:

## Создание контейнера docker:

* ```docker build -t container_name .```

## Поднятие контейнера docker:

* ```docker-compose up -d```

# Запуск на локальной машине:

## Установка сторонних зависимостей:

* ```pip install -r requirements.txt```

## Создание миграций:

* ```python manage.py makemigrations```

## Применение миграций:

* ```python manage.py migrate```

## Запуск сервера:

* ```python manage.py runserver```

# Использование:

* ### Административная панель находится по адресу admin/
* ### API находится по адресу api/
* ### Описание API находится по адресу swagger/