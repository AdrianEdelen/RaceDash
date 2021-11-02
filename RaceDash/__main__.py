import canLogger
import canNetwork
import commandDict
from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast

"""
The current main menu, will run in a tight loop to keep the app running
"""
def main():
    
    #setup api stuff
    app = Flask(__name__)
    api = Api(app)
    
    #all of these options should be moved to config files
    print('*******************Main Menu*******************')
    print('* 1) Read can data from car                   *')
    print('* 2) Read can data from file (sim or playback)*')
    print('* 3) Exit                                     *')
    print('***********************************************')
    userInput = int(input())

    if userInput == 1:
        bus = canNetwork.canCommunication()
        
    elif userInput == 2:
        bus = canNetwork.simCanCanUtils()
        
    else:
        exit()

    print('*******************Car Menu*******************')
    print('* 1) FRS                                      *')
    print('***********************************************')
    userInput = int(input()) #the car will be set in config but determined here
    if userInput == 1:
        cmds = commandDict.commmandDict('FRS')
    
    useDB = True #these flags will be set in config
    useFile = True
    useStream = True

    recorder = canLogger.CanLogger(bus.Queue, useDB, useFile,useStream, cmds)
    try:

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
