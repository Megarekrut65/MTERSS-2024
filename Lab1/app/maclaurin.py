import math
from decimal import Decimal

from app.euler import EulerZigzag


class MaclaurinSeries:
    def __init__(self):
        self.cancel = False

    def evaluate(self, x: Decimal|float|str, eps: Decimal|float|str) -> tuple[Decimal, int]:
        if not isinstance(x, Decimal):
            x = Decimal(x)
        if not isinstance(eps, Decimal):
            eps = Decimal(eps)

        if abs(x) >= math.pi / 2:
            raise ValueError(f"The function argument({x}) does not belong to the domain. The domain is (-π/2, π/2)")

        x_n = Decimal(1)
        n_fac = 1
        sum_ = Decimal(1)
        prev = Decimal(0)
        n = 1
        while abs(sum_ - prev) > eps and not self.cancel:
            n_fac *= n
            x_n *= x
            prev = sum_
            sum_ += Decimal(EulerZigzag.evaluate(n)) * x_n / n_fac
            n += 1

        # n = 1
        # sum_ = Decimal(1)
        # prev = Decimal(0)
        #
        # while abs(sum_ - prev) > eps:
        #     prev = sum_
        #     sum_ += Decimal(EulerZigzag.evaluate(n)) / math.factorial(n) * x**n
        #     n+=1

        return sum_, n - 1
