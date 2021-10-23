import os
import queue
import threading
import time
import can
#from can.interface import Bus

"""The can network operates by starting a thread
   and then queue all of the messages on the network
   the software can then process the messages as it sees fit
   the canSim behaves exactly the same as the real and 
   and can be used to simulate with dummy data or play back 
   real world logs"""
   #in the future I intend to add timestamp checking to play back messages in real time
class canNetworkInterface:
    messageReader = can.BufferedReader
    def startConnection():
        pass
    def closeConnection():
        pass
    def startRecieveThread():
        pass
    def recieveMessage():
        pass
    def sendMessage():
        pass

class canCommunication(canNetworkInterface):
    def __init__(self) -> None:
        super().__init__()
        self.bus = None
        self.messageReader = None

    def startConnection(self):
        #os.system('sudo ip link set can0 type can bitrate 500000')
        #os.system('sudo ifconfig can0 up')
        self.bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)
        self.messageReader  = can.BufferedReader()
        #can.rc['interface'] = 'socketcan'
        #can.rc['channel'] = 'can0'
        #can.rc['bitrate'] = 500000
        #bus = Bus()

        return
    def closeConnection(self):
        os.system('sudo ifconfig can0 down')
        return
    def startRecieveThread(self):
        pass
    def recieveMessage(self):
        pass
    def sendMessage(self):
        pass

class simCanComm(canNetworkInterface):
    def __init__(self) -> None:
        super().__init__()
        self.pos = 0
        self.lines = ''
        self.messageQueue = queue.Queue()
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

    def recieveMessage(self):
        while True:
            #time.sleep(.00001)
            #TODO instead of sleeping the thread here, instead get the
            #timestamp and sleep for the appropriate time
            try:
                curPacket = self.lines[self.pos]
                self.pos += 1
            except IndexError:
                self.pos = 0
                curPacket = self.lines[self.pos]
                self.pos += 1
            finally:
                self.messageQueue.put(curPacket)

    def sendMessage(self):
        pass

    
    
        