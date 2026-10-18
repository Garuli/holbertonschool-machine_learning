#!/usr/bin/env python3
"""Module that plots a stacked bar graph"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Plots a stacked bar graph of the fruit each person possesses"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))
    people = ['Farrah', 'Fred', 'Felicia']
    names = ['apples', 'bananas', 'oranges', 'peaches']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
    bottom = np.zeros(3)
    for i in range(4):
        plt.bar(people, fruit[i], width=0.5, bottom=bottom,
                color=colors[i], label=names[i])
        bottom = bottom + fruit[i]
    plt.ylabel('Quantity of Fruit')
    plt.ylim(0, 80)
    plt.yticks(range(0, 81, 10))
    plt.title('Number of Fruit per Person')
    plt.legend()
    plt.show()
