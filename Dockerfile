FROM python:3.6.3
ENV PYTHONUNBUFFERED 1
WORKDIR /src
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "core.wsgi", "-b", "0.0.0.0:8000"]
EXPOSE 8000
