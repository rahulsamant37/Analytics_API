#!/bin/bash

cd /code/src
RUN_PORT=${PORT:-8000}
RUN_HOST=${HOST:-0.0.0.0}

uv run uvicorn main:app --host $RUN_HOST --port $RUN_PORT