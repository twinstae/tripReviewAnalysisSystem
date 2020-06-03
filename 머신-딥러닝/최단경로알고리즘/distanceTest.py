import unittest
import distance
testResult5 = [78, 96, 119, 143, 150, 157]
testResult15 = [6, 9, 10, 11, 15, 16, 19, 33, 37, 47, 49, 51, 52, 54, 57, 62, 70, 78, 83, 86, 89, 96, 101, 108, 113, 115, 117, 119, 123, 127, 129, 131, 135, 138, 141, 143, 144, 150, 156, 157, 163, 167, 170, 171]

class DistanceTest(unittest.TestCase):
    def test_15(self):
        c = distance.in_out_key_15(0)
        self.assertEqual(c, testResult15)
    
    def test_5(self):
        c= distance.in_out_key_5(0)
        self.assertEqual(c, testResult5)