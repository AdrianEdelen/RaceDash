from can.message import Message
from canNetwork import *
from packetCommand import commandDict


class car:
    def __init__(self, canBus: canNetworkInterface) -> None:
        self.canBus = canBus

        #identified values
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
        self.speed = 0
        
        #unidentified values
        self._321 = 0
        self._322 = 0
        self._324 = 0
        self._342 = 0
        self._642 = 0
        self._864 = 0
        self._865 = 0
        self._880 = 0
        self._882 = 0
        self._884 = 0
        self._885 = 0
        self._885 = 0
        self._1088 = 0
        self._1090 = 0
        self._1595 = 0
        self._1217 = 0
        self._1219 = 0
        self._1222 = 0
        self._1224 = 0
        self._1245 = 0
        self._1761 = 0
        self._1762 = 0

    def __str__(self) -> str:
        return f'''\
*************************************************************************************
accel pedal %........: {self.accelerator_position_percent}| brake pos %............: {self.brake_position_percent}
steering angle 1.....: {self.steering_angle_one}| speed MPH..............: {self.speed_mph}
engine RPM...........: {self.engine_rpm}| coolant Temp...........: {self.coolant_temp}
engine oil temp......: {self.engine_oil_temp}| brake Pressure.........: {self.brake_pressure}
clutch position......: {self.clutch_position}| gear 1.................: {self.gear_one}
throttle position....: {self.throttle_position}| lateral accel..........: {self.lateral_accel}
long accel...........: {self.long_accel}| combined accel.........: {self.combined_accel}
yaw rate.............: {self.yaw_rate}| wheel speed FL.........: {self.wheel_speed_FL}
wheel speed FR.......: {self.wheel_speed_FR}| wheel speed RL.........: {self.wheel_speed_RL}
wheel speed RR.......: {self.wheel_speed_RR}| steering anglw 2.......: {self.steering_angle_two}
accel pedal (on/off).: {self.accel_pedal_on_off}| cruise control (on/off): {self.cruise_control_on_off}
cruise control set...: {self.cruise_control_set}| cruise control speed...: {self.cruise_speed}
gear 2...............: {self.gear_two}| speed: {self.speed}
321..................: {self._321} |322..................: {self._322}
324..................: {self._324} |342..................: {self._342}
642..................: {self._642} |864..................: {self._864}
865..................: {self._865} |880..................: {self._880}
882..................: {self._882} |884..................: {self._884}
885..................: {self._885} |1088.................: {self._1088}
1090.................: {self._1090} |1595.................: {self._1595}
1217.................: {self._1217} |1219.................: {self._1219}
1222.................: {self._1222} |1224.................: {self._1224}
1245.................: {self._1245} |1761.................: {self._1761}
1762.................: {self._1762}

Packets Behind: {self.canBus.Queue.unfinished_tasks}
'''
    #we want to block here to honor the order of the can bus
    #however, we may add a timeout at some point to drop a message
    #probably just exit the calc if a new packet comes in
    #on the other side, we may be able to catch up on easy to process packets
    #so it may be best to drop a packet if the q is greater than n packets
    def startProcessorThread(self):
        self.workerProc = threading.Thread(target=self.calcCanMessage, args=())
        self.workerProc.setDaemon(False)
        self.workerProc.start()
        pass

    def dispose(self):
        self.canBus.closeConnection()

    def calcCanMessage(self):
        while True:
            
            msg:can.Message = self.canBus.Queue.get(True)
            msgId = msg.arbitration_id
            msg.data
            if msgId in commandDict.commands:
                msgFunc = commandDict.commands[msgId]
                msgFunc(self, msg.data)
            else:
                print('Unknown Packet Id: ', msgId)
            self.canBus.Queue.task_done()




        

            

