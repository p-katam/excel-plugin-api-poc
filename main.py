from typing import Union
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/weatherdata")
def weather_data():
    data = [
        ["1/1/2017", "The Phone Company", "Communications", "120"],
        ["1/2/2017", "Northwind Electric Cars", "Transportation", "142.33"],
        ["1/5/2017", "Best For You Organics Company", "Groceries", "27.9"],
        ["1/10/2017", "Coho Vineyard", "Restaurant", "33"],
        ["1/11/2017", "Bellows College", "Education", "350.1"],
        ["1/15/2017", "Trey Research", "Other", "135"],
        ["1/15/2017", "Best For You Organics Company", "Groceries", "97.88"],
    ]

    response = {"data": data}

    # Add the headers to the response
    headers = {
        "Access-Control-Allow-Origin": "*",  # Allow requests from any origin
        "Access-Control-Allow-Headers": "Content-Type",  # Specify allowed headers
    }

    return Response(content=response, headers=headers)
