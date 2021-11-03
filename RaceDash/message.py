from flask_restful import Resource
import json
"""
Message is a single translated piece of data from the can bus
E.G. time|speed|45
"""
class TranslatedMessage(Resource):
    def __init__(self, timeRecieved: float, name: str, magnitude: str) -> None:
        self.timeRecieved = round(timeRecieved,3)
        self.name = name
        self.magnitude = magnitude

    def __str__(self) -> str:
        return f'''{self.timeRecieved}|{self.name}:{self.magnitude}'''
    #convert to json string
    def ToJson(self):
        return json.dumps(self.car.__dict__, indent=4, sort_keys=True, default=str)

    #return a message in json
    def get(self):
        return self.ToJson(), 200



