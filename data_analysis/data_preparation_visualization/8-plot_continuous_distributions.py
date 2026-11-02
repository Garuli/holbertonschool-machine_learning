#!/usr/bin/env python3
"""Module that plots the distribution of continuous columns."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """Plot a histogram with KDE and a boxplot for each continuous column.

    Args:
        df: pandas DataFrame with the data.
        columns_to_plot: list of column names to plot.
                         If None, all numeric columns are used.

    Returns:
        None
    """
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include=[np.number]).columns

    n_cols = len(columns_to_plot)

    fig, axes = plt.subplots(n_cols, 2, figsize=(14, 3 * n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, col in enumerate(columns_to_plot):
        data = df[col].dropna()

        # Histogram + KDE
        axes[i, 0].hist(
            data,
            bins=30,
            density=True,
            alpha=0.7,
            edgecolor="black"
        )

        # KDE curve
        kde = stats.gaussian_kde(data)
        x = np.linspace(data.min(), data.max(), 200)

        axes[i, 0].plot(
            x,
            kde(x),
            color="red",
            linestyle="--",
            linewidth=1.5
        )

        axes[i, 0].set_title(f"{col} Histogram + KDE")
        axes[i, 0].set_xlabel(col)
        axes[i, 0].set_ylabel("Density")

        # Horizontal Boxplot
        axes[i, 1].boxplot(
            data,
            vert=False,
            patch_artist=False,
            whis=(0, 100),
            showfliers=False
        )

        axes[i, 1].set_title(f"{col} Boxplot")
        axes[i, 1].set_xlabel(col)

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()