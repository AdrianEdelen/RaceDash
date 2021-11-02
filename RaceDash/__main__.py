import os
import canLogger
import canNetwork
import commandDict
from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast
import configparser

"""
The current main menu, will run in a tight loop to keep the app running
"""
def main():
    try:
    #setup api stuff
        app = Flask(__name__)
        api = Api(app)
    
        #load config
        Config = configparser.ConfigParser()
        Config.read('RaceDash\config.ini')

        if Config.getboolean('Config', 'SpoofData'):
            bus = canNetwork.simCanCanUtils()
        else:
            bus = canNetwork.canCommunication()

        recorder = canLogger.CanLogger(bus.Queue, 
        Config.getboolean('Config', 'UseDatabase'), 
        Config.getboolean('Config', 'UseFile'),
        Config.getboolean('Config', 'UseStream'), 
        commandDict.commmandDict(Config.get('Config', 'Car')).car)

        bus.startConnection() #open the can bus connection
        recorder.startProcessorThread() #start processing packets
        bus.startRecieveThread() #start listening for packets
        #it is important to start processing packets first, otherwise, you can build up a queue of messages

        #start api server
        #hold on this
        # api.add_resource(carApi, '/Car',
        #          resource_class_kwargs={'car': curCar})
        # if __name__ == '__main__':
        #     app.run()
    except Exception as e:
        print(e)
        print("Unable to establish connection. Shutting down")
        
main()
