FROM python:3.6-alpine

RUN pip install flask

COPY . /app
WORKDIR /app

CMD ["python", "app.py"]
