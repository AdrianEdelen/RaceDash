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
        id = idAndMessage[0]
        data = idAndMessage[1].zfill(16)
        return packet(device, id, data, timeStamp)
       

    def byte_to_int_le(data: str, startBytePos: int, bytesToMergePos: int) -> int:
        byteList = wrap(data, 2)
        newList = []
        for startBytePos in range(bytesToMergePos):
            newList.append(byteList[-(bytesToMergePos - startBytePos)])
        return int(''.join(newList), 16)

