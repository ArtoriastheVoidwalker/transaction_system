#!/bin/bash


docker run -d --net=host --platform linux/amd64 -p 8001:8001 --env-file .env my_doctor-backend:latest