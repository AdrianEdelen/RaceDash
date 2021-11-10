import psycopg2
import configparser

class Broker:
    def __init__(self) -> None:
        Config = configparser.ConfigParser()
        Config.read('/home/pi/RaceDash/RaceDash/RaceDash/config.ini')

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

    def insert(self, msg):
        self.dbCursor.execute("INSERT INTO " + "FRS" + " VALUES (%s, %s, %s)", (msg.timeRecieved, msg.name, msg.magnitude))
        self.dbConn.commit()
    #create
    #read
    #update
    #self.dbCursor.execute("INSERT INTO FRS (Timestamp, Name, Magnitude) VALUES (%s, %s, %s)", (msg.timeRecieved, msg.name, msg.magnitude))
    #self.dbConn.commit()
    #delete


