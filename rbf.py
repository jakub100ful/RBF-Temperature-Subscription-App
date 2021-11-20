from scipy.interpolate import Rbf
import numpy as np
from pprint import pprint
import csv


def getTempData():

    with open("sensor_data.txt") as textFile:
        lines = [line.strip('\n').split(',') for line in textFile]

    x = []
    y = []
    z = []
    d = []

    n = len(lines)
    a = (n*2)-1

    i = 0

    while i < n:
        x.append(lines[i][0])
        y.append(lines[i][1])
        z.append(lines[i][2])
        d.append(lines[i][3])

        i += 1

    rbfi = Rbf(x, y, z, d)  # radial basis function interpolator instance
    # coordinates to be interpolated / predicted

    i = 0
    xi = []
    yi = []
    zi = []

    while i < a:
        xi = np.append(xi, np.linspace(-n+1, n-1, a))
        yi = np.append(yi, np.linspace(0, 0, a))
        zi = np.append(zi, np.linspace(-n+1, n-1, a))

        i += 1

    di = rbfi(xi, yi, zi)   # interpolated values

    i = 0

    with open("static/sensor_data.csv", "w", newline='') as f:

        writer = csv.writer(f)

        while i < a**2:
            f.write("{},{},{}".format(xi[i], zi[i], di[i]))
            f.write("\n")

            i += 1

    return di
