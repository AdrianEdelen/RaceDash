
from typing import DefaultDict
import can
from packetProcessor import packetProcessor
import car

"""Each method processes the can data differently.
   The methods are mapped to a dict and are called in the 
   packet processing thread
"""

class commandDict:
    
    def _144(car:car.car, msg: can.Message.data):
        return 'parsed packet id 144'

    def _142(car:car.car, msg: can.Message.data):
        # unknown
        print('parsed packet id 142')
        pass

    def _141(car:car.car, msg: can.Message.data):
        print('parsed packet id 141')
        pass

    def _140(car:car.car, msg: can.Message.data):
        #Accelerator Position %
        car.accelerator_position_percent = msg[0] / 2.55
        #G / 2.55
        # engine rpm
        # clutch pos
        # throttle pos
        # accel pedal on/off
        print('parsed packet id 140')
        pass

    def _156(car:car.car, msg:can.Message.data):
        
        print('parsed packet id 156')
        pass

    def _152(car:car.car, msg: can.Message.data):
        print('parsed packet id 152')
        pass

    def _018(car:car.car, msg: can.Message.data):
        # Steering Angle
        car.steering_angle_one=  round(packetProcessor.byte_to_int_le(msg, 0, 2) * 0.1, 4)

    def _0D4(car:car.car, msg: can.Message.data):
        # FL wheel speed
        # FR wheel speed
        # RL wheel speed
        # RR wheel speed
        print('parsed packet id 0D4')
        pass

    def _0D3(car:car.car, msg: can.Message.data):
        # unknown
        print('parsed packet id 0D3')
        pass

    def _0D2(car:car.car, msg: can.Message.data):
        # unknown
        print('parsed packet id 0D2')
        pass

    def _0D1(car:car.car, msg: can.Message.data):
        # brake pos %
        # brake pressure
        print('parsed packet id 0D1')
        pass

    def _0D0(car:car.car, msg: can.Message.data):
        # steering angle
        # lat accel
        # long accel
        # combined accel
        # yaw
        print('parsed packet id 0D0')
        pass

    def _282(car:car.car, msg: can.Message.data):
        print('parsed packet id 282')
        pass

    def _370(car:car.car, msg: can.Message.data):
        print('parsed packet id 370')
        pass

    def _440(car:car.car, msg: can.Message.data):
        print('parsed packet id 440')
        pass

    def _361(car:car.car, msg: can.Message.data):
        # gear
        print('parsed packet id 361')
        pass

    def _360(car:car.car, msg: can.Message.data):
        # coolant temp
        # engine oil temp
        # cruise on off
        # cruise set
        # cruise speed
        print('parsed packet id 360')
        pass

    def _372(car:car.car, msg: can.Message.data):
        print('parsed packet id 372')
        pass

    def _63B(car:car.car, msg: can.Message.data):
        print('parsed packet id 63B')
        pass

    def _442(car:car.car, msg: can.Message.data):
        print('parsed packet id 442')
        pass

    def _375(car:car.car, msg: can.Message.data):
        print('parsed packet id 375')
        pass

    def _374(car:car.car, msg: can.Message.data):
        print('parsed packet id 374')
        pass

    def _4C8(car:car.car, msg: can.Message.data):
        print('parsed packet id 4C8')
        pass

    def _6E1(car:car.car, msg: can.Message.data):
        print('parsed packet id 6E1')
        pass

    def _6E2(car:car.car, msg: can.Message.data):
        print('parsed packet id 6E2')
        pass

    def _4DD(car:car.car, msg: can.Message.data):
        print('parsed packet id 4DD')
        pass

    def _4C3(car:car.car, msg: can.Message.data):
        print('parsed packet id 4C3')
        pass

    def _4C1(car:car.car, msg: can.Message.data):
        print('parsed packet id 4C1')
        pass

    def _4C6(car:car.car, msg: can.Message.data):
        print('parsed packet id 4C6')
        pass

    def unknown(car:car.car, msg: can.Message.data):
        print()
        pass
    
    
    commands = {
        324: _144,  322: _142,  321: _141,  320: _140,  342: _156,  338: _152,
        24: _018,  212: _0D4,  323: _0D3,  210: _0D2,  209: _0D1,  208: _0D0,
        642: _282,  880: _370, 1088: _440,  865: _361,  864: _360,  882: _372,
        1595: _63B, 1090: _442,  885: _375,  884: _374, 1224: _4C8, 1761: _6E1,
        1762: _6E2, 1245: _4DD, 1219: _4C3, 1217: _4C1, 1222: _4C6}
