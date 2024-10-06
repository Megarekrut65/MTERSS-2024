import unittest
from random import randint

from app.utility import binomial_coefficient as bc

class TestUtility(unittest.TestCase):
    def test_min(self):
        n = 1
        k = 0

        res = bc(n, k)

        self.assertEqual(res, 1)
    def test_big(self):
        n = 100
        k = 20

        res = bc(n, k)

        self.assertEqual(res, 535_983_370_403_809_682_970)

        n = 1000
        k = 998

        res = bc(n, k)

        self.assertEqual(res, 499500)

    def test_less_by_one(self):
        n = randint(1, 100000)
        k = n - 1

        res = bc(n, k)

        self.assertEqual(res, n)

    def test_middle(self):
        n = 5
        k = 3

        res = bc(n, k)

        self.assertEqual(res, 10)

        n = 20
        k = 3

        res = bc(n, k)

        self.assertEqual(res, 1140)

    def test_same(self):
        n = randint(1, 100000)
        k = n

        res = bc(n, k)

        self.assertEqual(res, 1)

    def test_k_zero(self):
        n = randint(1, 100000)
        k = 0

        res = bc(n, k)

        self.assertEqual(res, 1)

    def test_out_of_left_range(self):
        n = randint(1, 100000)
        k = -n

        res = bc(n, k)

        self.assertEqual(res, 0)

    def test_out_of_right_range(self):
        n = randint(1, 100000)
        k = n + 1

        res = bc(n, k)

        self.assertEqual(res, 0)