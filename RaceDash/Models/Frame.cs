
namespace RaceDash.Models 
{
    class Frame
    {
        public Datetime Timestamp { get; set; }
        public string Name { get; set; }
        public double Magnitude { get; set; }

        public strin Device { get; set; }

        //TODO: change device to an enum
        public Frame(Datetime timestamp, string device,string name,double magnitude)
        {
            Timestamp = timestamp;
            Device = device;
            Name = name;
            Magnitude = magnitude;
        }

    }
}