#!/bin/bash


python3 -m venv env
./venv/bin/pip3 install --upgrade pip
./venv/bin/pip3 install -r requirements.txt
cp dev.env .env
cp -rf default_storage/. storage
createdb transaction_system
./venv/bin/alembic upgrade head
./scripts/prepare_db.sh
echo "Successful prepared app"
