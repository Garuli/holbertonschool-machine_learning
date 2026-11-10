#!/usr/bin/env python3
"""Module that defines the Normal distribution class"""


class Normal:
    """Class that represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize the Normal distribution

        data: list of data used to estimate the distribution
        mean: mean of the distribution
        stddev: standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            n = len(data)
            self.mean = float(sum(data) / n)
            variance = sum((x - self.mean) ** 2 for x in data) / n
            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """Calculate the z-score of a given x-value

        x: the x-value
        Returns the z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate the x-value of a given z-score

        z: the z-score
        Returns the x-value of z
        """
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculate the PDF for a given x-value

        x: the x-value
        Returns the PDF value for x
        """
        pi = 3.1415926536
        e = 2.7182818285
        coef = 1 / (self.stddev * ((2 * pi) ** 0.5))
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        return coef * (e ** exponent)
