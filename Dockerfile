FROM python:alpine

WORKDIR /usr/src/app

COPY /requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

RUN python manage.py makemigrations && python manage.py migrate
