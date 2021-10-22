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
        curCar = car(canNetwork.simCanComm()) #instantiate sim car
    else:
        exit()

    cmdDict = commandDict().commands
    curCar.canNetworkInterface.startConnection() #open the can bus connection
    curCar.canNetworkInterface.startRecieveThread() #start listening for packets
    
    while True:
        #time.sleep(10)
        curMess = curCar.canNetworkInterface.messageQueue.get(True)
        packet = packetProcessor.process_packet_string(curMess)
        try:
            thing = cmdDict[packet.id]
        except KeyError:
            print('Unknown packet ID', packet.id)

        curCar.canNetworkInterface.messageQueue.task_done()
        if curCar.canNetworkInterface.messageQueue.unfinished_tasks > 0:
            print(curCar.canNetworkInterface.messageQueue.unfinished_tasks)

main()
