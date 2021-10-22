import os
import queue
import threading
import time

"""The can network operates by starting a thread
   and then queue all of the messages on the network
   the software can then process the messages as it sees fit
   the canSim behaves exactly the same as the real and 
   and can be used to simulate with dummy data or play back 
   real world logs"""
   #in the future I intend to add timestamp checking to play back messages in real time
class canNetworkInterface:
    
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

    def startConnection():
        os.system('sudo ip link set can0 type can bitrate 500000')
        os.system('sudo ifconfig can0 up')
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

    def startConnection(self):
        file = open('resources\candump-2021-10-20_203215.log', 'r')
        self.lines = file.read().splitlines()

    def closeConnection(self):
        #kill the queue
        #kill the thread
        pass

    def startRecieveThread(self):
        worker = threading.Thread(target=self.recieveMessage, args=(1, self))
        worker.setDaemon()
        worker.start()

    def recieveMessage(self):
        time.time.sleep(.0001)
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

    
    
        