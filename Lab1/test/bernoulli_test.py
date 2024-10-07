import unittest
from random import randint
from fractions import Fraction

from app.bernoulli import Bernoulli as Algo


class TestBernoulli(unittest.TestCase):
    def test_min(self):
        n = 0

        res = Algo.evaluate(n)
        self.assertEqual(res, 1)

    def test_big(self):
        n = 100

        res = Algo.evaluate(n)
        self.assertEqual(res,
                         Fraction(
                             -94598037819122125295227433069493721872702841533066936133385696204311395415197247711,
                             33330))

    def test_out_of_range(self):
        n = randint(-100, -1)

        self.assertRaises(ValueError, Algo.evaluate, n)

    def test_middle(self):
        n = 50

        res = Algo.evaluate(n)
        self.assertEqual(res, Fraction(495057205241079648212477525, 66))

    def test_odd(self):
        n = randint(1, 50)*2 + 1

        res = Algo.evaluate(n)
        self.assertEqual(res, 0)


    def test_cache(self):
        n = 100

        res = Algo.evaluate(n)
        self.assertEqual(res,
                         Fraction(
                             -94598037819122125295227433069493721872702841533066936133385696204311395415197247711,
                             33330))

        n = 50

        res = Algo.evaluate(n)
        self.assertEqual(res, Fraction(495057205241079648212477525, 66))
