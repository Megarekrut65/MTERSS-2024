from fractions import Fraction

import bernoulli
import utility


class Euler:
    __cache: dict[int, int] = {0:1}

    @staticmethod
    def evaluate(n: int) -> int:
        if n < 0:
            raise ValueError("The index of Euler number cannot be negative.")
        if n % 2 != 0:
            return 0
        if Euler.__cache.get(n):
            return Euler.__cache[n]
        euler_num = 1
        for k in range(1, n + 1):
            euler_num += Fraction(utility.binomial_coefficient(n, k-1) * (2**k - 4**k)* bernoulli.Bernoulli.evaluate(k)) / k

        Euler.__cache[n] = int(euler_num)
        return Euler.__cache[n]

    @staticmethod
    def zigzag(n: int) -> int:
        if n < 0:
            raise ValueError("The index of Euler number cannot be negative.")
        if n % 2 == 0:
            return (-1)**(n//2) * Euler.evaluate(n)
        two_n = 2**(n+1)
        return int((-1)**((n-1)//2) * (two_n * (two_n - 1) * bernoulli.Bernoulli.evaluate(n+1)) / (n + 1))