FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY diploma-frontend/frontend/static ./static
COPY diploma-frontend-0.6.tar.gz diploma-frontend-0.6.tar.gz
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY megano .

CMD ["gunicorn","megano.wsgi:application", "--bind", "0.0.0.0:8000"]
