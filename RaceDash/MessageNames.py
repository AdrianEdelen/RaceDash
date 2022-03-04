from enum import Enum
class MessageNames(Enum):
    READY = "ready", "I'm ready to do whatever is needed"
    ERROR = "error", "Something went wrong here"
    SteeringAngleOne = "Steering Angle One"
    SteeringAngleTwo = "Steering Angle Two"
    YawRate = "Yaw Rate"
    LateralAccel = "Lateral Acceleration"
    LongAccel = "Longitudinal Acceleration"
    Speed = "Speed"
    BrakePressure = "Brake Pressure"
    WheelSpeedFL = "Front Left Wheel Speed"
    WheelSpeedFR = "Front Right Wheel Speed"
    WheelSpeedRL = "Rear Left Wheel Speed"
    WheelSpeedRR = "Rear Right Wheel Speed"
    AccelPositionPercent = "Accelerator Position Percent"
    ThrottlePosition = "Throttle Position"

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, description: str = None):
        self._description_ = description

    def __str__(self):
        return self.value

    # this makes sure that the description is read-only
    @property
    def description(self):
        return self._description_
