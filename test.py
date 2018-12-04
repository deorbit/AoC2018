import unittest
import day_01
import day_02
import day_03
import day_04

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

    def test_03_star1(self):
        overlap = day_03.day_03_star1(day_03.read_input())
        self.assertEqual(overlap, 100595)

    def test_03_star2(self):
        claim_id = day_03.day_03_star2(day_03.read_input())
        self.assertEqual(claim_id, 415)

    def test_04_star1(self):
        guard_minute = day_04.day_04_star1(day_04.read_input())
        self.assertEqual(guard_minute, 26281)

    def test_04_star2(self):
        guard_minute = day_04.day_04_star2(day_04.read_input())
        self.assertEqual(guard_minute, 73001)