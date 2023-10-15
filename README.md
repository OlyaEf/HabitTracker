# Проект HabitTracker

HabitTracker - это веб-приложение для отслеживания и управления своими привычками.

## Установка и Запуск Проекта

Чтобы установить и запустить проект HabitTracker, выполните следующие шаги:

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/OlyaEf/HabitTracker.git
   
Создайте и активируйте виртуальное окружение:
bash
Copy code
cd habit-tracker
python -m venv venv
source venv/bin/activate  # На Linux / macOS
venv\Scripts\activate  # На Windows

Установите зависимости проекта:
bash
Copy code
pip install -r requirements.txt

Примените миграции для создания базы данных:
bash
Copy code
python manage.py migrate

Создайте суперпользователя для доступа к админ-панели:
bash
Copy code
python manage.py csu

Запустите сервер разработки Django:
bash
Copy code
python manage.py runserver
Откройте приложение в вашем веб-браузере по адресу http://127.0.0.1:8000/

Используемые Технологии
Django - фреймворк для веб-разработки.
Django REST framework - фреймворк для создания API.
PostgreSQL - система управления реляционными базами данных.

Дополнительная Информация
Если у вас есть вопросы или возникли проблемы с проектом, не стесняйтесь обращаться к автору проекта или искать помощь в сообществе Django.

Счастливого кодирования!

