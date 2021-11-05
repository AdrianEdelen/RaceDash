using RaceDash.Models;
using System.Collections.Generic;

namespace RaceDash.CanNetwork
{
    class CanCommunication : ICanNetwork
    {
        public Queue<Frame> Queue { get; set; }
        public void CanConnection()
        {
            
        }
        public void StartConnection() 
        {
            throw new NotImplementedException();
        }
        public void CloseConnection()
        {
            throw new NotImplementedException();
        }
        public void StartReceiveThread()
        {
            throw new NotImplementedException();
        }
        public void startSendThread()
        {
            throw new NotImplementedException();
        }
        public void receiveMessage()
        {
            throw new NotImplementedException();
        }
        public void SendMessage() 
        {
            throw new NotImplementedException();
        }
    }
}