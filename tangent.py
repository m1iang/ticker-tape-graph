import numpy as np
from data import displacement_data


def f(x):
    # creates a function that returns the y value of the parabola at x
    return (
        np.polyfit(displacement_data[0], displacement_data[1], 2)[0] * x**2
        + np.polyfit(displacement_data[0], displacement_data[1], 2)[1] * x
        + np.polyfit(displacement_data[0], displacement_data[1], 2)[2]
    )


def slope(x):
    # get the derivative of the function returned by f
    return (
        2 * np.polyfit(displacement_data[0], displacement_data[1], 2)[0] * x
        + np.polyfit(displacement_data[0], displacement_data[1], 2)[1]
    )


# define only 10 points for the x axis
x = np.linspace(0.0, 1.0, 10)

# get the tangent line at a certain point
def get_tangent(x1):
    x1 = x1
    y1 = f(x1)
    return x1, y1


# construct the tangent line y = mx + b
def get_tangent_equation(x, x1, y1):
    return slope(x1) * (x - x1) + y1


# get the slope of the tangent line at a certain point
def get_tangent_line_slope(x1):
    return slope(x1)
