#!/bin/env bash

PORT = ${PORT:-8080}
gunicorn -b 0.0.0.0:$PORT web:app &
python3 main.py