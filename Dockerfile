FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./ecomtoday ./ecomtoday

CMD ["python3", "./ecomtoday/manage.py", "runserver", "127.0.0.1:8000"]