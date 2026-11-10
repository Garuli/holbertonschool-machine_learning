#!/usr/bin/env python3
"""Module that defines the Binomial distribution class"""


class Binomial:
    """Class that represents a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize the Binomial distribution

        data: list of data used to estimate the distribution
        n: number of Bernoulli trials
        p: probability of a success
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            size = len(data)
            mean = sum(data) / size
            variance = sum((x - mean) ** 2 for x in data) / size
            p = 1 - (variance / mean)
            self.n = int(round(mean / p))
            self.p = float(mean / self.n)

    def pmf(self, k):
        """Calculate the PMF for a given number of successes

        k: number of successes
        Returns the PMF value for k, or 0 if k is out of range
        """
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        n_fact = 1
        for i in range(1, self.n + 1):
            n_fact *= i
        k_fact = 1
        for i in range(1, k + 1):
            k_fact *= i
        nk_fact = 1
        for i in range(1, self.n - k + 1):
            nk_fact *= i
        comb = n_fact / (k_fact * nk_fact)
        return comb * (self.p ** k) * ((1 - self.p) ** (self.n - k))
