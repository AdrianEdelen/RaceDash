import time
import connection
import re
from textwrap import wrap
from packetProcessor import *
from car import *

def main():
    car = car()
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

    start = time.time()

    filepath = 'C:\\Users\\Mike\\Downloads\\candump1.log'
    file = open(filepath, 'r')
    lines = file.read().splitlines()
    
    canList = []

    start = time.time()
    for line in lines:
        canList.append(packetProcessor.process_packet_string(line))



    #average time between messages appears to be one ms
    

    #currently we have to just guess what the packet ID may be. this honestly may be fine
    #but if time starts becoming an issue we can order the packets by frequency
    # Primary goal is not to sacrifice packets.    
    calcs = 0
    for packet in canList:
        byteList = wrap(line[1], 2)
        # if len(byteList) == 8:
        #     A = int(byteList[0], 16)
        #     B = int(byteList[1], 16)
        #     C = int(byteList[2], 16)
        #     D = int(byteList[3], 16)
        #     E = int(byteList[4], 16)
        #     F = int(byteList[5], 16)
        #     G = int(byteList[6], 16)
        #     H = int(byteList[7], 16)
        
        #for now we are going to ignore short packets
        if packet.id == '144':
            continue
        elif packet.id == '142':
            continue
        elif packet.id == '141':
            # gear
            continue
        elif packet.id == '140':
            # accelpos
            #A / 2.55
            #G / 2.55
            # engine rpm
            # clutch pos
            # throttle pos
            # accel pedal on/off
            calcs += 2
            continue
        elif packet.id == '156':
            continue
        elif packet.id == '152':
            continue
        elif packet.id == '018':
            # steering angle

            #keep this for the love of god
            #this is basicaly bytes to int LE, 
            #with a sig/args like this bytesToIntLE(byteList, 0, 2)
            #args are raw bytelist, starting pos? total bytes included (inclusive))
            #in this case we want to start from the 7th byte, and take it and the next one
            #what that really means (atleast for translations sake) is start from byte 8,
            #grab the first 2, swap their order, and then & together adn take the int out of it
            #this is a PAIN IN THE ASS
            #a = byteList[6]
            #b = byteList[7]
            #val = int(a + b, 16)
            
            steeringAngle = (packetProcessor.byte_to_int_le(packet.data,0,2) * 0.1)
            print(steeringAngle)
            calcs += 1
            continue
        elif packet.id == '0D4':
            # FL wheel speed
            # FR wheel speed
            # RL wheel speed
            # RR wheel speed
            continue
        elif packet.id == '0D3':
            continue
        elif packet.id == '0D2':
            continue
        elif packet.id == '0D1':
            # brake pos %
            # brake pressure
            continue
        elif packet.id == '0D0':
            # steering angle
            # lat accel
            # long accel
            # combined accel
            # yaw
            continue
        elif packet.id == '282':
            continue
        elif packet.id == '370':
            continue
        elif packet.id == '440':
            continue
        elif packet.id == '361':
            # gear
            continue
        elif packet.id == '360':
            # coolant temp
            # engine oil temp
            # cruise on off
            # cruise set
            # cruise speed
            continue
        elif packet.id == '372':
            continue
        elif packet.id == '63B':
            continue
        elif packet.id == '442':
            continue
        elif packet.id == '375':
            continue
        elif packet.id == '374':
            continue
        elif packet.id == '4C8':
            continue
        elif packet.id == '6E1':
            continue
        elif packet.id == '6E2':
            continue
        elif packet.id == '4DD':
            continue
        elif packet.id == '4C3':
            continue
        elif packet.id == '4C1':
            continue
        elif packet.id == '4C6':
            continue
        else:
            print(packet.id)

        

    end = time.time()
    processTime = end - start
    print('the total processing time is: ',end - start)
    print('the total message time was: ')
    
    print ('calcs performed: ', calcs)
    print ('The average processing time of each packet is: ')
    print ('the average time between incomming messages is: ')
    print ('The total message count was: ')
    a = False
    # connection.start_can_interface()

    # can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native

    #msg = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], extended_id=False)
    #msg = can0.recv(10.0)
    # print(msg)
    # if msg is None:
    #    print('Timeout occurred, no message.')

    # connection.shutdown_can_interface()
main()
