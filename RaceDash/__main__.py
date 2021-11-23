import canNetwork
import asyncio
async def main():
    try:
        #For testing implement a message counter
        messageCounter = 0
        # we can pass a known amount of complex messages in and count how many are missed
        # if any, it's not clear if the buffered messages are lost or not

        bus = canNetwork.canCommunication('can0')
        while True:
            msgtuple = bus.calcCanMessage(await bus.asyncBufferedReader.get_message())
            for translatedmsg in msgtuple:
                messageCounter += 1
                #Do Stuff
                pass
    except KeyboardInterrupt:
        print("Keyboard Interrupt, Shutting Down")
        bus.closeConnection()
        exit()
    except Exception as e:
        print(e)
        print("Unable to establish connection. Shutting down")     

        
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
