from accel import get_acceleration
import matplotlib.pyplot as plt


def run_avst():
    raw_acceleration_data = get_acceleration()
    acceleration_data = raw_acceleration_data["full_array"]
    times = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    fig, ax = plt.subplots()

    ax.plot(times, acceleration_data)
    ax.set_ylim(0, max(acceleration_data) + 0.1)
    ax.set_xlim(0, 1.0 + 0.1)
    ax.locator_params(axis="x", nbins=10)
    ax.locator_params(axis="y", nbins=15)
    fig.suptitle("$\overrightarrow{a}$ vs $t$", fontsize=14, fontweight="bold")
    ax.set_xlabel("$t$ (s)")
    ax.set_ylabel("$\overrightarrow{a}$ $(m/s^2)$ [+]")
    ax.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

    fig.savefig("avst.png", dpi=1200)
