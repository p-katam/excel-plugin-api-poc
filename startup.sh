pip install --upgrade pip

gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app