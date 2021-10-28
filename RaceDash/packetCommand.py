
from typing import DefaultDict
import can
import car


"""
Each method processes the can data differently.
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
    #copied from so, needs testing
    def access_bit(data, num):
        base = int(num // 8)
        shift = int(num % 8)
        return (data[base] >> shift) & 0x1


    def _018(car:car, msg: can.Message.data): #24
        
        car.steering_angle_one = round(int.from_bytes([msg[0], msg[1]], 'little') * 0.1, 2)

    def _0D0(car:car, msg: can.Message.data): #208
        car.steering_angle_two = round(int.from_bytes([msg[0], msg[1]], 'little') * 0.1, 2)
        car.yaw_rate = round(int.from_bytes([msg[2], msg[3]], 'little') * -0.286478897, 2)

        car.lateral_accel = round(msg[6] * 0.2, 2)
        car.long_accel = round(msg[7] * -0.1, 2)

    def _0D1(car:car, msg: can.Message.data): #209
        car.speed = round(int.from_bytes([msg[0],msg[1]],'little'), 2)
        car.brake_pressure = min(msg[2] / 0.7, 100)

    def _0D2(car:car, msg: can.Message.data): #210
        # unknown
        car._210 = msg
    def _0D3(car:car, msg: can.Message.data): #211
        # unknown
        car._211 = msg
    def _0D4(car:car, msg: can.Message.data): #212
        car.wheel_speed_FL = int.from_bytes([msg[0], msg[1]], 'little') #0,1
        car.wheel_speed_FR = int.from_bytes([msg[2], msg[3]], 'little') #2,3
        car.wheel_speed_RL = int.from_bytes([msg[4], msg[5]], 'little') #4,5
        car.wheel_speed_RR = int.from_bytes([msg[6], msg[7]], 'little') #6,7
        
    def _140(car:car, msg: can.Message.data): #dec 320
        car.accelerator_position_percent = msg[7] / 2.55
        car.throttle_position = msg[6] / 2.55
        #for engine rpm we need bits from pos:16 through 30
        #this is a nightmare
        # bits = [commandDict.access_bit(msg,i) for i in range(len(msg)*8)]
        # bitsOfInterest = bits[16:30]
        # for b in bitsOfInterest:
        #     b = str(b)

        # bitString = ''.join(bitsOfInterest)
        # car.engine_rpm= int(bitString, 2) #i hate bit fiddling in python
        
        a = True
        # engine rpm
        # clutch pos
        # throttle pos
        # accel pedal on/off
    def _141(car:car, msg: can.Message.data): #321
        car._321 = msg
        
    def _142(car:car, msg: can.Message.data): #322
        car._322 = msg
        # unknown
        
    def _144(car:car, msg: can.Message.data): #324
        car._324 = msg
    def _152(car:car, msg: can.Message.data): #338
        car._338 = msg
    def _156(car:car, msg:can.Message.data): #342
        car._342 = msg
    def _282(car:car, msg: can.Message.data): #642
        car._642 = msg
    def _360(car:car, msg: can.Message.data): #864
        # coolant temp
        # engine oil temp
        # cruise on off
        # cruise set
        # cruise speed
        car._864 = msg
        
    def _361(car:car, msg: can.Message.data): #865
        car._865 = msg
        # gear
        
    def _370(car:car, msg: can.Message.data): #880
        car._880 = msg
        
    def _372(car:car, msg: can.Message.data): #882
        car._882 = msg
        
    def _374(car:car, msg: can.Message.data): #884
        car._884 = msg
        
    def _375(car:car, msg: can.Message.data): #885
        car._885 = msg
        
    def _440(car:car, msg: can.Message.data): #1088
        car._1088 = msg
        
    def _442(car:car, msg: can.Message.data): #1090
        car._1090 = msg
        
    def _63B(car:car, msg: can.Message.data): #1595
        car._1595 = msg
        
    def _4C1(car:car, msg: can.Message.data): #1217
        car._1217 = msg
        
    def _4C3(car:car, msg: can.Message.data): #1219
        car._1219 = msg
        
    def _4C6(car:car, msg: can.Message.data): #1222
        car._1222 = msg
        
    def _4C8(car:car, msg: can.Message.data): #1224
        car._1224 = msg
        
    def _4DD(car:car, msg: can.Message.data): #1245
        car._1245 = msg
        
    def _6E1(car:car, msg: can.Message.data): #1761
        car._1761 = msg
        
    def _6E2(car:car, msg: can.Message.data): #1762
        car._1762 = msg
         
    def unknown(car:car, msg: can.Message.data):
        return
    
    commands = {
        324: _144,  322: _142,  321: _141,  320: _140,  342: _156,  338: _152,
        24: _018,  212: _0D4,  323: _0D3,  210: _0D2,  209: _0D1,  208: _0D0,
        642: _282,  880: _370, 1088: _440,  865: _361,  864: _360,  882: _372,
        1595: _63B, 1090: _442,  885: _375,  884: _374, 1224: _4C8, 1761: _6E1,
        1762: _6E2, 1245: _4DD, 1219: _4C3, 1217: _4C1, 1222: _4C6, 211: _0D3}
