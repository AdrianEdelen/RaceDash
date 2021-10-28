# RaceDash

RaceDash aims to be a complete drop in replacement gauge cluster and radio for your car.

This repository houses the software component of the system.

Using can-bus, RaceDash processes each and every message coming through the car's internal communication bus.

Currently the only supported platform is FT86. Due to the nature of automotive manufacturing, even though the can bus is standard, and OBD-II uses standard PIDs 
we do not always have the luxury of using the standardized message IDs. Therefore additional platforms will require large amounts of reverse engineering to determine 
the contents of each message.

The benefit of using the direct can-bus over OBD-II, is speed and access. RaceDash has direct access to many internal systems and is not limited by the arbitrary rate limits 
set by OBD-II testers.

Another primary goal of RaceDash is to allow alternate control of your vehicle, did you remove the door cards but still want to roll your window down?
Do you want to change the feedback of your electric power steering? these are things we hope to make possible with RaceDash.

RaceDash is use at your own risk, and can be highly dangerous to you or your car if you don't know what you are doing.
