import math
from decimal import Decimal

from euler import Euler


class MaclaurinSeries:
    @staticmethod
    def evaluate(x: Decimal|float|str, eps: Decimal|float|str) -> Decimal:
        if not isinstance(x, Decimal):
            x = Decimal(x)
        if not isinstance(eps, Decimal):
            eps = Decimal(eps)

        if abs(x) >= math.pi / 2:
            raise ValueError(f"The function argument is not scoped: {x}")

        x_n = Decimal(1)
        n_fac = 1
        sum_ = Decimal(1)
        prev = Decimal(0)
        n = 1
        while abs(sum_ - prev) > eps:
            n_fac *= n
            x_n *= x
            prev = sum_
            sum_ += x_n * Euler.zigzag(n) / n_fac
            n += 1

        return prev