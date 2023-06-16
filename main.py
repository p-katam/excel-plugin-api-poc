from typing import Union
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

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
    return {
        "data": [
            {
                "latitude": -32.95,
                "longitude": 151.7,
                "stationName": "Location 1",
                "stationID": 1,
            },
            {
                "latitude": -32.96,
                "longitude": 151.71,
                "stationName": "Location 2",
                "stationID": 1,
            },
            {
                "latitude": -32.965,
                "longitude": 151.705,
                "stationName": "Location 3",
                "stationID": 1,
            },
        ]
    }


@app.get("/weatherdata")
def weather_data():
    return {
        "data": [
            ["1/1/2017", "The Phone Company", "Communications", "120"],
            ["1/2/2017", "Northwind Electric Cars", "Transportation", "142.33"],
            ["1/5/2017", "Best For You Organics Company", "Groceries", "27.9"],
            ["1/10/2017", "Coho Vineyard", "Restaurant", "33"],
            ["1/11/2017", "Bellows College", "Education", "350.1"],
            ["1/15/2017", "Trey Research", "Other", "135"],
            ["1/15/2017", "Best For You Organics Company", "Groceries", "97.88"],
        ]
    }
