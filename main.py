from avst import run_avst
from generate import generate_graphs
from accel import get_acceleration
import subprocess

from vvst import get_velocity_data


def main():
    print("Do you want to generate the graphs? (y/n)")
    generate = input()
    if generate == "y":
        generate_graphs()
        print("Graphs generated")
        print("Would you like to see the graphs? (y/n)")
        if input() == "y":
            print("Opening graphs")
            subprocess.call(["open", "dvst.png"])
            subprocess.call(["open", "vvst.png"])
            subprocess.call(["open", "dvst_deviation.png"])
            subprocess.call(["open", "vvst_deviation.png"])
    elif generate == "n":
        print("Would you like to see the graphs? (y/n)")
        if input() == "y":
            print("Opening graphs")
            subprocess.call(["open", "dvst.png"])
            subprocess.call(["open", "vvst.png"])
            subprocess.call(["open", "dvst_deviation.png"])
            subprocess.call(["open", "vvst_deviation.png"])

    else:
        print("Invalid input")
        main()

    print("Would you like to see the data points (y/n)")
    if input() == "y":
        print(get_velocity_data())
    else:
        print("Okay")

    print("Calculating acceleration")

    print("Would you like to see the acceleration? (y/n)")
    if input() == "y":
        acceleration = get_acceleration()
        print("Acceleration calculated")
        if acceleration["is_uniform"] == "acceleration is uniform":
            print("Acceleration is uniform")
            print("Acceleration:\n" + acceleration["acceleration"] + "\n")
            [print(i) for i in acceleration["full_array"]]
        else:
            print("Acceleration is not uniform")
    print("Would you like to see the acceleration graph? (y/n)")
    if input() == "y":
        run_avst()
        print("Opening acceleration graph")
        subprocess.call(["open", "avst.png"])

    else:
        print("Ok, bye")


main()
