from dotenv import load_dotenv
import os
import psycopg2

# Load environment variables from .env file
load_dotenv()

# Database connection variables
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SERVER_HOST = os.getenv("DB_SERVER_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


def execute_query(query):
    # Establish a connection to the database
    conn = psycopg2.connect(
        host=DB_SERVER_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD,
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    return result
