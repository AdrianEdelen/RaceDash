import psycopg2

class Broker:
    def __init__(self) -> None:
        self.dbConn = psycopg2.connect(dbname='racedash', user='admin', password='Add!ctive!@', host='192.168.1.41')
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute("SELECT version()")
        print(self.dbCursor.fetchone())
        
    #create
    #read
    #update
    #self.dbCursor.execute("INSERT INTO FRS (Timestamp, Name, Magnitude) VALUES (%s, %s, %s)", (msg.timeRecieved, msg.name, msg.magnitude))
    #self.dbConn.commit()
    #delete


