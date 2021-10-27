
from typing import DefaultDict
import can
from packetProcessor import packetProcessor
import car

"""Each method processes the can data differently.
   The methods are mapped to a dict and are called in the 
   packet processing thread
"""

#Warning, a lot of the calculations are empirical, they don't always make sense
class commandDict:
    
    def _144(car:car, msg: can.Message.data):
        return 'parsed packet id 144'

    def _142(car:car, msg: can.Message.data):
        # unknown
        return

    def _141(car:car, msg: can.Message.data):
        return
        
    def _140(car:car, msg: can.Message.data):
        #Accelerator Position %
        car.accelerator_position_percent = msg[0] / 2.55
        #G / 2.55
        # engine rpm
        # clutch pos
        # throttle pos
        # accel pedal on/off

    def _156(car:car, msg:can.Message.data):
        return

    def _152(car:car, msg: can.Message.data):
        return

    def _018(car:car, msg: can.Message.data):
        # Steering Angle
        #instead of this
        # car.steering_angle_one=  round(packetProcessor.byte_to_int_le(msg, 0, 2) * 0.1, 4)
        #possibly something like this. we can also get the byte letters at the beginning of the
        
        intval = round(int.from_bytes([msg[7], msg[6]], 'little') * 0.1, 2)
        print (intval)
        car.steering_angle_one = intval * 0.1

    def _0D4(car:car, msg: can.Message.data):
        # FL wheel speed
        # FR wheel speed
        # RL wheel speed
        # RR wheel speed
        return

    def _0D3(car:car, msg: can.Message.data):
        # unknown
        return

    def _0D2(car:car, msg: can.Message.data):
        # unknown
        return

    def _0D1(car:car, msg: can.Message.data):
        # brake pos %
        # brake pressure
        return

    def _0D0(car:car, msg: can.Message.data):
        # steering angle
        # lat accel
        # long accel
        # combined accel
        # yaw
        return

    def _282(car:car, msg: can.Message.data):
        return

    def _370(car:car, msg: can.Message.data):
        return

    def _440(car:car, msg: can.Message.data):
        return

    def _361(car:car, msg: can.Message.data):
        # gear
        return

    def _360(car:car, msg: can.Message.data):
        # coolant temp
        # engine oil temp
        # cruise on off
        # cruise set
        # cruise speed
        return

    def _372(car:car, msg: can.Message.data):
        return

    def _63B(car:car, msg: can.Message.data):
        return

    def _442(car:car, msg: can.Message.data):
        return

    def _375(car:car, msg: can.Message.data):
        return

    def _374(car:car, msg: can.Message.data):
        return

    def _4C8(car:car, msg: can.Message.data):
        return

    def _6E1(car:car, msg: can.Message.data):
        return

    def _6E2(car:car, msg: can.Message.data):
        return

    def _4DD(car:car, msg: can.Message.data):
        return

    def _4C3(car:car, msg: can.Message.data):
        return

    def _4C1(car:car, msg: can.Message.data):
        return

    def _4C6(car:car, msg: can.Message.data):
        return
    
    def _0D3(car:car, msg: can.Message.data):
        return

    def unknown(car:car, msg: can.Message.data):
        return
    
    commands = {
        324: _144,  322: _142,  321: _141,  320: _140,  342: _156,  338: _152,
        24: _018,  212: _0D4,  323: _0D3,  210: _0D2,  209: _0D1,  208: _0D0,
        642: _282,  880: _370, 1088: _440,  865: _361,  864: _360,  882: _372,
        1595: _63B, 1090: _442,  885: _375,  884: _374, 1224: _4C8, 1761: _6E1,
        1762: _6E2, 1245: _4DD, 1219: _4C3, 1217: _4C1, 1222: _4C6, 211: _0D3}
