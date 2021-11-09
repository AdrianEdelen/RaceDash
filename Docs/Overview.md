Overview

The RaceDash Processing Module consists of four primary elements

The Network
The Logger
The Command Dictionary
And the message

The Network:
The canNetwork interface establishes the connection to the bus.
It is a wrapper over the python-can class adding the functionailty to fully monitor the bus and consume any messages that come across, it also has similar behavior for sending messages.

The canNetwork also configures the can devices on the host device.

This abstraction makes it much easier to get a connection up and running and start receiving messages on the bus. 

To use the CanNetwork and its implementations simply instantiate an implementation and pass in a reference Queue (for the received messages to be stored), the device you want to use e.g. 'can0', the speed, eg '500000' for automative, and the txrx buffer TODO

Once you have an instantiated Network it will continously monitor for new messages and put them into the queue, you can use any of the python queue implementations and handle the queue however you would like.

The queue holds standard python-can messages and so they can be handled accordingly

The Logger




The RPM also consists of additional ancillary components that are not required for primitive operation

These include:

The API
The Database Broker
The File Writer
The Data Streamer

While none of these components are technically required to process the data coming off of the bus, you won't get much of a result without atleast one component active

These components serve as the communication layer to listening and services
