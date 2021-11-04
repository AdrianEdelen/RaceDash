using System;
using RaceDash.CanNetwork;
using RaceDash.Models;

namespace RaceDash
{
    class Program
    {
        static void Main(string[] args)
        {
            //start queue
            CuncurrentQueue<Frame> queue = new CuncurrentQueue<Frame>();            

            //load settings
            
            // start db connection

            //start can network
            bool useSim = true;
            if (useSim)
            {
                var network = new CanNetwork.SimCanUtils(queue);
            }
            //start can translator

            //start api server

        }
    }
}