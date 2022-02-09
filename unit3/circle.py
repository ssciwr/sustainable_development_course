import numpy as np


def area_circ(r_in):
    """Calculates the area of a circle with given radius.

    :Input: The radius of the circle (float, >=0).
    :Returns: The area of the circle (float)."""
    if r_in < 0:
        raise ValueError("The radius must be >= 0.")
    area_out = np.pi * r_in**2
    print("Circle with radius r = {:3.2f}cm:".format(r_in))
    print("Area A = {:4.2f}cm2.".format(area_out))
    return area_out