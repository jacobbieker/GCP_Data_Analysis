from __future__ import division
__author__ = 'Jacob'
import math
import os
import csv
import numpy as np
import matplotlib as pyplot

data = 'GCP_spectroscopicdata.csv'
bin_size = 0.1
redshift_array = []
bins = np.arange(0, 1.2, bin_size)

f = open(data)
csv_file = csv.reader(f)
next(csv_file)
for line in csv_file:
    print float(line[3])
    redshift_array.append(float(line[3]))


pyplot.hist(redshift_array, bins=0.1)
hist, edges = np.histogram(redshift_array, bins=0.1)
width = 0.7 * (edges[1] - edges[0])
center = (edges[:-1] + edges[1:])/2
pyplot.bar(center, hist, align='center', width=width)
pyplot.show()