import unittest
import day_01, day_02

class AoCTests(unittest.TestCase):
    def test_01_star1(self):
        sum = day_01.day_01_star1()
        self.assertEqual(sum, 400)

    def test_01_star2(self):
        deltas = [+3, +3, +4, -2, -4]
        repeated_freq = day_01.day_01_star2(deltas)
        self.assertEqual(repeated_freq, 10)

        deltas = [+7, +7, -2, -7, -4]
        repeated_freq = day_01.day_01_star2(deltas)
        self.assertEqual(repeated_freq, 14)

    def test_02_star1(self):
        checksum = day_02.day_02_star1(day_02.read_input())
        self.assertEqual(checksum, 6448)
    
    def test_02_star2(self):
        day_02.day_02_star2(day_02.read_input())