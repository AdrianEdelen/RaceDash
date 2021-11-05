using System;
using RaceDash.Models;
using System.Text.RegularExpressions;
using System.Collections.Generic;


namespace RaceDash.CanNetwork
{
    /// <summary>
    /// SimCanUtils is a class that contains methods that are used to parse the CAN messages
    /// that come from can utils. It parses the messages and queues the data in a format that
    /// that the rest of the application understands.
    /// </summary>
    /// <remarks>
    /// 
    class SimCanUtils : ICanNetwork
    {
        private const string _filePath = "resources\\candump-2021-10-20_203215.log";
        private Queue<Frame> _queue;
        private List<string> _lines;
        public bool IsConnected { get; private set; }

        public SimCanUtils(Queue<Frame> queue)
        {
            Queue = queue;
            IsConnected = false;
        }
        public void StartConnection()
        {
            using (System.IO.FileStream = new  System.IO.FileStream(_filePath, FileMode.Open))
            {
                using (System.IO.StreamReader reader = new System.IO.StreamReader(file))
                {
                    while (!reader.EndOfStream)
                    {
                        string line = reader.ReadLine();
                        _lines.Add(line);
                    }
                    IsConnected = true;
                }
            }
        }
        
        public void CloseConnection()
        {
            IsConnected = false;
        }
        public void StartReceiveThread()
        {
            Task.Run(() => { while (IsConnected) receiveMessage();});
        }
        public void startSendThread()
        {   
            throw new NotImplementedException();
        }
        public void receiveMessage()
        {
            //This so so complex because of the way can-utils creates logs
            //It is a mess
            //I'm sorry
            //I'm so sorry
            //I bet you could do this with regex
            for (var i = 0; i < _lines.Count; i++)
            {
                //add one millisecond pause to simulate the time it takes to receive the message
                System.Threading.Thread.Sleep(1);

                /*
                Example of a canUtils log line:
                (1634776360.079982) can0 018#FFE5700A0000007E
                packet parts splits the lines by the space character
                timestamp is the first part of the line with parans removed
                device is the can0 portion
                idAndmMssage are the last two parts of the line
                split the idAndMessage by the # character
                */
                var packetParts = _lines[i].Split(' ');
                var timestampString = repacketParts[0].Replace("(", "").Replace(")", "");
                var device = packetParts[1];
                var idAndMessage = packetParts[2].Split('#');
                var id = idAndMessage[0];
                var message = idAndMessage[1];

                //add trailing zeros to message to make it 16 characters long
                //this is a hack to make the message 16 characters long
                //this makes it easier to process the data later
                message = message.PadRight(16, '0');

                //split message in groups of 2 characters
                //And convert to bytearray
                var messageArr = new List<byte>();
                for (var i = 0; i < message.Length; i += 2)
                {
                    var group = message.Substring(i, 2);
                    var value = Convert.ToByte(group);
                    messageArr.Add(value);
                }
                //reverse messageArr, This is to correct the endianness of the architecture
                messageArr.Reverse();
                //convert timestampString to DateTime from unix time string
                var timestamp = DateTime.FromUnixTimeSeconds(Convert.ToInt64(timestampString));
                //TODO change this from frame to whatever data type c# can uses
                Queue.Enqueue(new Frame(timestamp, device, id, messageArr));
            } 
        }   

        public void SendMessage()
        {
            throw new NotImplementedException();
        }
    }
}
