import sys
import argparse
import numpy as np

# functional programming style
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Program to calculate 
            area of circle. Check -h or --help for options.
            Usage: ./main.py -r 4""")
    parser.add_argument("-r", "--radius", default=3.0, help="Radius of the \
            circle, in cm. \
            Default value: 3.0 cm")
    args = parser.parse_args()
    r = float(args.radius)
    if r < 0:
        raise ValueError("The radius must be >= 0.")
    area = lambda r : np.pi * r**2
    print("Circle with radius r = {:3.2f}cm:".format(r))
    print("Area A = {:4.2f}cm2.".format(area(r)))
