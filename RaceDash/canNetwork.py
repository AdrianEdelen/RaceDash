import os
import can
import asyncio
"""
The CanNetwork pulls messages off of the bus (or simfile) and puts them into a queue for processing.
"""
class canCommunication():
    def __init__(self, device) -> None:
        self.Device = device
        self.notifier: can.Notifier = None
        self.bus: can.interface.Bus = None
        self.asyncBufferedReader = None
        #TODO: Properly set up multiple can devices (should be scalable)
        os.system(f'sudo ip link set {self.Device} type can bitrate 500000')
        os.system(f'sudo ifconfig {self.Device} up')    
        bus: can.BusABC = can.interface.ThreadSafeBus(bustype='socketcan', channel='can0', bitrate=500000)
        self.asyncBufferedReader = can.AsyncBufferedReader(self.bus, 0.1)
        loop = asyncio.get_event_loop()
        self.notifier = can.Notifier(bus, self.asyncBufferdReader, loop=loop)
    def calcCanMessage(self, msg): 
            if msg.arbitration_id in self.cmds:
                msgFunc = self.cmds[msg.arbitration_id]
                processedMessage = msgFunc(msg)
            else: #unknown packet
                processedMessage = TranslatedMessage(msg.timestamp, msg.arbitration_id ,msg.data),        
            return processedMessage
    def closeConnection(self):
        os.system('sudo ifconfig can0 down')

"""Message is a single translated piece of data from the can bus"""
class TranslatedMessage():   
    def __init__(self, timeReceived: float, name: str, magnitude: str):
        self.timeReceived = round(timeReceived,3)
        self.name = name
        self.magnitude = magnitude