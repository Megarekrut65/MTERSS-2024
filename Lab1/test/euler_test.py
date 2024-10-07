import unittest
from random import randint

from app.euler import Euler as Algo
from app.euler import EulerZigzag as Zigzag

class TestEuler(unittest.TestCase):
    def test_min(self):
        n = 0

        res = Algo.evaluate(n)
        self.assertEqual(res, 1)

    def test_big(self):
        n = 28

        res = Algo.evaluate(n)
        self.assertEqual(res, 1252259641403629865468285)

    def test_out_of_range(self):
        n = randint(-100, -1)

        self.assertRaises(ValueError, Algo.evaluate, n)

    def test_middle(self):
        n = 14

        res = Algo.evaluate(n)
        self.assertEqual(res, -199360981)

    def test_odd(self):
        n = randint(1, 50) * 2 + 1

        res = Algo.evaluate(n)
        self.assertEqual(res, 0)

    def test_cache(self):
        n = 28

        res = Algo.evaluate(n)
        self.assertEqual(res, 1252259641403629865468285)

        n = 28

        res = Algo.evaluate(n)
        self.assertEqual(res, 1252259641403629865468285)


class TestZigzag(unittest.TestCase):
    def test_min(self):
        n = 0

        res = Zigzag.evaluate(n)
        self.assertEqual(res, 1)

    def test_big(self):
        n = 199

        res = Zigzag.evaluate(n)
        self.assertEqual(res, 4708832410839036775127083656277455369927039641053956502555399993155472733019528453011116691778992363061715184657414377790009176379417288118062966167517347003597981485965853471991857601361417617516852747544156416749236128186966601581747429234102943849652014945729710502948586969216249495899499695789626698086604635236876027635257311232)

    def test_out_of_range(self):
        n = randint(-100, -1)

        self.assertRaises(ValueError, Zigzag.evaluate, n)

    def test_middle(self):
        n = 10

        res = Zigzag.evaluate(n)
        self.assertEqual(res, 50521)
