using RaceDash.Models;

namespace RaceDash.CarData
{

    class FRS2013Base : Car
    {
        /*
        This is the command dictionary for a 2013 Scion FRS
        Each car is different.
        Each method processes the can data differently.
        The methods are mapped to a dict and are called in the 
        packet processing thread

        BYTE ORDERING / NAMING
        The bytes are reversed to LE 
        before they get sent here
         _________________
        | 0 1 2 3 4 5 6 7 |
        | A B C D E F G H |
         ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        */

        public FRS2013Base(TransmissionType transType, UsageType usage,
                            string color, string name )
        {
            base.Make = "Scion";
            base.Model = "FRS";
            base.Year = 2013;
            base.TransType = transType;
            base.Usage = usage;
            base.color = color;
            base.Name = name;
            

        }

        Dictionary<string, Function<string, Frame>> commandDict = 
        {
            
        }; 

    }


}