from typing import Union
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from endpoints.rainfallstations import get_rainfall_stations
from endpoints.weatherdata import get_weather_data

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
    return get_rainfall_stations()


@app.get("/weatherdata")
def weather_data():
    return get_weather_data()
