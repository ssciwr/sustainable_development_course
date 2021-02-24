#!/usr/bin/env python3
# package data_analysis
# brief Contains tests for profiler and libraries

# By ISU, 01/21
# This package handles the analysis of the measured data.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from time import time


def check_libraries(imax):
    """function to test the libraries"""
    testarr = np.zeros((imax, imax))
    testdf = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                          columns=['a', 'b', 'c'])
    print("Testing pandas")
    print(testdf.head(2))
    xplot = np.arange(imax)
    plt.plot(xplot, testarr[0])
    plt.title("Testing matplotlib")
    plt.show()
    sns.set()
    plt.plot(xplot, testarr[0])
    plt.title("Testing seaborn")
    plt.show()
    return

def main(imax):
    """Main function to test the profiler.

    Args:
        imax (integer): array dimension"""
    start = time()
    check_libraries(imax)
    end = time()
    print('The script took {:.2f} seconds to run!'.format(end - start))
    return

if __name__ == "__main__":
    main(50)
