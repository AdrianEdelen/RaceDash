
namespace RaceDash.CanNetwork
{
    interface ICanNetwork
    {
        public Queue Queue { get; set; }

        public StartConnection();
        public CloseConnection();
        public StartReceiveThread();
        public startSendThread();
        public receiveMessage();
        public SendMessage();
        

    }

}