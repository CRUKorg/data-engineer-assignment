"""
Database connection example
"""
import logging
import psycopg
from retry.api import retry_call

logging.basicConfig(level=logging.INFO)

# connect to database
logging.info("Connecting to database...")
with retry_call(
    psycopg.connect,
    fargs=["host=db port=5432 dbname=postgres user=postgres password=postgres"],
    tries=10,
    delay=1,
) as conn:
    logging.info("Connected")
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        # Query the database and obtain data as Python objects.
        cur.execute("SELECT count(*) FROM sample;")
        print(f"Sample table has {cur.fetchone()[0]} rows")
