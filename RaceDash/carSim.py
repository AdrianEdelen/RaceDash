

class carSim:
    def __init__(self) -> None:
        self.pos = 0
        self.lines = ''
        

    def loadRaw(self, filepath: str):
        file = open(filepath, 'r')
        self.lines = file.read().splitlines()

    def streamCanData(repeat: bool):
        return

    def getNextmessage(self):
        try:
            curPacket = self.lines[self.pos]
            self.pos += 1
        except IndexError:
            self.pos = 0
            curPacket = self.lines[self.pos]
            self.pos += 1
        finally:
            return curPacket

