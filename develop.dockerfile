ENV PYTHONPATH=/app

WORKDIR /app/

COPY requirements.txt /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000
EXPOSE 5432

CMD ["/bin/bash", "-c", "./scripts.sh kube_prepare_db && uvicorn app.main:app --host 0.0.0.0 --port 8000"]