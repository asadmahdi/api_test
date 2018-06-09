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
        cur.execute("SELECT * FROM property JOIN owner on\
         property.ownerID = owner.id WHERE property.id = (%s)",(property_id,))
        result = cur.fetchone()
        if (not result):
            return jsonify({'Error' : 'Invalid property id'}),404
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
            }),200
    except Exception as e:
        return jsonify({'Error' : str(e)}),500

@app.route('/property/get-all',  methods = ['GET'])
def get_all_properties():
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM property JOIN owner on property.ownerID = owner.id")
        result = cur.fetchall()
        property_list = []
        for row in result:
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
            }),200
    except Exception as e:
        return jsonify({'Error' : str(e)}),500

@app.route('/property/delete/<property_id>',  methods = ['DELETE'])
def delete_property(property_id):
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM property WHERE id = (%s)", (property_id,))
        cur.close()
        conn.commit()
        conn.close()
        return jsonify({
            'Status' : 'property ' + property_id + ' deleted'
            }),202
    except Exception as e:
        conn.close()
        return jsonify({'Error' : str(e)}),500
    


@app.route('/property/update-address/<property_id>',  methods = ['POST'])
def update_property_address(property_id):
    conn = create_connection()
    try:

        payload = request.get_json()

        new_address = payload['newAddress']
        if(not new_address):
            return jsonify({
                'Error' : 'No new address provided'
                }),400

        cur = conn.cursor()
        cur.execute("UPDATE property SET situsAddress = (%s) WHERE id = (%s)", (new_address,property_id))
        cur.close()
        conn.commit()
        conn.close()
        return jsonify({
            'Status' : 'Property ' + property_id + '\'s address succesfully updated'
            }),200
    except Exception as e:
        conn.close()
        return jsonify({'Error' : str(e)}),500

@app.route('/owner/update-name/<owner_id>',  methods = ['POST'])
def update_owner_name(owner_id):
    conn = create_connection()
    try:
        payload = request.get_json()

        new_name = payload.get('newName')
        if(not new_name):
            return jsonify({
                'Error' : 'No new name provided'
                }),400
        cur = conn.cursor()
        cur.execute("UPDATE owner SET name = (%s) WHERE id = (%s)", (new_name,owner_id))
        cur.close()
        conn.commit()
        conn.close()
        return jsonify({'Status' : 'Owner name succesfully updated to' + new_name})
    except Exception as e:
        conn.close()
        return jsonify({'Error' : str(e)}),500

