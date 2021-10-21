import time
import connection
import re
from textwrap import wrap

def main():
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

    filepath = 'C:\\Users\\Mike\\Downloads\\candump1.log'
    file = open(filepath, 'r')
    lines = file.read().splitlines()
    canList = []
    canMessagesList = []
    timestamps = []
    for line in lines:
        time1 = line[1:18]
        
        timestamps.append(float(time1))

    messageCount = len(timestamps)
    maxTime = max(timestamps)
    minTime = min(timestamps)
    totalTime = maxTime - minTime
    
    ave = (totalTime / messageCount)

    start = time.time()

    for line in lines:
        canList.append(line[25:])

    for line in canList:
        a = line.split('#')
        canMessagesList.append(a)

    

    #average time between messages appears to be one ms
    

    #currently we have to just guess what the packet ID may be. this honestly may be fine
    #but if time starts becoming an issue we can order the packets by frequency
    # Primary goal is not to sacrifice packets.    
    calcs = 0
    for line in canMessagesList:
        byteList = wrap(line[1], 2)
        if len(byteList) == 8:
            A = int(byteList[0], 16)
            B = int(byteList[1], 16)
            C = int(byteList[2], 16)
            D = int(byteList[3], 16)
            E = int(byteList[4], 16)
            F = int(byteList[5], 16)
            G = int(byteList[6], 16)
            H = int(byteList[7], 16)
        else:
            continue
        #for now we are going to ignore short packets
        if line[0] == '144':
            continue
        elif line[0] == '142':
            continue
        elif line[0] == '141':
            # gear
            continue
        elif line[0] == '140':
            # accelpos
            A / 2.55
            G / 2.55
            # engine rpm
            # clutch pos
            # throttle pos
            # accel pedal on/off
            calcs += 2
            continue
        elif line[0] == '156':
            continue
        elif line[0] == '152':
            continue
        elif line[0] == '018':
            # steering angle

            #keep this for the love of god
            #this is basicaly bytes to int LE, 
            #with a sig/args like this bytesToIntLE(byteList, 0, 2)
            #args are raw bytelist, starting pos? total bytes included (inclusive))
            #in this case we want to start from the 7th byte, and take it and the next one
            #what that really means (atleast for translations sake) is start from byte 8,
            #grab the first 2, swap their order, and then & together adn take the int out of it
            #this is a PAIN IN THE ASS
            a = byteList[6]
            b = byteList[7]
            val = int(a + b, 16)
            finalVal = val * (0.1)
            calcs += 1
            continue
        elif line[0] == '0D4':
            # FL wheel speed
            # FR wheel speed
            # RL wheel speed
            # RR wheel speed
            continue
        elif line[0] == '0D3':
            continue
        elif line[0] == '0D2':
            continue
        elif line[0] == '0D1':
            # brake pos %
            # brake pressure
            continue
        elif line[0] == '0D0':
            # steering angle
            # lat accel
            # long accel
            # combined accel
            # yaw
            continue
        elif line[0] == '282':
            continue
        elif line[0] == '370':
            continue
        elif line[0] == '440':
            continue
        elif line[0] == '361':
            # gear
            continue
        elif line[0] == '360':
            # coolant temp
            # engine oil temp
            # cruise on off
            # cruise set
            # cruise speed
            continue
        elif line[0] == '372':
            continue
        elif line[0] == '63B':
            continue
        elif line[0] == '442':
            continue
        elif line[0] == '375':
            continue
        elif line[0] == '374':
            continue
        elif line[0] == '4C8':
            continue
        elif line[0] == '6E1':
            continue
        elif line[0] == '6E2':
            continue
        elif line[0] == '4DD':
            continue
        elif line[0] == '4C3':
            continue
        elif line[0] == '4C1':
            continue
        elif line[0] == '4C6':
            continue
        else:
            print(line[0])

        

    end = time.time()
    processTime = end - start
    print('the total processing time is: ',end - start)
    print('the total message time was: ', totalTime)
    
    
    

    aveIndTimes = processTime / messageCount
    print ('calcs performed: ', calcs)
    print ('The average processing time of each packet is: ', aveIndTimes)
    print ('the average time between incomming messages is: ', ave)
    print ('The total message count was: ', messageCount)
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
