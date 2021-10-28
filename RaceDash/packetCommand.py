
from typing import DefaultDict
import can
from packetProcessor import packetProcessor
import car


"""Each method processes the can data differently.
   The methods are mapped to a dict and are called in the 
   packet processing thread

BYTE ORDERING / NAMING
The bytes are reversed to LE 
before they get sent here

 _________________
| 0 1 2 3 4 5 6 7 |
| A B C D E F G H |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

"""
#Warning, a lot of the calculations are empirical, they don't always make sense
class commandDict:

    def _018(car:car, msg: can.Message.data): #24
        
        car._18_C = msg[2]
        car._18_D = msg[3]
        car._18_E = msg[4]
        car._18_F = msg[5]
        car._18_G = msg[6]
        car._18_H = msg[7]
        car.steering_angle_one = round(int.from_bytes([msg[0], msg[1]], 'little') * 0.1, 2)

    def _0D0(car:car, msg: can.Message.data): #208
        car.steering_angle_two = round(int.from_bytes([msg[0], msg[1]], 'little') * 0.1, 2)
        car.yaw_rate = round(int.from_bytes([msg[2], msg[3]], 'little') * -0.286478897, 2)
        car._208_E = msg[4]
        car._208_F = msg[5]
        car.lateral_accel = round(msg[6] * 0.2, 2)
        car.long_accel = round(msg[7] * -0.1, 2)

    def _0D1(car:car, msg: can.Message.data): #209
        car.speed = round(int.from_bytes([msg[0],msg[1]],'little'), 2)
        car.brake_pressure = min(msg[2] / 0.7, 100)
        car._209_D = msg[3]
        car._209_E = msg[4]
        car._209_F = msg[5]
        car._209_G = msg[6]
        car._209_H = msg[7]

    def _0D2(car:car, msg: can.Message.data): #210
        # unknown
        return
    def _0D3(car:car, msg: can.Message.data): #211
        # unknown
        return
    def _0D4(car:car, msg: can.Message.data): #212
        # FL wheel speed
        # FR wheel speed
        # RL wheel speed
        # RR wheel speed
        return
    def _140(car:car, msg: can.Message.data): #dec 320
        #Accelerator Position %
        car.accelerator_position_percent = round(msg[7] / 2.55,2)
        #G / 2.55
        
        # engine rpm
        # clutch pos
        # throttle pos
        # accel pedal on/off
    def _141(car:car, msg: can.Message.data): #321
        return
    def _142(car:car, msg: can.Message.data): #322
        # unknown
        return
    def _144(car:car, msg: can.Message.data): #324
        return 'parsed packet id 144'
    def _152(car:car, msg: can.Message.data): #338
        return
    def _156(car:car, msg:can.Message.data): #342
        return
    def _282(car:car, msg: can.Message.data): #642
        return
    def _360(car:car, msg: can.Message.data): #864
        # coolant temp
        # engine oil temp
        # cruise on off
        # cruise set
        # cruise speed
        return
    def _361(car:car, msg: can.Message.data): #865
        # gear
        return
    def _370(car:car, msg: can.Message.data): #880
        return
    def _372(car:car, msg: can.Message.data): #882
        return
    def _374(car:car, msg: can.Message.data): #884
        return
    def _375(car:car, msg: can.Message.data): #885
        return
    def _440(car:car, msg: can.Message.data): #1088
        return
    def _442(car:car, msg: can.Message.data): #1090
        return
    def _63B(car:car, msg: can.Message.data): #1595
        return
    def _4C1(car:car, msg: can.Message.data): #1217
        return
    def _4C3(car:car, msg: can.Message.data): #1219
        return
    def _4C6(car:car, msg: can.Message.data): #1222
        return
    def _4C8(car:car, msg: can.Message.data): #1224
        return
    def _4DD(car:car, msg: can.Message.data): #1245
        return
    def _6E1(car:car, msg: can.Message.data): #1761
        return
    def _6E2(car:car, msg: can.Message.data): #1762
        return



    def unknown(car:car, msg: can.Message.data):
        return
    
    commands = {
        324: _144,  322: _142,  321: _141,  320: _140,  342: _156,  338: _152,
        24: _018,  212: _0D4,  323: _0D3,  210: _0D2,  209: _0D1,  208: _0D0,
        642: _282,  880: _370, 1088: _440,  865: _361,  864: _360,  882: _372,
        1595: _63B, 1090: _442,  885: _375,  884: _374, 1224: _4C8, 1761: _6E1,
        1762: _6E2, 1245: _4DD, 1219: _4C3, 1217: _4C1, 1222: _4C6, 211: _0D3}
