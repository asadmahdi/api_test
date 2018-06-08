import psycopg2
import sys, os
from flask import jsonify

def exception_handler(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print(str(e))
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    return jsonify({
        'error': str(e),
        'type' : str(exc_type),
        'file' : str(fname),
        'line' : str(exc_tb.tb_lineno)
        })

def create_connection():
    conn = psycopg2.connect(
    database='d92qa4905r9bsr',
    user='lqtwdobqtkimqd',
    password='d50ab29944cc4c0281087f3245cce6c2affe87f1a2d21b7c7d38328b926a93d6',
    host='ec2-54-235-75-214.compute-1.amazonaws.com',
    port=5432
    )
    return conn

def create_owner_table():
    conn = create_connection()
    try:
        cur = conn.cursor()

        cur.execute(
            """
            CREATE TABLE owner(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255)
            )""")
        cur.close()
        conn.commit()
        conn.close()

    except Exception as e:
        conn.close()
        return str(e)

def create_property_table():
    conn = create_connection()
    try:
        cur = conn.cursor()

        cur.execute(
            """
            CREATE TABLE property(
            id INTEGER PRIMARY KEY,
            geoID VARCHAR(255),
            legalDescription VARCHAR(255),
            situsAddress VARCHAR(255),
            ownerID INTEGER REFERENCES owner (id)
            )""")
        cur.close()
        conn.commit()
        conn.close()

    except Exception as e:
        conn.close()
        return str(e)
    
    

#create_owner_table()
create_property_table()
