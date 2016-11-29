"""Unter - It's like Uber

This is the Flask description of the API service for Unter
"""

import sqlite3
from flask import Flask, request, render_template, Response, abort
app = Flask(__name__)

# open the DB and run the schema script
schema_filename = "schema.sql"
db_conn = sqlite3.connect('unter.db')
with open(schema_filename, 'r') as f:
    script = "\n".join(f.readlines())
    db_conn.executescript(script)


@app.route("/location")
@app.route("/location/")
@app.route("/location/<int:car_number>", methods=['GET', 'PUT'])
def location(car_number=None):
    """Things to do with locations

    As a driver, I want to:
	    * update my location so that my passengers can see how close I am to picking them up

    As a passenger, I want to:
	    * alert a driver where I want to be picked up
    """

    if request.method == "PUT":
    	return location_put(car_number)
    	return "posted"
    elif request.method == "GET":
	return location_request(car_number)
    else:
	return "PANIC"

def location_put(car_number):
    """changes the location of a driver or requester"""

    if car_number in cars:
	return "Already have one"
    else:
	cars.append(car_number)
	return "Okay"


def location_request(car_number):
    """Get the location of a person.

    If no person is given, get a listing of all possible people"""

    if car_number == None:
	# json: TODO: use 3rd-party formatter
	ret_val = "{cars:["
	ret_val += ",".join([str(x) for x in cars])
	ret_val += "]}"
	return ret_val
	# TODO: allow for other formats
    else:
	return "Location of car number: " + str(car_number)



@app.route('/car_data/')
def car_data():
    """Show me all of the data for all cars driving"""
    for car in cars:
	pass
	# is it a driver?
	# no: continue
	# yes: return driver name, car name, passengers' names


@app.route('/person/', methods=['GET'])
def list_person():
    global db_conn

    cursor = db_conn.cursor()
    cursor.execute("SELECT * from person")
    resp = "<ul>"
    for item in cursor:
	resp += "<li>" + str(item) + "</li>"
    resp += "</ul>"
    return resp

@app.route('/person/<string:name>', methods=['POST'])
def new_person(name):
    global db_conn

    cursor = db_conn.cursor()
    cursor.execute("Insert into person (name) values(?)", (name, ))
    new_id = str(cursor.lastrowid)
    resp = Response("created id: " + new_id)
    resp.status_code = 201
    resp.headers['Location'] = '/person/'+ new_id
    db_conn.commit()
    return resp

@app.route('/person/<int:id>', methods=['GET'])
def get_person(id=None):
    global db_conn

    if request.method == 'GET':
	cursor = db_conn.cursor()
	cursor.execute("SELECT name from person where id = " + str(id))
	name = cursor.fetchone()
	if name is not None:
	    return str(name[0])
	else:
	    abort(404)

@app.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    global db_conn

    cursor = db_conn.cursor()
    cursor.execute("DELETE FROM person where id = " + str(id))
    db_conn.commit()
    return ('', 204)
