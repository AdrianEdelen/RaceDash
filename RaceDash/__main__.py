from threading import Thread
from packetCommand import *
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

    cmdDict = commandDict().commands

    try:
        curCar.canBus.startConnection() #open the can bus connection
        curCar.canBus.startRecieveThread()
    except KeyboardInterrupt:
        print('Shutting Down')
        os.system('sudo ifconfig can0 down')

main()
