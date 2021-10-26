
from typing import DefaultDict
import can
from packetProcessor import packetProcessor
import car

"""
The packetCommand module takes all the possible packet ids from a car and performs the operations
required to extract the data out of them
This is done by creating a generic interface that each command
implements and putting them in a dict.
this way we just need to add the method and add it to the dict to create new packet handlers
then search through the dict and call the method associated with the id

the method process the data of the message and sets the properties of the car object

"""

"""I am not sure what to do with this. for now I am leaving this code in here because it is a lot
of boiler plate that I don't want to retype, but I am not sure if this pattern is actually
any faster than if else, or easier to read, or easier to expand.
if it ends up being faster and a giant if else is no good, we may come back to it"""

"""
self.commands = {
            '144': _144, '142': _142, '141': _141, '140': _140, '156': _156, '152': _152,
            '018': _018, '0D4': _0D4, '0D3': _0D3, '0D2': _0D2, '0D1': _0D1, '0D0': _0D0, 
            '282': _282, '370': _370, '440': _440, '361': _361, '360': _360, '372': _372,
            '63B': _63B, '442': _442, '375': _375, '374': _374, '4C8': _4C8, '6E1': _6E1,
            '6E2': _6E2, '4DD': _4DD, '4C3': _4C3, '4C1': _4C1, '4C6': _4C6 }
            """


class commandDict:
    
    def _144(self, msg: can.Message.data):
        return 'parsed packet id 144'

    def _142(self, msg: can.Message.data):
        # unknown
        print('parsed packet id 142')
        pass

    def _141(self, msg: can.Message.data):
        print('parsed packet id 141')
        pass

    def _140(self, msg: can.Message.data):
        # accelpos
        #A / 2.55
        #G / 2.55
        # engine rpm
        # clutch pos
        # throttle pos
        # accel pedal on/off
        print('parsed packet id 140')
        pass

    def _156(self, msg):
        
        print('parsed packet id 156')
        pass

    def _152(self, msg: can.Message.data):
        print('parsed packet id 152')
        pass

    def _018(self, msg: can.Message.data):
        # steering angle

        # keep this for the love of god
        # this is basicaly bytes to int LE,
        # with a sig/args like this bytesToIntLE(byteList, 0, 2)
        # args are raw bytelist, starting pos? total bytes included (inclusive))
        # in this case we want to start from the 7th byte, and take it and the next one
        # what that really means (atleast for translations sake) is start from byte 8,
        # grab the first 2, swap their order, and then & together adn take the int out of it
        # this is a PAIN IN THE ASS
        #a = byteList[6]
        #b = byteList[7]
        #val = int(a + b, 16)
        self.car.steering_angle_one =  round(packetProcessor.byte_to_int_le(msg, 0, 2) * 0.1, 4)
        #steeringAngle = (packetProcessor.byte_to_int_le(packet.data,0,2) * 0.1)
        # print(steeringAngle)
        print('parsed packet id 018')
        pass

    def _0D4(self, msg: can.Message.data):
        # FL wheel speed
        # FR wheel speed
        # RL wheel speed
        # RR wheel speed
        print('parsed packet id 0D4')
        pass

    def _0D3(self, msg: can.Message.data):
        # unknown
        print('parsed packet id 0D3')
        pass

    def _0D2(self, msg: can.Message.data):
        # unknown
        print('parsed packet id 0D2')
        pass

    def _0D1(self, msg: can.Message.data):
        # brake pos %
        # brake pressure
        print('parsed packet id 0D1')
        pass

    def _0D0(self, msg: can.Message.data):
        # steering angle
        # lat accel
        # long accel
        # combined accel
        # yaw
        print('parsed packet id 0D0')
        pass

    def _282(self, msg: can.Message.data):
        print('parsed packet id 282')
        pass

    def _370(self, msg: can.Message.data):
        print('parsed packet id 370')
        pass

    def _440(self, msg: can.Message.data):
        print('parsed packet id 440')
        pass

    def _361(self, msg: can.Message.data):
        # gear
        print('parsed packet id 361')
        pass

    def _360(self, msg: can.Message.data):
        # coolant temp
        # engine oil temp
        # cruise on off
        # cruise set
        # cruise speed
        print('parsed packet id 360')
        pass

    def _372(self, msg: can.Message.data):
        print('parsed packet id 372')
        pass

    def _63B(self, msg: can.Message.data):
        print('parsed packet id 63B')
        pass

    def _442(self, msg: can.Message.data):
        print('parsed packet id 442')
        pass

    def _375(self, msg: can.Message.data):
        print('parsed packet id 375')
        pass

    def _374(self, msg: can.Message.data):
        print('parsed packet id 374')
        pass

    def _4C8(self, msg: can.Message.data):
        print('parsed packet id 4C8')
        pass

    def _6E1(self, msg: can.Message.data):
        print('parsed packet id 6E1')
        pass

    def _6E2(self, msg: can.Message.data):
        print('parsed packet id 6E2')
        pass

    def _4DD(self, msg: can.Message.data):
        print('parsed packet id 4DD')
        pass

    def _4C3(self, msg: can.Message.data):
        print('parsed packet id 4C3')
        pass

    def _4C1(self, msg: can.Message.data):
        print('parsed packet id 4C1')
        pass

    def _4C6(self, msg: can.Message.data):
        print('parsed packet id 4C6')
        pass

    def unknown(self, msg: can.Message.data):
        print()
        pass
    
    
    commands = {
        324: _144,  322: _142,  321: _141,  320: _140,  342: _156,  338: _152,
        24: _018,  212: _0D4,  323: _0D3,  210: _0D2,  209: _0D1,  208: _0D0,
        642: _282,  880: _370, 1088: _440,  865: _361,  864: _360,  882: _372,
        1595: _63B, 1090: _442,  885: _375,  884: _374, 1224: _4C8, 1761: _6E1,
        1762: _6E2, 1245: _4DD, 1219: _4C3, 1217: _4C1, 1222: _4C6}
