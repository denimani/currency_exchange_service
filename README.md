## Джанго-приложение "Служба обмена валют"

___

Проект реализует сервис для отслеживания курсов валют с использованием фреймворка Django. Основной функционал включает в
себя:
1. Создание базы данных в Postgres с таблицей currency, содержащей информацию о курсах валют.
2. Консольная команда для обновления данных в таблице currency с использованием данных с сайта Центрального банка России.
3. Реализация двух REST API методов:
   * GET `/currencies` для получения списка курсов валют с возможностью пагинации.
   * GET `/currency/` для получения курса валюты по переданному идентификатору.
4. Защита API авторизацией по токену Bearer.
5. Покрытие всех компонентов приложения юнит-тестами.

### Технологии

* [Django](https://www.djangoproject.com/)
* [Python](https://www.python.org/)
* [PostgreSQL](https://www.postgresql.org/)

### Инструкция по запуску приложения:

_Для запуска проекта необходимо клонировать репозиторий, создать и активировать виртуальное окружение:_

```
python3 -m venv venv - установка виртуального окружения

venv/Scripts/activate - активация виртуального окружения
```

_Установить необходимые зависимости:_

```
pip install -r requirements.txt
```

_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample:_

```
SECRET_KEY=

# настройка базы данных
POSTGRES_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```

_Выполнить миграции:_

```
python3 manage.py migrate
```

_Создать суперпользователя:_

```
python3 manage.py createsuperuser
```

_Запуск приложения:_

```
python3 manage.py runserver
```

_Для запуска приложения:_

```
python3 manage.py runserver
```

_Для тестирования проекта запустить команду:_

```
python3 manage.py test
```

### API-документация проекта: http://{HOST}:{PORT}/swagger/

### Аутентификация

API эндпоинты защищены аутентификацией. Вы можете использовать токены аутентификации для доступа к защищенным
эндпоинтам. Чтобы получить токен, выполните POST-запрос на token/ с параметрами username и password. Полученный
токен должен быть передан в заголовке Authorization для доступа к защищенным ресурсам.

### Автор

* **Исхаков Денис** - [Iskhakov Denis](https://github.com/denimani)
