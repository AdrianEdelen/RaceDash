from abc import abstractmethod; import os
import queue; import threading
import time; import can
from can.bus import BusState; from can.interface import Bus
from sys import platform; import re
from textwrap import wrap

"""
The CanNetwork pulls messages off of the bus (or simfile) and puts them into a queue for processing.
"""
#in the future I intend to add timestamp checking to play back messages in real time
class canNetworkInterface:
    def __init__(self, queue:queue.Queue) -> None:
        self.Queue = queue
    @abstractmethod
    def startConnection():
        pass
    @abstractmethod
    def closeConnection():
        pass
    @abstractmethod
    def startRecieveThread():
        pass
    @abstractmethod
    def startSendThread():
        pass
    @abstractmethod
    def recieveMessage():
        pass
    @abstractmethod
    def sendMessage():
        pass
class canCommunication(canNetworkInterface):
    def __init__(self,queue) -> None:
        super().__init__(queue)
        self.bus = None
    def startConnection(self):
        os.system('sudo ip link set can0 type can bitrate 500000')
        os.system('sudo ifconfig can0 up')
        if platform == "linux" or platform == "linux2":
            os.system('sudo ip link set can0 type can bitrate 500000')
            os.system('sudo ifconfig can0 up')
        elif platform == "darwin":
            # OS X
            pass
        elif platform == "win32":
            # Windows...
            pass
        self.bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)
        self.bus.state = BusState.ACTIVE
    def closeConnection(self):
        if platform == "linux" or platform == "linux2":
            os.system('sudo ifconfig can0 down')
        elif platform == "darwin":
            # OS X
            pass
        elif platform == "win32":
            # Windows...
            pass
    def startRecieveThread(self):
        self.workerRec = threading.Thread(target=self.recieveMessage, args=())
        self.workerRec.setDaemon(False)
        self.workerRec.start()
    def startSendThread(self):
        self.workerSend = threading.Thread(target=self.sendMessage, args=())
        self.workerSend.setDaemon(False)
        self.workerSend.start()
    def recieveMessage(self) -> can.Message:
        while True:
            msg = can.Message(self.bus.recv())
            self.Queue.put(msg)
    def sendMessage(self):
        pass
#When loading can-utils log files use this
class simCanCanUtils(canNetworkInterface):
    def __init__(self,queue) -> None:
        super().__init__(queue)
        self.pos = 0
        self.lines = ''
        self.worker = None
    def startConnection(self):
        file = open('resources\candump-2021-10-20_203215.log', 'r')
        self.lines = file.read().splitlines()
    def closeConnection(self):
        #TODO kill the queue
        #TODO kill the thread
        pass
    def startRecieveThread(self):
        self.worker = threading.Thread(target=self.recieveMessage, args=())
        self.worker.setDaemon(False)
        self.worker.start()
    def startSendThread():
        pass
    def recieveMessage(self):
        while True:
            time.sleep(.001)
            #TODO instead of sleeping the thread here, instead get the
            #timestamp and sleep for the appropriate time
            try:
                curPacket = self.lines[self.pos]
                self.pos += 1
            except IndexError:
                print('new loop')
                self.pos = 0
                curPacket = self.lines[self.pos]
                self.pos += 1
            finally:
                packetParts = curPacket.split()
                idAndMessage = packetParts[2].split('#')

                dataBackwards = idAndMessage[1].zfill(16)
                byteList = wrap(dataBackwards, 2)

                data = []
                for b in byteList:
                    data.append(int(b,16))
                
                msg = can.Message()
                msg.arbitration_id = int(idAndMessage[0], 16)
                msg.data = data
                msg.channel = packetParts[1]
                msg.timestamp = float(re.sub(r'[\(\)]', '', packetParts[0]))
                self.Queue.put(msg)
    def sendMessage(self):
        pass