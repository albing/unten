from flask import Flask, request, render_template
app = Flask(__name__)

# only until we get a database hooked in
cars = [1,2,3,4]

#
# /location/
#
# Things to do with locations
#
# As a driver, I want to:
# 	* update my location so that my passengers can see how close I am to picking them up
#
# As a passenger, I want to:
# 	* alert a driver where I want to be picked up
#
@app.route("/location")
@app.route("/location/")
@app.route("/location/<int:car_number>", methods=['GET', 'PUT'])
def location(car_number=None):
    if request.method == "PUT":
    	return location_put(car_number)
    	return "posted"
    elif request.method == "GET":
	return location_request(car_number)
    else:
	return "PANIC"

# PUT method
# changes the location of a driver or requester
def location_put(car_number):
    if car_number in cars:
	return "Already have one"
    else:
	cars.append(car_number)
	return "Okay"


# GET method
# Get the location of a person.
# If no person is given, get a listing of all possible people
def location_request(car_number):
    if car_number == None:
	# json: TODO: use 3rd-party formatter
	ret_val = "{cars:["
	ret_val += ",".join([str(x) for x in cars])
	ret_val += "]}"
	return ret_val
	# TODO: allow for other formats
    else:
	return "Location of car number: " + str(car_number)

