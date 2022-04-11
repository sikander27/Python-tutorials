"""
For a parking space of 5 slots, please create 4 API endpoints which are mentioned below:
1. Park a Car: The endpoint will be given the input - car number. Output is the slot
where it is parked. If the parking lot is full, the appropriate error message is returned. #POST --> /parking/{car_number}
2. Unpark the Car: The endpoint will be given the input - slot number, from which the car is to be removed.
Output is a message if car is successfully unparked. #POST/DELETE --> /parking/{car_number}
3. Get the Car and Slot Information via slot number: This endpoint will be given the input - slot number.
output - return both the car number and slot number for the input. #GET --> /parking/slot/{nuber}
4. Get the Car and Slot Information via car number: This endpoint will be given the input - car number.
output - return both the car number and slot number for the input. #GET --? /parking/info/{car_number}

Note: You cannot use any database for storage
"""
import re
from tkinter import E
from flask import Flask, request
import json

app = Flask(__name__)

parking_space = [26,32,65,14,24] # [0, 0, 0, 0, 0]

# Get car info
@app.route("/parking/info", methods = ['POST'])
def park_car():
    slot_number = request.data
    if parking_space[slot_number] and parking_space[slot_number] != 0:
        return json.dumps({"car_number":parking_space[slot_number]})
        
    if len(parking_space) >= 5 and parking_space.count(0) != 5: # [0, 0, 0, 0, 0]
        return json.dumps({"message":"Sorry, Parking Full!"})
    else:
        parking_space.append(car_number)
        return json.dumps({"slot_no":parking_space.index(car_number)})

# Parking
@app.route("/parking", methods = ['POST'])
def park_car():
    car_number = request.data
    if len(parking_space) >= 5 and parking_space.count(0) != 5: # [0, 0, 0, 0, 0]
        return json.dumps({"message":"Sorry, Parking Full!"})
    else:
        parking_space.append(car_number)
        return json.dumps({"slot_no":parking_space.index(car_number)})

# Un-Parking
@app.route("/parking/unpark", methods = ['POST'])
def unpark_car():
    slot_number = request.data
    # import pdb; pdb.set_trace()
    # return json.dumps({"slot": slot_number})
    if slot_number > 4:
        return json.dumps({"message":"Please pass valid slot id"})
    elif parking_space[slot_number]: # [ 12,]
        parking_space[slot_number] = 0
        return json.dumps({"message":"Successfully unparked car"})
    # elif parking_space[slot_number]: # [ 12,]
    #     parking_space.remove(slot_number)
    #     return json.dumps({"message":"Successfully unparked car"})

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



if __name__ == "__main__":
    app.run(debug=True)





