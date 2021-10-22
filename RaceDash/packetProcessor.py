import re
from textwrap import wrap

class packet:
    def __init__(self, device: str, id: str, data: str, timeStamp: float) -> None:
        self.device = device
        self.id = id
        self.data = data
        self.timeStamp = timeStamp

        def get_device(self):
            return self.device
        def get_id(self) -> int:
            return self.id
        def get_data(self):
            return self.data
        def get_timeStamp(self):
            return self.timeStamp

class packetProcessor:

    def process_packet_string(rawData):
        packetParts = rawData.split()
        timeStamp =float(re.sub(r'[\(\)]', '', packetParts[0]))
        device = packetParts[1]
        idAndMessage = packetParts[2].split('#')
        id = idAndMessage[0]
        data = idAndMessage[1].zfill(16)
        return packet(device, id, data, timeStamp)
       

    def byte_to_int_le(data: str, startBytePos: int, bytesToMergePos: int) -> int:
        byteList = wrap(data, 2)
        newList = []
        for startBytePos in range(bytesToMergePos):
            newList.append(byteList[-(bytesToMergePos - startBytePos)])
        return int(''.join(newList), 16)


        
    def identifyPacket(packet):
        if packet.id == '144':
            return
        elif packet.id == '142':
            return
        elif packet.id == '141':
            # gear
            return
        elif packet.id == '140':
            # accelpos
            #A / 2.55
            #G / 2.55
            # engine rpm
            # clutch pos
            # throttle pos
            # accel pedal on/off
            
            return
        elif packet.id == '156':
            return
        elif packet.id == '152':
            return
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
            
            
        elif packet.id == '0D4':
            # FL wheel speed
            # FR wheel speed
            # RL wheel speed
            # RR wheel speed
            return
        elif packet.id == '0D3':
            return
        elif packet.id == '0D2':
            return
        elif packet.id == '0D1':
            # brake pos %
            # brake pressure
            return
        elif packet.id == '0D0':
            # steering angle
            # lat accel
            # long accel
            # combined accel
            # yaw
            return
        elif packet.id == '282':
            return
        elif packet.id == '370':
            return
        elif packet.id == '440':
            return
        elif packet.id == '361':
            # gear
            return
        elif packet.id == '360':
            # coolant temp
            # engine oil temp
            # cruise on off
            # cruise set
            # cruise speed
            return
        elif packet.id == '372':
            return
        elif packet.id == '63B':
            return
        elif packet.id == '442':
            return
        elif packet.id == '375':
            return
        elif packet.id == '374':
            return
        elif packet.id == '4C8':
            return
        elif packet.id == '6E1':
            return
        elif packet.id == '6E2':
            return
        elif packet.id == '4DD':
            return
        elif packet.id == '4C3':
            return
        elif packet.id == '4C1':
            return
        elif packet.id == '4C6':
            return
        else:
            print(packet.id)

        


