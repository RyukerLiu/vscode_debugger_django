FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /code


RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

RUN pip install --upgrade pip 

COPY Pipfile .
RUN pip install pipenv
RUN pipenv install --skip-lock --system

COPY . .

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
