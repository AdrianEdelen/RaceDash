from car import *
import canNetwork
"""
The current main menu, basic display if toggled on
"""
def main():
    print('*******************Main Menu*******************')
    print('* 1) Read can data from car                   *')
    print('* 2) Read can data from file (sim or playback)*')
    print('* 3) Exit                                     *')
    print('***********************************************')
    userInput = int(input())

    if userInput == 1:
        curCar = car(canNetwork.canCommunication()) #instantiate our car
    elif userInput == 2:
        curCar = car(canNetwork.simCanCanUtils()) #instantiate sim car
    else:
        exit()

    try:
        curCar.canBus.startConnection() #open the can bus connection
        curCar.startProcessorThread() #start processing packets
        curCar.canBus.startRecieveThread() #start listening for packets
        #it is important to start processing packets first, otherwise, you can build up a queue of messages
    except:
        print("Unable to establish connection. Shutting down")
        curCar.dispose()
    #this try gets all connections going, at that point, they should be 
    #updating the properties of our car object in the background.
    #that means we can access the car periodically and get the current state of it
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(curCar)
    except KeyboardInterrupt:
        print('Shutting Down')
        curCar.dispose()

main()
