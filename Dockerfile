FROM python:3

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install -r requirements.txt

COPY . .

# Загрузите переменные окружения из файла .env
RUN ["python", "-c", "from dotenv import load_dotenv; load_dotenv()"]

CMD ["python", "manage.py", "runserver"]
