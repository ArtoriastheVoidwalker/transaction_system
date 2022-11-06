FROM python:3.8.6-slim-buster

WORKDIR /app/

RUN apt-get update && apt-get install vim curl -y && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

ENV PYTHONPATH=/app

EXPOSE 8000

COPY requirements.txt /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app
COPY scripts/worker_start.sh /worker-start.sh

CMD ["bash", "/worker-start.sh"]
