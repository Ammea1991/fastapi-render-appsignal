FROM python:3.11-slim

WORKDIR /app
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
