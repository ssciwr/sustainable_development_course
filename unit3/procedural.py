import sys
import argparse
import numpy as np

# procedural programming style

def parse_command_line()->float:
    """Function to parse user input. User input is a float and a string.
    :Returns: area of the circle (float)"""
    parser = argparse.ArgumentParser(description="""Program to calculate 
        area of circle. Check -h or --help for options.
        Usage: ./main.py -r 4""")
    parser.add_argument("-r", "--radius", default=3.0, help="Radius of the \
        circle, in cm. \
        Default value: 3.0 cm")
    args = parser.parse_args()
    r = float(args.radius)
    return r


def print_out(r_in, area_out)->None:
    """Function to print output."""
    print("Circle with radius r = {:3.2f}cm:".format(r_in))
    print("Area A = {:4.2f}cm2.".format(area_out))


def area_circ(r_in)->float:
    """Calculates the area of a circle with given radius.

    :Input: The radius of the circle (float, >=0).
    :Returns: The area of the circle (float)."""
    if r_in < 0:
        raise ValueError("The radius must be >= 0.")
    area_out = np.pi * r_in**2
    return area_out


if __name__ == "__main__":
    """Main function that drives the calculation."""
    # Get the input parameters
    r_in = parse_command_line()
    # Calculate the area of the given circle
    area_out = area_circ(r_in)
    print_out(r_in, area_out)