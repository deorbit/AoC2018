import unittest
import day_01
import day_02
import day_03
import day_04
import day_05
import day_06
import day_07

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

    def test_05_star1(self):
        remainder = day_05.day_05_star1(day_05.read_input())
        self.assertEqual(11720, len(remainder))

    def test_05_star2(self):
        shortest_length = day_05.day_05_star2(day_05.read_input())
        self.assertEqual(shortest_length, 4956)

    def test_06_star1(self):
        largest_area_size = day_06.day_06_star1(day_06.read_input())
        self.assertEqual(largest_area_size, 2342)

    def test_06_star2(self):
        cell_count = day_06.day_06_star2(day_06.read_input())
        self.assertEqual(cell_count, 43302)

    def test_07_star1(self):
        plan = day_07.day_07_star1(day_07.read_input("day_07_input.txt"))
        self.assertEqual(''.join(plan), "EPWCFXKISTZVJHDGNABLQYMORU")