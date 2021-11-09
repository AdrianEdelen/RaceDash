Overview

The RaceDash Processing Module consists of five primary elements

The Queue
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

The Logger:

The logger consumes can frames off of a queue and processes them according to the configured car
This works by consuming the next frame off of the queue, then finding the appropriate function for that car and frame ID, processing the frame and then gives the data for the processed data to its consumers

The logger determines where to send the data based on the configuration file. if no consumers are configured, the processed data will be thrown out and the logger will begin processing the next message in the queue

The Command Dictionary:

The command dictionary is a dictionary of k: Message IDs and v: functions
each ID needs to be processed in a unique manner as they represent different components in a can network.
The appropriate dictionary is loaded based on the config file, as the logger processes a frame, it searches the dictionary for the appropriate function to call to process the frame, the command dictionary functions all return a message object which contains the translated message information. Occasionally there will be data that has unknown translations, in that case the frame will be reported as unknown with the ID and the raw data. this can be helpful later on if that frame gets translated, it can be reproccessed and the information can still be gained.


The Queue:

The queue is a standard python queue (or anything that implements the python queue)
the network puts frames onto the queue and the logger takes frames off of the queue.
This provides a way for the message to always be processed in the desired order drastically reduces the likelihood of permantly losing a can frame.

Since receiving the message off of the bus is trivial and some frames can result in 5+ discrete messages, there may be times where there is a backup of frames in the queue. keeping the frames in the queue allows them to be processed whenever the logger can catch up.

Later on there are plans to add caching and priorities to the logging process to allow for better handling of congestion on the bus.
Since the goal of RPM is to capture ALL traffic on a bus and since can message filtering is typically done with hardware, there are currently no filters for the traffic on the bus, this keeps RPM simple and allows the clients to filter out messages they are not interested in.
A potential idea for filtering in the future may be to use a config file to mark which packets should be logged, the packets would still be processed in this case, but they would not be sent to the client (the slwoest part of the operation)



The RPM also consists of additional ancillary components that are not required for primitive operation

These include:

The API
The Flask App
The Database Broker
The File Writer
The Data Streamer

While none of these components are technically required to process the data coming off of the bus, you won't get much of a result without atleast one component active

These components serve as the communication layer to listening and services

The API:
sits between the primary functions of RPM and the ancillery,
the api takes a processed frame and exposes the frame to 

The API sits in be

The Database Broker:
the DB Broker allows for easy connection to the database, performing crud operations for saving translated messages
