from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

import logging
from logging_utils.logger import setup_logging
from endpoints.rainfallstations import get_rainfall_stations
from endpoints.weatherdata import get_weather_data

# Call setup_logging() to initialize the logging settings
setup_logging()
logging = logging.getLogger(__name__)

app = FastAPI(title="Experimental API for fetching BOM data from Postgres")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/rainfallstations")
def rainfall_stations():
    logging.info("rainfall stations data requested")
    return get_rainfall_stations()


@app.get("/weatherdata")
def weather_data():
    return get_weather_data()
