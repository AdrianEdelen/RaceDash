
namespace RaceDash.Models 
{
    class Frame
    {
        public Datetime Timestamp { get; set; }
        public string Name { get; set; }
        public double Magnitude { get; set; }

        public Frame(Datetime timestamp,string name,double magnitude)
        {
            Timestamp = timestamp;
            Name = name;
            Magnitude = magnitude;
        }

    }
}