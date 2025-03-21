FROM python:3.12.3-slim-bookworm

ENV PYTHONBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip 'poetry==2.1.1'

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY myplatform .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "myplatform.uwsgi:application", "-b", "0.0.0.0:8000"]