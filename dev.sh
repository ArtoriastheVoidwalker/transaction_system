#!/bin/bash

# ./env/bin/uvicorn app:app --port 8000 --timeout-keep-alive 10000 --env-file dev.env
./venv/bin/uvicorn --reload app.main:app --port 8001 --timeout-keep-alive 10000
# ./env/bin/gunicorn -k uvicorn.workers.UvicornWorker app.main:app -b :8000 --timeout 10000
