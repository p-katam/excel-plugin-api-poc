# this is the script that starts the server on Azure Webapp
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app