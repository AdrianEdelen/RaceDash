from threading import Thread
from packetCommand import *
from textwrap import wrap
from packetProcessor import *
from car import *
import canNetwork


def main():
    curCar = car(canNetwork.simCanComm) #instantiate our car
    curCar.canNetworkInterface.startConnection() #open the can bus connection
    curCar.canNetworkInterface.startRecieveThread() #start listening for packets
    
    while True:
        curMess = curCar.canNetworkInterface.messageQueue.get(True)
        packet = packetProcessor.process_packet_string(curMess)
        
        curCar.canNetworkInterface.messageQueue.task_done()
        if curCar.canNetworkInterface.messageQueue.unfinished_tasks > 0:
            print(curCar.canNetworkInterface.messageQueue.unfinished_tasks)

main()
