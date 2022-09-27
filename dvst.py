import matplotlib.pyplot as plt
import numpy as np
from tangent import f, x


def run_dvst():
    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(x, f(x))
    ax.set_ylim(0, f(x).max() + 0.1)
    ax.set_xlim(0, 1.0 + 0.1)
    ax.locator_params(axis="x", nbins=15)
    ax.locator_params(axis="y", nbins=10)
    fig.suptitle("$\overrightarrow{d}$ vs $t$", fontsize=14, fontweight="bold")
    ax.set_xlabel("t (s)")
    ax.set_ylabel("$\overrightarrow{d}$ (m) [+]")
    ax.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

    fig.savefig("dvst.png", dpi=1200)


def run_dvst_scatter():
    fig, ax = plt.subplots()
    ax.plot(x, f(x), "yo", x, f(x), "--k")
    ax.set_ylim(0, f(x).max() + 0.1)
    ax.set_xlim(0, 1.0 + 0.1)
    ax.locator_params(axis="x", nbins=10)
    ax.locator_params(axis="y", nbins=20)
    ax.grid()
    fig.suptitle("$\overrightarrow{d}$ vs $t$", fontsize=14, fontweight="bold")
    ax.set_title(
        "showing the deviation of the data points from the curve of best fit",
        fontsize=10,
    )
    ax.set_xlabel("t (s)")
    ax.set_ylabel("$\overrightarrow{d}$ (m) [+]")
    ax.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

    fig.savefig("dvst_deviation.png", dpi=1200)
