#!/usr/bin/env python3
"""Module that plots a line graph"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """Plots y as a solid red line, with the x-axis from 0 to 10"""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(y, 'r-')
    plt.xlim(0, 10)
    plt.show()
