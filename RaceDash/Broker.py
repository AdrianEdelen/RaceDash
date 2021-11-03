

class Broker:

    self.dbConn = psycopg2.connect(dbname='racedash', user='', password='', host='192.168.1.41')
    self.dbCursor = self.dbConn.cursor()
    self.dbCursor.execute("SELECT version()")
            print(self.dbCursor.fetchone()