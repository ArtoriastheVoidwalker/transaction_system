#!/bin/bash

set -e
set -x

./venv/bin/alembic revision --autogenerate -m "$1"