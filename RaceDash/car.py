

class car:
    def __init__(self, canNetworkInterface) -> None:
        self.canNetworkInterface = canNetworkInterface
        
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
