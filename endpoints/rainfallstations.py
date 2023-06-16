from fastapi import APIRouter
from database.dbc import execute_query

router = APIRouter()


@router.get("/rainfallstations")
def get_rainfall_stations():
    # Execute the SQL query
    query = (
        "SELECT station_number, station_name, latitude, longitude FROM weather_station"
    )

    try:
        # Execute the query and retrieve the results
        results = execute_query(query)
    except Exception as e:
        print("An error occurred during reflection:")
        print(str(e))

    # Access the data from the results
    weather_stations = []
    for row in results:
        # Access the columns using indexing or column names
        station_number = row[0]  # Index-based access
        station_name = row[1]  # Index-based access
        latitude = row[2]  # Index-based access
        longitude = row[3]  # Index-based access

        # Create a dictionary for the weather station data
        station_data = {
            "stationNumber": station_number,
            "stationName": station_name,
            "latitude": latitude,
            "longitude": longitude,
        }
        weather_stations.append(station_data)

    # Return the weather stations data
    return {"data": weather_stations}
