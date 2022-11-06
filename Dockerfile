FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN apt-get update && apt-get install vim python3-celery tzdata -y && rm -rf /var/lib/apt/lists/*

ENV PYTHONPATH=/app
ENV TZ=Asia/Bishkek
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 8000

WORKDIR /app/

COPY requirements.txt /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app