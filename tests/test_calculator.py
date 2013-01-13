import unittest
import sys
sys.path.append("../")
from calculator import *

class CalulatorTest(unittest.TestCase):
    
    def test_plus(self):
        self.assertEqual(3, plus(1, 2))

if __name__ == '__main__':
    unittest.main()
