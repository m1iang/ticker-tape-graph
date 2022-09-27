from data import displacement_data
import math
from sigfig import sig_to_n
import numpy as np
from vvst import get_velocity_data


def get_acceleration():
    velocity_data = get_velocity_data()

    # acceleration should be uniform

    # these will be the two points we use to calculate the slope of the acceleration line
    # the slope of the acceleration line will be the acceleration

    # get the slope of the acceleration line
    # acceleration = (y2 - y1) / (x2 - x1)

    acceleration_data = []

    for i in range(len(velocity_data[0])):
        if i != 0:
            # we want to make sure that the acceleration is uniform
            acceleration_data.append(
                (velocity_data[1][i] - velocity_data[1][i - 1])
                / (velocity_data[0][i] - velocity_data[0][i - 1])
            )

    # make sure that the acceleration has 11 data points
    acceleration_data.append(acceleration_data[3])

    # make sure that the acceleration is uniform by checking that all the values in acceleration_data are the same
    # use isclose due to floating point errors
    if (math.isclose(acceleration_data[0], acceleration_data[1])) and (
        math.isclose(acceleration_data[1], acceleration_data[2])
    ):
        return {
            "is_uniform": "acceleration is uniform",
            "acceleration": str(sig_to_n(2, acceleration_data[4])) + " m/s^2",
            "full_array": acceleration_data,
        }
