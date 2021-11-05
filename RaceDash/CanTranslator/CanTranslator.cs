using RaceDash.Models;
using System.Collections.Generic;
namespace RaceDash.CanTranslator
{
    class CanTranslator
    {
        //TODO: Change this from frame to whatever data type can uses
        private Queue<Frame> _queue;
        public CanTranslator(Queue<Frame> queue)
        {
            _queue = queue;
        }

        public void StartProcessorThread()
        {
            Task.Run(() => { while (true) TranslateMessage();});
        }
        public void TranslateMessageToFrame()
        {
            var canMsg = _queue.Dequeue();

            
        }
        public void TranslateMessageFromFrame() 
        {

        }
    }
}