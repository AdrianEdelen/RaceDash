import unittest
import can

from RaceDash.packetCommand import commandDict

class testPacketCommandMethods(unittest.TestCase):

    def setUp(self) -> None:

        self.msg= can.Message(arbitration_id = 0x144, data = [0, 25, 0, 1, 3, 1, 4, 1])
        

    def test_commandDict(self):
        cmds = commandDict().commands

        retString = cmds.get(self.msg.arbitration_id)
        self.assertEqual(retString, 'parsed packet id 144')


if __name__ == '__main__':
    unittest.main()