import matplotlib.pyplot as plt
from tangent import get_tangent_line_slope
from data import displacement_data


def get_velocity_data():
    velocity_data = [[], []]

    for i in range(len(displacement_data[0])):
        velocity_data[0].append(displacement_data[0][i])
        velocity_data[1].append(get_tangent_line_slope(displacement_data[0][i]))

    return velocity_data


def run_vvst():
    fig, ax = plt.subplots()

    velocity_data = [[], []]

    for i in range(len(displacement_data[0])):
        velocity_data[0].append(displacement_data[0][i])
        velocity_data[1].append(get_tangent_line_slope(displacement_data[0][i]))

    ax.plot(velocity_data[0], velocity_data[1])
    ax.set_ylim(0, velocity_data[1].pop() + 0.1)
    ax.set_xlim(0, 1.0 + 0.1)
    ax.locator_params(axis="x", nbins=10)
    ax.locator_params(axis="y", nbins=15)
    fig.suptitle("$\overrightarrow{v}$ vs $t$", fontsize=14, fontweight="bold")
    ax.set_xlabel("$t$ (s)")
    ax.set_ylabel("$\overrightarrow{v}$ (m/s) [+]")
    ax.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

    fig.savefig("vvst.png", dpi=1200)


def run_vvst_scatter():
    fig, ax = plt.subplots()

    velocity_data = [[], []]

    for i in range(len(displacement_data[0])):
        velocity_data[0].append(displacement_data[0][i])
        velocity_data[1].append(get_tangent_line_slope(displacement_data[0][i]))

    ax.plot(
        velocity_data[0],
        velocity_data[1],
        "yo",
        velocity_data[0],
        velocity_data[1],
        "--k",
    )
    ax.set_ylim(0, velocity_data[1].pop() + 0.1)
    ax.set_xlim(0, 1.0 + 0.1)
    ax.locator_params(axis="x", nbins=10)
    ax.locator_params(axis="y", nbins=20)
    ax.grid()
    fig.suptitle("$\overrightarrow{v}$ vs $t$", fontsize=14, fontweight="bold")
    ax.set_title(
        "showing the deviation of the data points from the line of best fit",
        fontsize=10,
    )
    ax.set_xlabel("t (s)")
    ax.set_ylabel("$\overrightarrow{d}$ (m/s) [+]")
    ax.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

    fig.savefig("vvst_deviation.png", dpi=1200)
