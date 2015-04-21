from __future__ import division
__author__ = 'Jacob'
import math
import os
import sys
import csv
import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib.mlab as mlab

try:
    bin_size = float(raw_input('Desired Bin Size: '))
except ValueError:
    print "Not a number"

data = 'GCP_spectroscopicdata.csv'
#bin_size = 0.1
redshift_array = []
bins = np.arange(0.0, 2.1, bin_size)

f = open(data)
csv_file = csv.reader(f)
next(csv_file)
for line in csv_file:
    print line[0]
    print line[3]
    redshift_array.append(float(line[3]))


pyplot.hist(redshift_array, bins)
pyplot.title("Redshift of Field Galaxies with Bin Size = " + str(bin_size))
pyplot.xlabel("Redshift (z)")
pyplot.ylabel("Number (N)")
pyplot.savefig("Redshift_bin_" + str(bin_size) + ".png")
pyplot.show()