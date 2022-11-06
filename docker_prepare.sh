#!/bin/bash


docker build -f develop.dockerfile
createdb transaction_system
cp dev.env .env
echo "Successful prepared docker image"