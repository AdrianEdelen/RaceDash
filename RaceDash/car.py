from can.message import Message
from canNetwork import *
from packetCommand import *

class car:
    def __init__(self, canBus: canNetworkInterface) -> None:
        self.canBus = canBus
        
        

        self.accelerator_position_percent = 0
        self.brake_position_percent = 0
        self.steering_angle_one = 0
        self.speed_mph = 0
        self.engine_rpm = 0
        self.coolant_temp = 0
        self.engine_oil_temp = 0
        self.brake_pressure = 0
        self.clutch_position = 0
        self.gear_one = 0
        self.throttle_position = 0
        self.lateral_accel = 0
        self.long_accel = 0
        self.combined_accel = 0
        self.yaw_rate = 0
        self.wheel_speed_FL = 0
        self.wheel_speed_FR = 0
        self.wheel_speed_RL = 0
        self.wheel_speed_RR = 0
        self.steering_angle_two = 0
        self.accel_pedal_on_off = 0
        self.cruise_control_on_off = 0
        self.cruise_control_set = 0
        self.cruise_speed = 0
        self.gear_two = 0

    def __str__(self) -> str:
        return f'''\
***********************************************
accel pedal %..........: {self.accelerator_position_percent}
brake pos %............: {self.brake_position_percent}
steering angle 1.......: {self.steering_angle_one}
speed MPH..............: {self.speed_mph}
engine RPM.............: {self.engine_rpm}
coolant Temp...........: {self.coolant_temp}
engine oil temp........: {self.engine_oil_temp}
brake Pressure.........: {self.brake_pressure}
clutch position........: {self.clutch_position}
gear 1.................: {self.gear_one}
throttle position......: {self.throttle_position}
lateral accel..........: {self.lateral_accel}
long accel.............: {self.long_accel}
combined accel.........: {self.combined_accel}
yaw rate...............: {self.yaw_rate}
wheel speed FL.........: {self.wheel_speed_FL}
wheel speed FR.........: {self.wheel_speed_FR}
wheel speed RL.........: {self.wheel_speed_RL}
wheel speed RR.........: {self.wheel_speed_RR}
steering anglw 2.......: {self.steering_angle_two}
accel pedal (on/off)...: {self.accel_pedal_on_off}
cruise control (on/off): {self.cruise_control_on_off}
cruise control set.....: {self.cruise_control_set}
cruise control speed...: {self.cruise_speed}
gear 2.................: {self.gear_two}
'''

        pass
        

    #as i get more comfortable with threading
    #the goal here is to start thread to process the packet and then kill it,
    #ideally, this means that we don't have to block or get behind on a particularly difficult
    #calculation
    def startProcessorThread(self):
        self.workerProc = threading.Thread(target=self.calcCanMessage, args=())
        self.workerProc.setDaemon(False)
        self.workerProc.start()
        pass

    def dispose(self):
        self.canBus.closeConnection()

    def calcCanMessage(self):
        msg:can.Message = self.canBus.Queue.get(True)
        msgId = msg.arbitration_id
        msgData = msg.data
        #need to time this and find out what messages come the most
        #the other way to speed it up may be to apply some multi level bit masks
        #that can potentially change the ifelse, to more of a binary search
        if msgId == 324:
            pass
        if msgId == 322:
            pass
        if msgId == 321:
            pass
        if msgId == 320:
            pass
        if msgId == 342:
            pass
        if msgId == 338:
            pass
        if msgId == 24:
            #steering angle

            pass
        if msgId == 212:
            pass
        if msgId == 323:
            pass
        if msgId == 210:
            pass
        if msgId == 209:
            pass
        if msgId == 208:
            pass
        if msgId == 642:
            pass
        if msgId == 880:
            pass
        if msgId == 1088:
            pass
        if msgId == 865:
            pass
        if msgId == 864:
            pass
        if msgId == 882:
            pass
        if msgId == 1595:
            pass
        if msgId == 1090:
            pass
        if msgId == 885:
            pass
        if msgId == 884:
            pass
        if msgId == 1224:
            pass
        if msgId == 1761:
            pass
        if msgId == 1762:
            pass
        if msgId == 1245:
            pass
        if msgId == 1219:
            pass
        if msgId == 1217:
            pass
        if msgId == 1222:
            pass
        else:
            print('unknown ID: ', msgId)



        

            

