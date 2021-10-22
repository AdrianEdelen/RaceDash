import threading
import queue

class carSim:
    def __init__(self) -> None:
        self.pos = 0
        self.lines = ''
        self.messageQueue = queue.Queue()

    def loadRaw(self, filepath: str):
        file = open(filepath, 'r')
        self.lines = file.read().splitlines()

    def streamCanData(repeat: bool):
        return

    def getNextMessage(self):
        try:
            curPacket = self.lines[self.pos]
            self.pos += 1
        except IndexError:
            self.pos = 0
            curPacket = self.lines[self.pos]
            self.pos += 1
        finally:
            self.messageQueue.put(curPacket)

    def getMessageTask(self):
        threading.Timer(.001,self.getNextMessage()).start()
        