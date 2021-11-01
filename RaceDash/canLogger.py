
"""
The canlogger spits out the processed data
"""
import queue
import threading
import can


class CanLogger:
    def __init__(self,canQueue, useDB, useFile, useStream, cmds) -> None:
        self.canBusQueue = canQueue
        self.useDB = useDB
        self.useFile = useFile
        self.useStream = useStream
        self.cmds = cmds
        pass

    def startProcessorThread(self):
        self.workerProc = threading.Thread(target=self.calcCanMessage, args=())
        self.workerProc.setDaemon(False)
        self.workerProc.start()
        pass
    
    #probably need to pass in the parent q here. and pass the processed message into our q
    #that way the subclasses can all just pull from the q and 
    def messageToDB(msg):
        #this will format for a db and send to db as configured
        pass
    def messageToFile(msg):
        #this will write to files split by size
        #these files will be local so try to save on space
        pass
    def messageToStream(msg):
        print(msg)
        #this will either be stdout, or some way for the os to just have an
        #open stream.
        #this would be used for a front end on the same device
        pass


    def calcCanMessage(self):
        while True:
            if self.canBusQueue.unfinishedTasks() > 100:
                #self.canBusQueue.clear --- not sure what the method is here
                continue
            msg:can.Message = self.canBusQueue.get(True)
            if msg.arbitration_id in self.cmds:
                msgFunc = self.cmds[msg.arbitration_id]
                msg = msgFunc(self, msg) #message come back as one or multiple values
            else:
                print('Unknown Packet Id: ', msg.arbitration_id)
            
            if self.useDB:
                self.messageToDB(msg)
            if self.useFile:
                self.messageToFile(msg)
            if self.useStream:
                self.messageToStream(msg)

            self.canBusQueue.task_done()

    


