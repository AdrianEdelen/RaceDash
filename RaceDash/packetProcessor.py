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
    def byte_to_int_le(data: bytearray, startBytePos: int, bytesToMergePos: int) -> int:
        newList = []
        
        for startBytePos in range(bytesToMergePos):
            newList.append(data[-(bytesToMergePos - startBytePos)])
        
        a = int.from_bytes(newList, "big")
        return  a



