#!/bin/bash
#This is a startup script (Bash) that runs your FastAPI app in production with Gunicorn + Uvicorn.
source /opt/venv/bin/activate #Activates the Python virtual environment located at /opt/venv.

cd /code
RUN_PORT=${PORT:-8000}
RUN_HOST=${HOST:-0.0.0.0}

gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT main:app 
#gunicorn → A robust Python WSGI server (handles multiple workers, scaling, etc.).