import time
import connection
import re
from textwrap import wrap
from packetProcessor import *
from car import *
from carSim import *
import queue

def getMessageTask():


    return


def main():
    sim = carSim()
    sim.loadRaw()
    curCar = car()
    #A NOTE OF WARNING FOR ANY ONLOOKERS:
    #THIS IS A HOT MESS
    # I AM PRETTY MUCH STILL AT THE EXPERIMENTATION STAGE
    # DO NOT JUDGE THIS CODE

    # data processing
    # recieve a message
    # pop into queue
    # log with timestamp

    # process messages
    # get first message in queue list
    # remove from queue
    # perform calcs
    # display/log
    
    messageQueue = queue.Queue()
    while True:
        nextPacket = sim.getNextmessage()
        messageQueue.put(nextPacket)
        if messageQueue.not_empty:
            curMess = messageQueue.get()
            packetProcessor.process_packet_string(curMess)
            messageQueue.task_done()
            print(messageQueue.unfinished_tasks)


    #average time between messages appears to be one ms
    #currently we have to just guess what the packet ID may be. this honestly may be fine
    #but if time starts becoming an issue we can order the packets by frequency
    # Primary goal is not to sacrifice packets.    
    # connection.shutdown_can_interface()
main()
