from scipy.interpolate import Rbf
import numpy as np
from pprint import pprint
import json
import itertools


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
    xi = np.linspace(-n+1, n-1, a)
    yi = np.linspace(0, 0, a**2)
    zi = np.linspace(-n+1, n-1, a)

    cartesianList = list(itertools.product(xi, zi))

    xic, zic = zip(*cartesianList)

    # print(cartesianList)

    di = rbfi(xic, yi, zic)   # interpolated values

    i = 0
    dataList = []

    print(di)

    with open("static/sensor_data.json", "w", newline='') as f:

        while i < a**2:
            interpolation = {'x': xic[i], 'z': zic[i], 'val': round(di[i], 2)}
            dataList.append(interpolation)

            i += 1

        json.dump(dataList, f)

    return di
