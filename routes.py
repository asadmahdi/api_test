from run import app
from flask import jsonify, request
from create_tables import create_connection
import sys, os
from psycopg2 import sql

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/property/get/<property_id>',  methods = ['GET'])
def get_property(property_id):
	try:
		conn = create_connection()
		cur = conn.cursor()
		cur.execute("SELECT * FROM property JOIN owner on property.ownerID = owner.id WHERE property.id = (%s)",(property_id,))
		result = cur.fetchone()
		prop = {
		'propID' : result[0],
		'geoID' : result[1],
		'legalDescription' : result[2],
		'situsAddress' :result[3],
		'ownerName' : result[6]
		}
		cur.close()
		conn.close()
		return jsonify({
			'propertyDetails' : prop
			})
	except Exception as e:
		return jsonify({'Error' : str(e)})

@app.route('/property/get-all',  methods = ['GET'])
def get_all_properties():
	try:
		conn = create_connection()
		cur = conn.cursor()
		cur.execute("SELECT * FROM property JOIN owner on property.ownerID = owner.id")
		result = cur.fetchall()
		property_list = []
		for row in result:
			print(row)
			prop = {
			'propID' : row[0],
			'geoID' : row[1],
			'legalDescription' : row[2],
			'situsAddress' :row[3],
			'ownerName' : row[6]
			}
			property_list.append(prop)
		cur.close()
		conn.close()
		return jsonify({
			'propertyList' : property_list
			})
	except Exception as e:
		return jsonify({'Error' : str(e)})

@app.route('/property/delete',  methods = ['DELETE'])
def delete_property():
	return 'Hello, World!'

@app.route('/property/update-address/',  methods = ['POST'])
def update_property_address():
	return 'Hello, World!'

@app.route('/owner/update-name/',  methods = ['POST'])
def update_owner_name():
	return 'Hello, World!'
