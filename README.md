# Запись студентов на дипломы

 - [x] Получение темы в форме в зависимости от руководителя
 - [x] Функционал резервирования тем
 - [x] Экспорт записей в CSV
 - [x] Архив записей

# TODO:
Пока ничего

# Инструкция
Приложение хранит параметры SECRET_KEY и DEBUG_DJANGO в системных переменных:
- DJANGO_SECRET_KEY - секретный ключ Django
- DEBUG_DJANGO - состояние дебага приложения

Генератор секретных ключей: [https://djecrety.ir/](https://djecrety.ir/)

# Настройка бд:
В settings.py прописать настройки для POSTGRES
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'RaspredImfiit',
'USER': '',
'PASSWORD': '',
'HOST': 'localhost',
'PORT': '', <!--- По дефолту 5432 -->

# Дополнительная настройка на проде
https://learndjango.com/tutorials/django-static-files-and-templates

# Используемый стек
1. Django [https://www.djangoproject.com/](https://www.djangoproject.com/)
	1. Django 4.1.7
	2. Django smart selects 1.6.0 [https://github.com/jazzband/django-smart-selects](https://github.com/jazzband/django-smart-selects)
2. Chota CSS [https://jenil.github.io/chota/](https://jenil.github.io/chota/)
3. PostgreSQL [https://www.postgresql.org/](https://www.postgresql.org/)
