
from typing import DefaultDict
import can

"""
The packetCommand module takes all the possible packet ids from a car and performs the operations
required to extract the data out of them
This is done by creating a generic interface that each command
implements and putting them in a dict.
this way we just need to add the method and add it to the dict to create new packet handlers
then search through the dict and call the method associated with the id

the method processes the id and returns either a string or list of strings
that contain the appropriate data.

"""

class commandDict:
    def __init__(self):
        self.commands = {
            '144': _144, '142': _142, '141': _141, '140': _140, '156': _156, '152': _152,
            '018': _018, '0D4': _0D4, '0D3': _0D3, '0D2': _0D2, '0D1': _0D1, '0D0': _0D0, 
            '282': _282, '370': _370, '440': _440, '361': _361, '360': _360, '372': _372,
            '63B': _63B, '442': _442, '375': _375, '374': _374, '4C8': _4C8, '6E1': _6E1,
            '6E2': _6E2, '4DD': _4DD, '4C3': _4C3, '4C1': _4C1, '4C6': _4C6 }
        
class packetCommandInterface:
    def exec(msg: can.Message):
        pass

class _144(packetCommandInterface):
    def exec(msg: can.Message):
        #unknown
        print('parsed packed id 144')
        pass

class _142(packetCommandInterface):
    def exec(msg: can.Message):
        #unknown
        print('parsed packed id 142')
        pass

class _141(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 141')
        pass

class _140(packetCommandInterface):
    def exec(msg: can.Message):
        # accelpos
        #A / 2.55
        #G / 2.55
        # engine rpm
        # clutch pos
        # throttle pos
        # accel pedal on/off
        print('parsed packed id 140')
        pass

class _156(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 156')
        pass

class _152(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 152')
        pass

class _018(packetCommandInterface):
    def exec(msg: can.Message):
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
            
        #steeringAngle = (packetProcessor.byte_to_int_le(packet.data,0,2) * 0.1)
        #print(steeringAngle)
        print('parsed packed id 018')
        pass

class _0D4(packetCommandInterface):
    def exec(msg: can.Message):
        # FL wheel speed
        # FR wheel speed
        # RL wheel speed
        # RR wheel speed
        print('parsed packed id 0D4')
        pass

class _0D3(packetCommandInterface):
    def exec(msg: can.Message):
        #unknown
        print('parsed packed id 0D3')
        pass

class _0D2(packetCommandInterface):
    def exec(msg: can.Message):
        #unknown
        print('parsed packed id 0D2')
        pass

class _0D1(packetCommandInterface):
    def exec(msg: can.Message):
        # brake pos %
        # brake pressure
        print('parsed packed id 0D1')
        pass

class _0D0(packetCommandInterface):
    def exec(msg: can.Message):
        # steering angle
        # lat accel
        # long accel
        # combined accel
        # yaw
        print('parsed packed id 0D0')
        pass

class _282(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 282')
        pass

class _370(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 370')
        pass

class _440(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 440')
        pass   

class _361(packetCommandInterface):
    def exec(msg: can.Message):
        # gear
        print('parsed packed id 361')
        pass

class _360(packetCommandInterface):
    def exec(msg: can.Message):
        # coolant temp
        # engine oil temp
        # cruise on off
        # cruise set
        # cruise speed
        print('parsed packed id 360')
        pass

class _372(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 372')
        pass

class _63B(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 63B')
        pass

class _442(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 442')
        pass

class _375(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 375')
        pass

class _374(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 374')
        pass

class _4C8(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 4C8')
        pass

class _6E1(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 6E1')
        pass

class _6E2(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 6E2')
        pass

class _4DD(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 4DD')
        pass

class _4C3(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 4C3')
        pass

class _4C1(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 4C1')
        pass

class _4C6(packetCommandInterface):
    def exec(msg: can.Message):
        print('parsed packed id 4C6')
        pass

class unknown(packetCommandInterface):
    def exec(msg: can.Message):
        print(msg.arbitration_id)
        pass
            