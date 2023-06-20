from database.dbc import execute_query
from datetime import datetime


def get_weather_data(station_number, from_date, to_date):
    # Convert the date strings to datetime objects
    from_date = datetime.strptime(from_date, "%d-%m-%Y").date()
    to_date = datetime.strptime(to_date, "%d-%m-%Y").date()

    query = """
    SELECT
        {columns}
    FROM
        weather_data
    WHERE
        station_number = {station_number}
        AND to_date(dd || '-' || mm || '-' || yyyy, 'DD-MM-YYYY') BETWEEN '{from_date}' AND '{to_date}'
    ORDER BY
        to_date(dd || '-' || mm || '-' || yyyy, 'DD-MM-YYYY')
    """

    try:
        # Get the column names from the table
        columns_query = """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = 'weather_data'
        """
        columns_result = execute_query(columns_query)
        all_columns = [row[0] for row in columns_result]

        # Filter out the columns containing "quality"
        columns = [column for column in all_columns if "quality" not in column]

        formatted_columns = ", ".join(columns)
        formatted_from_date = from_date.strftime("%Y-%m-%d")
        formatted_to_date = to_date.strftime("%Y-%m-%d")

        # Execute the query and retrieve the results
        results = execute_query(
            query.format(
                columns=formatted_columns,
                station_number=station_number,
                from_date=formatted_from_date,
                to_date=formatted_to_date,
            )
        )

        # Access the data from the results
        weather_data = []
        for row in results:
            data_row = list(row)  # Convert the row tuple to a list
            weather_data.append(data_row)

        # Return the weather data
        return {"data": weather_data}

    except Exception as e:
        print("An error occurred during query execution:")
        print(str(e))
        return {"error": "An error occurred"}
