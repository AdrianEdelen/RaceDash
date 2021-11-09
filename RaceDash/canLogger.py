
"""CanLogger works through messages in the queue. these messages can come from the bus or anywhere
The logger translates the messages and returns them in a Message data type

After processing, the messages are either sent out on a stream(TBD), written to file, sent to a db,
or any combination of these."""
import queue
import threading
import can
import datetime
from can.message import Message
import psycopg2
from RaceDash.commandDict import commmandDict
from message import TranslatedMessage
import requests
import api
import configparser

class CanLogger:
    def __init__(self,canQueue: queue.Queue) -> None:
        self.canBusQueue = canQueue

        Config = configparser.ConfigParser()
        Config.read('/home/pi/RaceDash/RaceDash/RaceDash/config.ini')
        self.useDB = Config.getboolean('Config', 'UseDatabase'), 
        self.useFile = Config.getboolean('Config', 'UseFile'),
        self.useStream = Config.getboolean('Config', 'UseStream'), 
        self.cmds = commmandDict.commmandDict(Config.get('Config', 'Car')).car
        if self.useDB:
            #prepare DB
            dbName = Config.get('Database', 'DBName')
            dbUser = Config.get('Database', 'DBUser')
            dbPass = Config.get('Database', 'DBPass')
            dbHost = Config.get('Database', 'DBHost')

            self.dbConn = psycopg2.connect(dbname=dbName, user=dbUser, password=dbPass, host=dbHost)
            self.dbCursor = self.dbConn.cursor()
            self.dbCursor.execute("SELECT version()")
            if self.dbCursor.fetchone()[0] == any:
                print("Database connected")
            else:
                print("Database not connected")

        if self.useFile:
            #prepare file
            pass
        if self.useStream:
            #prepare stream
            pass

    def startProcessorThread(self):
        self.workerProc = threading.Thread(target=self.calcCanMessage, args=())
        self.workerProc.setDaemon(False)
        self.workerProc.start()
    def messageToDB(self, msg:TranslatedMessage):
        self.dbCursor.execute("INSERT INTO FRS (Timestamp, Name, Magnitude) VALUES (%s, %s, %s)", (msg.timeRecieved, msg.name, msg.magnitude))
        self.dbConn.commit()
    def messageToFile(self, msg):
        date = datetime.datetime.now()
        logFile = open(f'logs\{date.strftime("%Y-%m-%d %H")}', 'a')
        logFile.write(str(msg) + '\n')
    def messageToStream(self, msg):
        print(msg)
    def calcCanMessage(self):
        while True:
            #if self.canBusQueue.unfinished_tasks > 100:
                #not sure if we need to clear the queue out, in theory we could get stuck in a lag state
                #that may be better since we would just wait after the car shuts down and the queue
                #slows down to process the data. better late than never
                #continue
            msg:can.Message = self.canBusQueue.get(True)
            if msg.arbitration_id in self.cmds:
                msgFunc = self.cmds[msg.arbitration_id]
                processedMessage = msgFunc(msg) #message come back as one or multiple values
                #api.PutSingleFrame.put(processedMessage)
            else: #unknown packet
                processedMessage = TranslatedMessage(msg.timestamp, msg.arbitration_id ,msg.data),
            for msgSingle in processedMessage:
                if self.useDB:
                    self.messageToDB(msgSingle)
                #TODO: push to ui
                #TODO: push to file
                #TODO: push to stream
            self.canBusQueue.task_done()
            if self.canBusQueue.unfinished_tasks != 0:
                print(f"{datetime.datetime.now()}: unfinished tasks: {self.canBusQueue.unfinished_tasks}")
