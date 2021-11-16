import canNetwork
import asyncio
async def main():
    try:
        bus = canNetwork.canCommunication('can0')
        while True:
            msgtuple = bus.calcCanMessage(await bus.asyncBufferedReader.get_message())
            for translatedmsg in msgtuple:
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
