from threading import Thread
from textwrap import wrap
from packetProcessor import *
from car import *
import canNetwork

def main():

    print('***********************************************')
    print('*******************Main Menu*******************')
    print('* 1) Read can data from car                   *')
    print('* 2) Read can data from file (sim or playback)*')
    print('* 3) Exit                                     *')
    print('***********************************************')
    print('***********************************************')
    userInput = int(input())

    if userInput == 1:
        curCar = car(canNetwork.canCommunication()) #instantiate our car
    elif userInput == 2:
        curCar = car(canNetwork.simCanCommOld()) #instantiate sim car
    else:
        exit()

    #this try gets all connections going, at that point, they should be 
    #updating the properties of our car object in the background.
    #that means we can access the car periodically and get the current state of it
    try:
        
        curCar.canBus.startConnection() #open the can bus connection
        curCar.startProcessorThread() #start processing packets
        curCar.canBus.startRecieveThread() #start listening for packets
        #it is important to start processing packets first, otherwise, you can build up a queue of messages
        #i intend to handle this at some point by dropping loq priority messages
        #if the queue grows beynd n number of messages


        # while True:
        #     time.sleep(.016)
        #     os.system('cls' if os.name == 'nt' else 'clear')
        #     print(curCar)
        #     print('packets behind: ', curCar.canBus.Queue.unfinished_tasks)


    except KeyboardInterrupt:
        print('Shutting Down')
        curCar.dispose()

    

main()
