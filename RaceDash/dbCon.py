from logging import exception
import psycopg2

from canNetwork import TranslatedMessage

#postgres
#CRUD

#maybe this script/tool should only be able to Add

#tables
#translatedMSG


#write to disk first
#insert to db when connected
#once commited and confirmed delete from disk

class db:
    def __init__(self) -> None:
        self.connected = False

        try:
            self.con = psycopg2.connect(database="racedash",user="admin", password="admin", host="192.168.1.41", port="23543")
            self.cur = self.con.cursor()
            self.connected = True
        except Exception as e:
            print(e)
            self.connected = False

    def InsertMsg(self, msg: TranslatedMessage):
        self.cur.execute("SELECT * from information_schema.tables")
        s = self.cur.fetchone()
        self.cur.execute("INSERT INTO messages (MsgId, Data, timestamp) VALUES (%s, %s, %s)", (msg.name, msg.magnitude, msg.timeReceived))
        self.con.commit()