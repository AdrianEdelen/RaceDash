using System.Collections.Generic;
using RaceDash.Models;
namespace RaceDash.CanNetwork
{
    public interface ICanNetwork
    {
        

        public void StartConnection();
        public void CloseConnection();
        public void StartReceiveThread();
        public void startSendThread();
        public void receiveMessage();
        public void SendMessage();
        

    }

}