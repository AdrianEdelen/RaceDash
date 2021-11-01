from flask_restful import Resource
import json


#time recieved should propably be a datetime of some type
#instead of keeping state of the car, we will process a packet and 
#split it into as many messages as needed,
#and then create this message object with it
#
class Message(Resource):
    def __init__(self, timeRecieved: int, name: str, magnitude: str) -> None:
        self.timeRecieved = timeRecieved
        self.name = name
        self.magnitude = magnitude

    def __str__(self) -> str:
        return f'''timestamp: {self.timeRecieved} | {self.name}: {self.magnitude}'''
    #convert to json string
    def ToJson(self):
        return json.dumps(self.car.__dict__, indent=4, sort_keys=True, default=str)

    #return a message in json
    def get(self):
        return self.ToJson(), 200



