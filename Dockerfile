FROM python:3.10

WORKDIR /code

EXPOSE 8000

COPY ./requirements.txt /code/

RUN pip install -r requirements.txt

COPY . .

# Загрузите переменные окружения из файла .env
RUN pip install python-dotenv

COPY .env /code/

CMD ["sh", "-c", "python manage.py migrate"]
