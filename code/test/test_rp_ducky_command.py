import unittest
from unittest import TestCase

from lib.rp_ducky_command import RPDuckyCommand, RPDuckyCommandType


#===============================================================================
#===============================================================================

class TestRPDuckyCommand(TestCase):
    
    def test_create_returns_none_for_rem_command(self):
      command = RPDuckyCommand.make_command("REM hello world", None)
      arguments = command.getArguments()

      self.assertEqual(command.getType(), RPDuckyCommandType.DELAY)

      self.assertEqual(len(arguments), 1)
      self.assertEqual(arguments[0], 1000)

    def test_handles_delay_with_string_argument(self):
      command = RPDuckyCommand.make_command("DELAY 1000", None)

      self.assertEqual(command.getType(), RPDuckyCommandType.DELAY)
      self.assertEqual(command.ar(), RPDuckyCommandType.DELAY)

#===============================================================================
#===============================================================================

if __name__ == '__main__':
    unittest.main()