import re
from textwrap import wrap

class packet:
    def __init__(self, device: str, id: str, data: str, timeStamp: float) -> None:
        self.device = device
        self.id = id
        self.data = data
        self.timeStamp = timeStamp

class packetProcessor:

    def process_packet_string(rawData):
        packetParts = rawData.split()
        timeStamp =float(re.sub(r'[\(\)]', '', packetParts[0]))
        device = packetParts[1]
        idAndMessage = packetParts[2].split('#')
        id = int(idAndMessage[0], 16)
        data = idAndMessage[1].zfill(16)
        byteList = wrap(data, 2)
        bArr = []
        for b in byteList:
            bArr.append(int(b,16))
        return packet(device, id, bArr, timeStamp)
       

    #This is hacky
    #slim shady voice -Something's wrong and I can feel it.
    #i think this needs to go away, and instead we will just get bytes as we see fit
    #for ex. instead of btie 0,2
    #we will just get byte 7 and byte 8 and & them together.
    #see id:018
    def byte_to_int_le(data: bytearray, startBytePos: int, bytesToMergePos: int) -> int:
        newList = []
        
        for startBytePos in range(bytesToMergePos):
            newList.append(data[-(bytesToMergePos - startBytePos)]) 
        a = int.from_bytes(newList, "big")
        return  a


    #since we are working with individual bytes very often, it can be more
    #pleasant to read if the bytes are 'named'
    #another addition is since our data can be UP TO 8 bytes long, but may be less
    #we can check that when we get the byte here to keep the calculation simpler
    def getByteA(data: bytearray):
        if len(data) > 0:
            return data[0]
        else:
            return 0
        
    def getByteB(data: bytearray):
        if len(data) > 1:
            return data[1]
        else:
            return 0
        
    def getByteC(data: bytearray):
        if len(data) > 2:
            return data[2]
        else:
            return 0
        
    def getByteD(data: bytearray):
        if len(data) > 3:
            return data[3]
        else:
            return 0
        
    def getByteE(data: bytearray):
        if len(data) > 4:
            return data[4]
        else:
            return 0
        
    def getByteF(data: bytearray):
        if len(data) > 5:
            return data[5]
        else:
            return 
        
    def getByteG(data: bytearray):
        if len(data) > 6:
            return data[6]
        else:
            return 0
        
    def getByteH(data: bytearray):
        if len(data) > 7:
            return data[7]
        else:
            return 0
        
    
