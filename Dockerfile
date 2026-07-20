FROM python:latest

EXPOSE 8000
WORKDIR /usr/src/app

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
