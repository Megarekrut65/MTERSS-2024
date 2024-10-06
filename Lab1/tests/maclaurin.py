import unittest
from decimal import Decimal

from app.maclaurin import MaclaurinSeries as Algo

PI = Decimal("3.14159265358979323846")

class TestZigzag(unittest.TestCase):
    def test_near_right_border(self):
        x = PI / 2 - Decimal("0.1")
        places = 10
        eps = 10**(-places)

        res, _ = Algo.evaluate(x, eps)
        self.assertAlmostEqual(res, Decimal("19.9833305549"), places=places-1)

    def test_near_left_border(self):
        x = -PI / 2 + Decimal("0.1")
        places = 6
        eps = 10**(-places)

        res, n = Algo.evaluate(x, eps)
        print(n)
        self.assertAlmostEqual(res, Decimal("0.050041"), places=places-1)

    def test_small_eps(self):
        x = -PI / 2 + Decimal("0.1")
        places = 11
        eps = 10**(-places)

        res, _ = Algo.evaluate(x, eps)
        self.assertAlmostEqual(res, Decimal("0.05004170837"), places=places)

    def test_near_zero(self):
        x = Decimal("0.0005")
        places = 6
        eps = 10 ** (-places)

        res, n = Algo.evaluate(x, eps)
        self.assertAlmostEqual(res, Decimal("1.0005"), places=places)

    def test_zero(self):
        x = Decimal(0)

        places = 3
        eps = 10**(-places)

        res, _ = Algo.evaluate(x, eps)
        self.assertAlmostEqual(res, Decimal(1), places=places)

    def test_out_of_left_range(self):
        x = -PI

        places = 3
        eps = 10**(-places)

        self.assertRaises(ValueError, Algo.evaluate, x, eps)

    def test_out_of_right_range(self):
        x = PI

        places = 3
        eps = 10**(-places)

        self.assertRaises(ValueError, Algo.evaluate, x, eps)