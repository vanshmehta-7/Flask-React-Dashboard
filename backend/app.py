from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv
from flask_cors import CORS
from datetime import datetime, timedelta
import pytz
import json

load_dotenv("local.env")

app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("SECRET_KEY")


import pytz
from datetime import datetime

def format_time(time_str):
    # Remove the timezone label from the time string and strip any trailing whitespace
    time_formatted = time_str.replace('(Eastern Daylight Time)', '').strip()[:-5]
    
    # Parse the time string using the format string and create a datetime object
    dt = datetime.strptime(time_formatted, '%a %b %d %Y %H:%M:%S %Z')
    
    # Create a timezone object for US/Eastern and attach it to the datetime object
    eastern_tz = pytz.timezone('US/Eastern')
    dt = eastern_tz.localize(dt.replace(tzinfo=None), is_dst=None)
    
    # Format the datetime object as a string using the specified format string and return it
    final_time = dt.strftime('%Y-%m-%d %H:%M:%S%z')
    return final_time


@app.route("/", methods=["GET"])
def index():
    return "Ark Biotech"

@app.route("/temperature", methods=["GET"])
def temperature():
    #Create a connection to the PostgreSQL database using psycopg2 library.
    conn = psycopg2.connect(
        f'dbname={os.getenv("POSTGRES_DB")} user={os.getenv("POSTGRES_USER")} password={os.getenv("POSTGRES_PASSWORD")} host={os.getenv("POSTGRES_HOST")} port={os.getenv("POSTGRES_PORT")}'
        # "dbname=brx1 user=process_trending password=abc123 host=postgres port=5432"
    )

    #Create a cursor object to interact with the database and execute SQL queries.
    cur = conn.cursor()
 
    start_time_str = request.args.get('start')
    final_start = format_time(start_time_str)

    end_time_str = request.args.get('end')
    final_end = format_time(end_time_str) if end_time_str else "null"

    #check if the start time is equal to the first time in the database
    cur.execute("SELECT time FROM public.\"CM_HAM_DO_AI1/Temp_value\" ORDER BY time ASC LIMIT 1;")
    first_time = cur.fetchone()[0]

    if final_start == first_time:
        #return all the data from start_time
        cur.execute(
            "SELECT * FROM public.\"CM_HAM_DO_AI1/Temp_value\" WHERE time >= '" + final_start + "';",
        )
    else:
        #check if end_time is empty
        if final_end == "null":
            #return all the data from start_time
            cur.execute(
                "SELECT * FROM public.\"CM_HAM_DO_AI1/Temp_value\" WHERE time >= '" + final_start + "';",
            )
        else:
            #return data from start_time to end_time
            cur.execute(
                "SELECT * FROM public.\"CM_HAM_DO_AI1/Temp_value\" WHERE time >= '" + final_start + "' AND time <= '" + final_end + "';",
            )

    #Fetch all the records from the cursor after executing the SQL query   
    results = cur.fetchall()

    # convert the database result to a JSON response
    data = [{"time": str(row[0]), "value": row[1]} for row in results]
    return jsonify({"data": data})


@app.route("/ph", methods=["GET"])
def ph():
    #Create a connection to the PostgreSQL database using psycopg2 library.
    conn = psycopg2.connect(
        "dbname=brx1 user=process_trending password=abc123 host=postgres port=5432"
    )

    #Create a cursor object to interact with the database and execute SQL queries.
    cur = conn.cursor()
 
    start_time_str = request.args.get('start')
    final_start = format_time(start_time_str)

    end_time_str = request.args.get('end')
    final_end = format_time(end_time_str) if end_time_str else "null"

    #check if the start time is equal to the first time in the database
    cur.execute("SELECT time FROM public.\"CM_HAM_PH_AI1/pH_value\" ORDER BY time ASC LIMIT 1;")
    first_time = cur.fetchone()[0]

    if final_start == first_time:
        #return all the data from start_time
        cur.execute(
            "SELECT * FROM public.\"CM_HAM_PH_AI1/pH_value\" WHERE time >= '" + final_start + "';",
        )
    else:
        #check if end_time is empty
        if final_end == "null":
            #return all the data from start_time
            cur.execute(
                "SELECT * FROM public.\"CM_HAM_PH_AI1/pH_value\" WHERE time >= '" + final_start + "';",
            )
        else:
            #return data from start_time to end_time
            cur.execute(
                "SELECT * FROM public.\"CM_HAM_PH_AI1/pH_value\" WHERE time >= '" + final_start + "' AND time <= '" + final_end + "';",
            )
    
    #Fetch all the records from the cursor after executing the SQL query
    results = cur.fetchall()

    # convert the database result to a JSON response
    data = [{"time": str(row[0]), "value": row[1]} for row in results]
    return jsonify({"data": data})

@app.route("/distilled_oxygen", methods=["GET"])
def distilled_oxygen():
    #Create a connection to the PostgreSQL database using psycopg2 library.
    conn = psycopg2.connect(
        "dbname=brx1 user=process_trending password=abc123 host=postgres port=5432"
    )

    #Create a cursor object to interact with the database and execute SQL queries.
    cur = conn.cursor()
 
    start_time_str = request.args.get('start')
    final_start = format_time(start_time_str)

    end_time_str = request.args.get('end')
    final_end = format_time(end_time_str) if end_time_str else "null"


    #check if the start time is equal to the first time in the database
    cur.execute("SELECT time FROM public.\"CM_PID_DO/Process_DO\" ORDER BY time ASC LIMIT 1;")
    first_time = cur.fetchone()[0]

    if final_start == first_time:
        #return all the data from start_time
        cur.execute(
            "SELECT * FROM public.\"CM_PID_DO/Process_DO\" WHERE time >= '" + final_start + "';",
        )
    else:
        #check if end_time is empty
        if final_end == "null":
            #return all the data from start_time
            cur.execute(
                "SELECT * FROM public.\"CM_PID_DO/Process_DO\" WHERE time >= '" + final_start + "';",
            )
        else:
            #return data from start_time to end_time
            cur.execute(
                "SELECT * FROM public.\"CM_PID_DO/Process_DO\" WHERE time >= '" + final_start + "' AND time <= '" + final_end + "';",
            )

    #Fetch all the records from the cursor after executing the SQL query 
    results = cur.fetchall()

    # convert the database result to a JSON response
    data = [{"time": str(row[0]), "value": row[1]} for row in results]
    return jsonify({"data": data})


@app.route("/pressure", methods=["GET"])
def pressure():
    #Create a connection to the PostgreSQL database using psycopg2 library.
    conn = psycopg2.connect(
        "dbname=brx1 user=process_trending password=abc123 host=postgres port=5432"
    )

    #Create a cursor object to interact with the database and execute SQL queries.
    cur = conn.cursor()
 
    start_time_str = request.args.get('start')
    final_start = format_time(start_time_str)

    end_time_str = request.args.get('end')
    final_end = format_time(end_time_str) if end_time_str else "null"


    #check if the start time is equal to the first time in the database
    cur.execute("SELECT time FROM public.\"CM_PRESSURE/Output\" ORDER BY time ASC LIMIT 1;")
    first_time = cur.fetchone()[0]

    if final_start == first_time:
        #return all the data from start_time
        cur.execute(
            "SELECT * FROM public.\"CM_PRESSURE/Output\" WHERE time >= '" + final_start + "';",
        )
    else:
        #check if end_time is empty
        if final_end == "null":
            #return all the data from start_time
            cur.execute(
                "SELECT * FROM public.\"CM_PRESSURE/Output\" WHERE time >= '" + final_start + "';",
            )
        else:
            #return data from start_time to end_time
            cur.execute(
                "SELECT * FROM public.\"CM_PRESSURE/Output\" WHERE time >= '" + final_start + "' AND time <= '" + final_end + "';",
            )
    
    #Fetch all the records from the cursor after executing the SQL query
    results = cur.fetchall()

    # convert the database result to a JSON response
    data = [{"time": str(row[0]), "value": row[1]} for row in results]
    return jsonify({"data": data})

