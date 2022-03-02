import argparse
import numpy as np

# object-oriented programming style


class in_out:
    """Contains the input and output methods."""

    def __init__(self) -> None:
        self.parse_command_line()

    def parse_command_line(self):
        """Function to parse user input. User input is a float and a string.
        :Returns: area of the circle (float)"""
        parser = argparse.ArgumentParser(
            description="""Program to calculate 
            area of circle. Check -h or --help for options.
            Usage: ./main.py -r 4"""
        )
        parser.add_argument(
            "-r",
            "--radius",
            default=3.0,
            help="Radius of the \
            circle, in cm. \
            Default value: 3.0 cm",
        )
        args = parser.parse_args()
        self.r = float(args.radius)

    def print_out(self, area_out) -> None:
        """Function to print output."""
        if self.r == None:
            raise AttributeError("Radius was not provided!")
        if area_out == None:
            raise AttributeError("Area was not computed!")
        print("Circle with radius r = {:3.2f}cm:".format(self.r))
        print("Area A = {:4.2f}cm2.".format(area_out))


class transform:
    """Contains the data transformation."""

    def __init__(self, r_in) -> None:
        self.r = r_in

    def area_circ(self) -> float:
        """Calculates the area of a circle with given radius.

        :Input: The radius of the circle (float, >=0).
        :Returns: The area of the circle (float)."""
        if self.r < 0:
            raise ValueError("The radius must be >= 0.")
        self.area = np.pi * self.r**2
        return self.area


if __name__ == "__main__":
    """Main function that drives the calculation."""
    # create instance of the i/o object
    obj = in_out()
    # process data
    area_out = transform(obj.r).area_circ()
    # provide output
    obj.print_out(area_out)
