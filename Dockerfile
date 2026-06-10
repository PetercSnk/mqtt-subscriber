FROM python:3.12-slim-bookworm

WORKDIR /subscribe-app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--config", "gunicorn.py", "--log-config", "logging.conf", "app:createApp()"]