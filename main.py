import logging
import sys
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from endpoints.rainfallstations import get_rainfall_stations
from endpoints.weatherdata import get_weather_data

# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler(sys.stdout)],
)

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
