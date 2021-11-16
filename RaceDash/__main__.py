import canLogger
import canNetwork
import asyncio
"""
The main method loads configurations, and starts the threads for parsing packets off of the bus
"""
async def main():
    try:
        bus = canNetwork.canCommunication('can0')
        recorder = canLogger.CanLogger()
        while True:
            msgtuple = bus.calcCanMessage(await bus.asyncBufferedReader.get_message())
            
            for translatedmsg in msgtuple:
                #send to db
                #send to UI
                #send to File
                #whatever
                pass
    except KeyboardInterrupt:
        print("Keyboard Interrupt, Shutting Down")
        bus.closeConnection()
        recorder.dbConn.close()
        exit()
    except Exception as e:
        print(e)
        print("Unable to establish connection. Shutting down")     
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
