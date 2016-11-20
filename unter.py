from flask import Flask
app = Flask(__name__)

@app.route("/status")
def status():
    return "Status!"


cars = [1,2,3,4]
@app.route("/location")
@app.route("/location/<int:car_number>")
def get_location(car_number=None):
    if car_number == None:
	ret_val = "list of cars:<br><ul>"
	for car in cars:
	    ret_val += "<li>" + str(car) + "</li>"
	ret_val += "</ul>"
	return ret_val
    else:
	return "Location of car number: " + str(car_number)


    # getLocation(car_number=3)
