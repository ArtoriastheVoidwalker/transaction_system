#!/bin/bash

set -e
set -x

./venv/bin/alembic revision -m "$1"