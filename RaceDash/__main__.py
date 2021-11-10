import os
import queue
import canLogger
import canNetwork
from flask import Flask
from flask_restful import Resource, reqparse
import dbBroker
import api

"""
The main method loads configurations, and starts the threads for parsing packets off of the bus
"""
def main():
    try:
        #create packet Queue
        print("Creating packet queue")
        packetQueue = queue.Queue()

        #open DB Connection
        broker = dbBroker.Broker()
        #start api server
        lApi = api.api(broker)
    
        #for testing purposes, use the mock canNetwork
        #bus = canNetwork.simCanCanUtils(packetQueue)
        bus = canNetwork.canCommunication(packetQueue, 'can0')

        #start can logger
        print("Starting can logger")
        recorder = canLogger.CanLogger(packetQueue)

        #start can network
        print("Starting can network")
        bus.startConnection() #open the can bus connection
        recorder.startProcessorThread() #start processing packets
        bus.startRecieveThread() #start listening for packets
        #it is important to start processing packets first, otherwise, you can build up a queue of messages

    except KeyboardInterrupt:
        print("Keyboard Interrupt, Shutting Down")
        bus.closeConnection()
        recorder.dbConn.close()
        exit()
    except Exception as e:
        print(e)
        print("Unable to establish connection. Shutting down")
        
main()
