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
