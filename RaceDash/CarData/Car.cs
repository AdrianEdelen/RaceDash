namespace RaceDash.CarData
{
    public enum TransmissionType
    {
        Automatic,
        Manual
    }
    public enum UsageType
    {
        Daily,
        Weekend,
        TrackDay,
        TrackCar,
        RaceCar
    }
    public abstract class Car
    {
        public string Make { get; set; }
        public string Model { get; }
        public int Year { get; }
        public TransmissionType TransType { get; set; }
        public string color { get; set; }
        public UsageType Usage { get; set; }
        public string Name { get; set; }

        public Car()
        {
            Make = "None";
            Model = "None";
            Year = 1000;
            TransType = TransmissionType.Automatic;
            Usage = usageType.Daily;
            Name = "No Info";
        }
       
        
    }
}