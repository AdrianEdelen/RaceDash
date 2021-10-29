
from car import *
import canNetwork

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast



"""
The current main menu, basic TTY display that should really only be used for debugging
"""
def main():
    
    #setup api stuff
    app = Flask(__name__)
    api = Api(app)
    
    print('*******************Main Menu*******************')
    print('* 1) Read can data from car                   *')
    print('* 2) Read can data from file (sim or playback)*')
    print('* 3) Exit                                     *')
    print('***********************************************')
    userInput = int(input())

    if userInput == 1:
        curCar = car(canNetwork.canCommunication()) #instantiate our car
    elif userInput == 2:
        curCar = car(canNetwork.simCanCanUtils()) #instantiate sim car
    else:
        exit()

    try:
        curCar.canBus.startConnection() #open the can bus connection
        curCar.startProcessorThread() #start processing packets
        curCar.canBus.startRecieveThread() #start listening for packets
        #it is important to start processing packets first, otherwise, you can build up a queue of messages

        
        #start api server
        api.add_resource(car(), '/Car')
        if __name__ == '__main__':
            app.run()

    except:
        print("Unable to establish connection. Shutting down")
        curCar.dispose()
    
    # try:
    #     while True:
    #         a = curCar.get()

            
    #         #os.system('cls' if os.name == 'nt' else 'clear')
    #         #print(curCar)
    #         #exit()
    # except KeyboardInterrupt:
    #     print('Shutting Down')
    #     curCar.dispose()
    #   # run our Flask app
    
main()
