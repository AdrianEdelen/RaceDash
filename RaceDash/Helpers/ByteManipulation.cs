
namespace Helpers.ByteManipulation 
{
    class ByteManipulation 
    {
        //get bytes from array
        public static byte[] GetBytes(byte[] bytes, int start, int length) 
        {
            byte[] newBytes = new byte[length];
            for (int i = 0; i < length; i++) 
            {
                newBytes[i] = bytes[start + i];
            }
            return newBytes;
        }
        //get bits from byte array
        public static byte[] GetBits(byte[] bytes, int start, int length) 
        {
            byte[] newBytes = new byte[length];
            for (int i = 0; i < length; i++) 
            {
                newBytes[i] = (byte)(bytes[start + i] >> (i % 8));
            }
            return newBytes;
        }
        
    }
}