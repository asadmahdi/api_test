import psycopg2
import sys, os
from flask import jsonify

"""
method to connect to db
"""
def create_connection():
    conn = psycopg2.connect(
    database='d92qa4905r9bsr',
    user='lqtwdobqtkimqd',
    password='d50ab29944cc4c0281087f3245cce6c2affe87f1a2d21b7c7d38328b926a93d6',
    host='ec2-54-235-75-214.compute-1.amazonaws.com',
    port=5432
    )
    return conn

"""
methods for creating tables
"""
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
        return 'Error : ' + str(e)

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
        return 'Error : ' + str(e)
    
    

#create_owner_table()
#create_property_table()
