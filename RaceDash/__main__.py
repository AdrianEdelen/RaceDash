from pyparsing import empty
from commandDict import commmandDict
import canNetwork
import asyncio
from commandDict import MessageNames
from textwrap import wrap
import jsonManager
import dbCon
async def main():
    try:


        testFilePath = 'resources/candump-2021-10-20_203215.log'

        #test gui:
        #just append each new message that comes through to a list
        #display it just like in the console with live values
        #expirement with the car until the values make sense
        json = jsonManager.jsonManager()
        context = dbCon.db()


        file = open(testFilePath,'r')
        lines = file.readlines()
        file.close()
        testing = True

        if not testing:
            bus = canNetwork.canCommunication('can0')

            while True:
                msgtuple = bus.calcCanMessage(await bus.asyncBufferedReader.get_message())
                
                for translatedmsg in msgtuple:
                    for name in MessageNames:
                        if translatedmsg.name == name:
                            json.appendToJson(translatedmsg)

                            pass
                            #write to disk (probably json)

        else:
            cmds = commmandDict('FRS')
            bus = canNetwork.canCommunication(cmds)
            while True:
                for line in lines:
                    splitLine = line.split()
                    timestamp = float(splitLine[0].replace('(','').replace(')',''))
                    idAndData = splitLine[2].split('#')
                    data = wrap(idAndData[1].zfill(16), 2)
                    #databytes = yield (int(byte,16) for byte in data)
                    databytes = []
                    for byte in data:
                        databytes.append(int(byte,16))
                    msg = type('',(object,),{"timestamp": timestamp, "arbitration_id":int(idAndData[0], 16), "data":databytes })()
                    msgtuple = bus.calcCanMessage(msg)
                    for msg in msgtuple:
                        json.appendToJson(msg)
                        context.InsertMsg(msg)
                        if msg.name == MessageNames.SteeringAngleOne:
                            print(msg.magnitude, end='\r')

            pass

    except KeyboardInterrupt:
        print("Keyboard Interrupt, Shutting Down")
        bus.closeConnection()
        exit()
    except FileNotFoundError as e:
        print('could not load:', e.filename)
    except Exception as e:
        print(e)
        print("Unable to establish connection. Shutting down")     
    finally:
        if (context.con):
            context.cur.close()
            context.con.close()

 
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
