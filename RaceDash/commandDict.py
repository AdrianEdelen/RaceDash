import can
from canNetwork import TranslatedMessage
from MessageNames import MessageNames


"""
This is the command dictionary for a 2013 Scion FRS
Each car is different.
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
class FRSCommands:
    #copied from so, needs testing
    def access_bit(data, num):
        base = int(num // 8)
        shift = int(num % 8)
        return (data[base] >> shift) & 0x1

    def _018(msg: can.Message): #24
 
        translatedMessage = TranslatedMessage(msg.timestamp, MessageNames.SteeringAngleOne, round(int.from_bytes([msg.data[0], msg.data[1]], 'little') * 0.1, 2))
        return translatedMessage,

    def _0D0(msg: can.Message): #208
        steering_angle_two = TranslatedMessage(msg.timestamp, MessageNames.SteeringAngleTwo, round(int.from_bytes([msg.data[0], msg.data[1]], 'little') * 0.1, 2))
        yaw_rate = TranslatedMessage(msg.timestamp,MessageNames.YawRate,round(int.from_bytes([msg.data[2], msg.data[3]], 'little') * -0.286478897, 2))

        lateral_accel = TranslatedMessage(msg.timestamp,MessageNames.LateralAccel,round(msg.data[6] * 0.2, 2))
        long_accel = TranslatedMessage(msg.timestamp,MessageNames.LongAccel,round(msg.data[7] * -0.1, 2))
        return steering_angle_two, yaw_rate, lateral_accel, long_accel


    def _0D1(msg: can.Message): #209
        speed = TranslatedMessage(msg.timestamp,MessageNames.Speed,round(int.from_bytes([msg.data[0],msg.data[1]],'little'), 2))
        brake_pressure = TranslatedMessage(msg.timestamp,MessageNames.BrakePressure,min(msg.data[2] / 0.7, 100))

        return speed, brake_pressure
    
    def _0D2(msg: can.Message): #210
        # unknown
        return TranslatedMessage(msg.timestamp, '210', msg.data),
    
    def _0D3(msg: can.Message): #211
        # unknown
        return TranslatedMessage(msg.timestamp, '211', msg.data),
    
    def _0D4(msg: can.Message): #212
        wheel_speed_FL = TranslatedMessage(msg.timestamp,MessageNames.WheelSpeedFL,int.from_bytes([msg.data[0], msg.data[1]], 'little')) #0,1
        wheel_speed_FR = TranslatedMessage(msg.timestamp,MessageNames.WheelSpeedFR,int.from_bytes([msg.data[2], msg.data[3]], 'little')) #2,3
        wheel_speed_RL = TranslatedMessage(msg.timestamp,MessageNames.WheelSpeedRL,int.from_bytes([msg.data[4], msg.data[5]], 'little')) #4,5
        wheel_speed_RR = TranslatedMessage(msg.timestamp,MessageNames.WheelSpeedRR,int.from_bytes([msg.data[6], msg.data[7]], 'little')) #6,7
        return wheel_speed_FL, wheel_speed_FR, wheel_speed_RL, wheel_speed_RR
    
    def _140(msg: can.Message): #dec 320
        accelerator_position_percent = TranslatedMessage(msg.timestamp,MessageNames.AccelPositionPercent, (msg.data[7] / 2.55))
        throttle_position = TranslatedMessage(msg.timestamp,MessageNames.ThrottlePosition,msg.data[6] / 2.55)
        #for engine rpm we need bits from pos:16 through 30
        #this is a nightmare
        # bits = [commandDict.access_bit(msg,i) for i in range(len(msg)*8)]
        # bitsOfInterest = bits[16:30]
        # for b in bitsOfInterest:
        #     b = str(b)

        # bitString = ''.join(bitsOfInterest)
        # engine_rpm= int(bitString, 2) #i hate bit fiddling in python
        
        a = True
        # engine rpm
        # clutch pos
        # throttle pos
        # accel pedal on/off
        return accelerator_position_percent, throttle_position
    
    def _141(msg: can.Message): #321
        return TranslatedMessage(msg.timestamp,'321',msg.data),
        
    def _142(msg: can.Message): #322
        return TranslatedMessage(msg.timestamp,'322',msg.data),
  
    def _144(msg: can.Message): #324
        return TranslatedMessage(msg.timestamp,'324',msg.data),
    
    def _152(msg: can.Message): #338
        return TranslatedMessage(msg.timestamp,'338',msg.data),
    
    def _156(msg:can.Message): #342
        return TranslatedMessage(msg.timestamp,'342',msg.data),
    
    def _282(msg: can.Message): #642
        return TranslatedMessage(msg.timestamp,'642',msg.data),
    
    def _360(msg: can.Message): #864
        # coolant temp
        # engine oil temp
        # cruise on off
        # cruise set
        # cruise speed
        return TranslatedMessage(msg.timestamp,'864',msg.data),
        
    def _361(msg: can.Message): #865
        # gear
        return TranslatedMessage(msg.timestamp,'865',msg.data),
        
    def _370(msg: can.Message): #880
        return TranslatedMessage(msg.timestamp,'880',msg.data),
        
    def _372(msg: can.Message): #882
        return TranslatedMessage(msg.timestamp,'882',msg.data),
        
    def _374(msg: can.Message): #884
        return TranslatedMessage(msg.timestamp,'884',msg.data),
        
    def _375(msg: can.Message): #885
        return TranslatedMessage(msg.timestamp,'885',msg.data),
        
    def _440(msg: can.Message): #1088
        return TranslatedMessage(msg.timestamp,'1088',msg.data),
        
    def _442(msg: can.Message): #1090
        return TranslatedMessage(msg.timestamp,'1090',msg.data),
        
    def _63B(msg: can.Message): #1595
        return TranslatedMessage(msg.timestamp,'1595',msg.data),
        
    def _4C1(msg: can.Message): #1217
        return TranslatedMessage(msg.timestamp,'1217',msg.data),
        
    def _4C3(msg: can.Message): #1219
        return TranslatedMessage(msg.timestamp,'1219',msg.data),
        
    def _4C6(msg: can.Message): #1222
        return TranslatedMessage(msg.timestamp,'1222',msg.data),
        
    def _4C8(msg: can.Message): #1224
        return TranslatedMessage(msg.timestamp,'1224',msg.data),
        
    def _4DD(msg: can.Message): #1245
        return TranslatedMessage(msg.timestamp,'1245',msg.data),
        
    def _6E1(msg: can.Message): #1761
        return TranslatedMessage(msg.timestamp,'1761',msg.data),
        
    def _6E2(msg: can.Message): #1762
        return TranslatedMessage(msg.timestamp,'1762',msg.data),
         
    def unknown(msg: can.Message):
        return TranslatedMessage(msg.timestamp,'unknown' + msg.id, msg.data),
    
    commands = {
        324: _144,  322: _142,  321: _141,  320: _140,  342: _156,  338: _152,
        24: _018,  212: _0D4,  323: _0D3,  210: _0D2,  209: _0D1,  208: _0D0,
        642: _282,  880: _370, 1088: _440,  865: _361,  864: _360,  882: _372,
        1595: _63B, 1090: _442,  885: _375,  884: _374, 1224: _4C8, 1761: _6E1,
        1762: _6E2, 1245: _4DD, 1219: _4C3, 1217: _4C1, 1222: _4C6, 211: _0D3}

class MatrixCommands:

    commands = {}

class TCCommands:

    commands = {}

class commmandDict:
    def __init__(self, car) -> None:
        self.car = self.carDict[car]
        pass
    carDict = {
        'FRS': FRSCommands.commands,
        'Matrix': MatrixCommands.commands,
        'TC': TCCommands.commands}