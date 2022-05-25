import json
import os

from canNetwork import TranslatedMessage

class jsonManager:

    def __init__(self) -> None:
        filename = 'resources/temp.json'
        self.file = open(filename, 'w+')
        self.isEmpty = self.CheckIfEmpty()
        if not self.isEmpty:
            self.json = json.loads(self.file)
        else:
            self.json = json.loads("{}")
        pass

    def CheckIfEmpty(self):
        self.file.seek(0, os.SEEK_END)
        if self.file.tell(): 
            self.seek(0)
            return True 
        else:
            return True

    def WriteJsonToDB():

        pass

    def appendToJson(self, translatedMsg: TranslatedMessage):
        if hasattr(translatedMsg.name, 'description'):
            translatedMsg.name = translatedMsg.name.description
        jsonobj = json.dump(translatedMsg.__dict__,self.file, ensure_ascii=False)
        self.file.write(',\n')
        self.file.flush()
        pass

    def removeFromJson():
        pass

    def printJson():
        print(json.dumps())