using System;
using RaceDash.Models;
using System.Text.RegularExpressions;
using System.DateTime;
namespace RaceDash.CanNetwork
{
    class SimCanUtils : ICanNetwork
    {
        private const string _filePath = "resources\\candump-2021-10-20_203215.log";

        public Queue Queue { get; set; }
        public int Position { get; set; }
        public List<string> Lines { get; set; }
        public SimCanUtils(Queue queue)
        {
            Queue = queue;
        }
        public StartConnection()
        {
            using (System.IO.FileStream = new  System.IO.FileStream(_filePath, FileMode.Open))
            {
                using (System.IO.StreamReader reader = new System.IO.StreamReader(file))
                {
                    while (!reader.EndOfStream)
                    {
                        string line = reader.ReadLine();
                        Lines.Add(line);
                    }
                }
            }
        }
        
        public CloseConnection()
        {
            throw new NotImplementedException();
        }
        public StartReceiveThread()
        {
            Thread thread = new Thread();
            throw new NotImplementedException();
        }
        public startSendThread()
        {   
            throw new NotImplementedException();
        }
        public receiveMessage()
        {
            var re = new Regex(@"[()]");
            for (var i = 0; i < Lines.Count; i++)
            {
                //add one millisecond pause to simulate the time it takes to receive the message
                System.Threading.Thread.Sleep(1);

                var packetParts = Lines[i].Split(' ');
                var timestampString = repacketParts[0].Replace("(", "").Replace(")", "");
                var device = packetParts[1];
                var idAndMessage = packetParts[2].Split('#');
                var id = idAndMessage[0];
                var message = idAndMessage[1];
                //add trailing zeros to message to make it 16 characters long
                message = message.PadRight(16, '0');
                //split message in groups of 2 characters
                var messageArr = new List<byte>();
                for (var i = 0; i < message.Length; i += 2)
                {
                    var group = message.Substring(i, 2);
                    var value = Convert.ToByte(group);
                    messageArr.Add(value);
                }
                //reverse messageArr
                messageArr.Reverse();
                //convert timestampString to DateTime from unix time string
                var timestamp = DateTime.FromUnixTimeSeconds(Convert.ToInt64(timestampString));

                Queue.Enqueue(new Frame(timestamp, device, id, messageArr));

                //reset the loop if the last line was reached
                //this creates an infinite loop of processing for testing and simulation
                
                if (i == Lines.Count - 1)
                {
                    i = 0;
                }
            }
        }
        public SendMessage()
        {
            throw new NotImplementedException();
        }
    }
}
