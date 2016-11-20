from flask import Flask, request, render_template
app = Flask(__name__)

# only until we get a database hooked in
cars = [1,2,3,4]

#
# DETAILED DESCRIPTION OF API CALL GOES HERE
#
@app.route("/location")
@app.route("/location/")
@app.route("/location/<int:car_number>", methods=['GET', 'PUT'])
def location(car_number=None):
    if request.method == "PUT":
    	return location_post(car_number)
    	return "posted"
    elif request.method == "GET":
	return location_request(car_number)
    else:
	return "PANIC"

# description of child function goes here
def location_post(car_number):
    if car_number in cars:
	return "Already have one"
    else:
	cars.append(car_number)
	return "Okay"

# description of child function goes here
def location_request(car_number):
    if car_number == None:
	ret_val = "list of cars:<br><ul>"
	for car in cars:
	    ret_val += "<li>" + "<a href='" + url_for('location', car_number=car) + "'>" + str(car) + "</a></li>"
	ret_val += "</ul>"
	return ret_val
    else:
	return "Location of car number: " + str(car_number)

