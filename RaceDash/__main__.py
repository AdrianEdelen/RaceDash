import os
import queue
import canLogger
import canNetwork
import commandDict
from flask import Flask
from flask_restful import Resource, Api, reqparse
import configparser
import dbBroker

"""
The main method loads configurations, and starts the threads for parsing packets off of the bus
"""
def main():
    try:
        #create packet Queue
        print("Creating packet queue")
        packetQueue = queue.Queue()

        #open DB Connection
        #start api server
        api = Api(dbBroker.Broker())
    
        print("Loading config")
        #load config
        Config = configparser.ConfigParser()
        Config.read('RaceDash\config.ini')

        if Config.getboolean('Config', 'SpoofData'):
            bus = canNetwork.simCanCanUtils(packetQueue)
        else:
            bus = canNetwork.canCommunication(packetQueue)

        #start can logger
        print("Starting can logger")
        recorder = canLogger.CanLogger(packetQueue, 
        Config.getboolean('Config', 'UseDatabase'), 
        Config.getboolean('Config', 'UseFile'),
        Config.getboolean('Config', 'UseStream'), 
        commandDict.commmandDict(Config.get('Config', 'Car')).car)

        #start can network
        print("Starting can network")
        bus.startConnection() #open the can bus connection
        recorder.startProcessorThread() #start processing packets
        bus.startRecieveThread() #start listening for packets
        #it is important to start processing packets first, otherwise, you can build up a queue of messages

    except Exception as e:
        print(e)
        print("Unable to establish connection. Shutting down")
        
main()
