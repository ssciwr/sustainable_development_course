import numpy as np


def area_circ(r_in):
    """Calculates the area of a circle with given radius.

    :Input: The radius of the circle (float, >=0).
    :Returns: The area of the circle (float)."""
    if r_in < 0:
        raise ValueError("The radius must be >= 0.")
    area_out = np.pi * r_in**2
    print("The area of a circle with radius r = {:3.2f}cm\
        is A = {:4.2f}cm2.".format(r_in, area_out))
    return area_out