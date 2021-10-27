from abc import abstractmethod
import os
import queue
import threading
import time
import can
from can.bus import BusState
from can.interface import Bus
from sys import platform

from packetProcessor import packetProcessor



"""
The can network operates by starting a thread and then queue all of 
the messages on the network the software can then process the messages 
as it sees fit the canSim behaves exactly the same as the real and 
and can be used to simulate with dummy data or play back real world logs
"""
#in the future I intend to add timestamp checking to play back messages in real time
class canNetworkInterface:

    def __init__(self) -> None:
        self.Queue = queue.Queue()
    

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
    def __init__(self) -> None:
        super().__init__()
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


#This implementation is outdated, it is based on the string that can-utils logs
#we will be making our own logs that is conducive to our style
#Deprecated
class simCanCommOld(canNetworkInterface):
    def __init__(self) -> None:
        super().__init__()
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
                pckt = packetProcessor.process_packet_string(curPacket)
                msg = can.Message()
                msg.arbitration_id = pckt.id
                msg.data = pckt.data
                msg.channel = pckt.device
                msg.timestamp = pckt.timeStamp
                self.Queue.put(msg)
                

    def sendMessage(self):
        pass

    
    
        