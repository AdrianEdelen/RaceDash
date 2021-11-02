
"""CanLogger works through messages in the queue. these messages can come from the bus or anywhere
The logger translates the messages and returns them in a Message data type

After processing, the messages are either sent out on a stream(TBD), written to file, sent to a db,
or any combination of these."""
import queue; import threading; import can; import datetime
class CanLogger:
    def __init__(self,canQueue: queue.Queue, useDB, useFile, useStream, cmds) -> None:
        self.canBusQueue = canQueue
        self.useDB = useDB
        self.useFile = useFile
        self.useStream = useStream
        self.cmds = cmds
    def startProcessorThread(self):
        self.workerProc = threading.Thread(target=self.calcCanMessage, args=())
        self.workerProc.setDaemon(False)
        self.workerProc.start()
    def messageToDB(self, msg):
        #this will format for a db and send to db as configured
        pass
    def messageToFile(self, msg):
        date = datetime.datetime.now()
        logFile = open(f'logs\{date.strftime("%Y-%m-%d %H")}', 'a')
        logFile.write(str(msg) + '\n')
    def messageToStream(self, msg):
        print(msg)
    def calcCanMessage(self):
        while True:
            if self.canBusQueue.unfinished_tasks > 100:
                #not sure if we need to clear the queue out, in theory we could get stuck in a lag state
                #that may be better since we would just wait after the car shuts down and the queue
                #slows down to process the data. better late than never
                continue
            msg:can.Message = self.canBusQueue.get(True)
            if msg.arbitration_id in self.cmds:
                msgFunc = self.cmds[msg.arbitration_id]
                processedMessage = msgFunc(msg) #message come back as one or multiple values
            else:
                print('Unknown Packet Id: ', msg.arbitration_id)
            for message in processedMessage:
                if self.useDB:
                    self.messageToDB(message)
                if self.useFile:
                    self.messageToFile(message)
                if self.useStream:
                    self.messageToStream(message)
            self.canBusQueue.task_done()
