#! /usr/bin/env bash
set -e

celery -A app.worker worker -B -Q queue -f celery.logs