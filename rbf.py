from scipy.interpolate import Rbf
import numpy as np
from pprint import pprint

with open("sensor_data.txt") as textFile:
    lines = [line.strip('\n').split(',') for line in textFile]

x = []
y = []
z = []
d = []
n = len(lines)

i = 0

while i < n:
    x.append(lines[i][0])
    y.append(lines[i][1])
    z.append(lines[i][2])
    d.append(lines[i][3])

    i += 1

rbfi = Rbf(x, y, z, d)  # radial basis function interpolator instance
# coordinates to be interpolated / predicted
xi = input("X coordinate: ")
yi = input("Y coordinate: ")
zi = input("Z coordinate: ")

di = rbfi(xi, yi, zi)   # interpolated values

print("Values for ", xi, yi, zi, " are ", di[0])

# i = 0

# while i < rbfi.N:

#     print("Node {0} X: {1} Y: {2} Z: {3} Value: {4}".format(
#         i, rbfi.xi[0][i], rbfi.xi[1][i], rbfi.xi[2][i], rbfi.di[i]))

#     i += 1
