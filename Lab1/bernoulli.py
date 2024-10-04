from fractions import Fraction

import utility


class Bernoulli:
    __cache: list[Fraction] = [Fraction(1)]

    @staticmethod
    def evaluate(n: int) -> Fraction:
        if n < 0:
            raise ValueError("The index of Bernoulli number cannot be negative.")
        if n % 2 != 0:
            return Fraction(0)
        if n < len(Bernoulli.__cache):
            return Bernoulli.__cache[n]

        for m in range(len(Bernoulli.__cache), n + 1):
            total_sum = Fraction(0)
            for k in range(m):
                binomial = utility.binomial_coefficient(m + 1, k)
                total_sum += binomial * Bernoulli.__cache[k]
            b_m = -total_sum / (m + 1)
            Bernoulli.__cache.append(b_m)

        return Bernoulli.__cache[n]
