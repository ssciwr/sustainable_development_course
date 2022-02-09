# main program

import sys
import argparse
import circle as ce


def parse_command_line():
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


if __name__ == "__main__":
    """Main function that drives the calculation."""
    # Get the input parameters
    r = parse_command_line()
    # Calculate the area of the given circle
    ac = ce.area_circ(r)
