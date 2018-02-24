FROM python:3.6.3

MAINTAINER contato.juanmagalhaes@gmail.com

ENV PYTHONUNBUFFERED 1
WORKDIR /src
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install --system
COPY . ./
CMD ["gunicorn", "core.wsgi", "-b", "0.0.0.0:8000"]
EXPOSE 8000
