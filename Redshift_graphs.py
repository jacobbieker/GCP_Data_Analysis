from __future__ import division
__author__ = 'Jacob'
import math
import os
import sys
import csv
import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib.mlab as mlab

#List of the columns for each data type in the CSV file
redshift_data = 3 #redshift
l_sigma = 4 #velocity dispersion in km/s
e_l_sigma = 5 #uncertainty in l_sigma
cn_3883 = 6 #CN3883 index fully corrected
e_cn_3883 = 7 #error in cn_3883
d_4000 = 8 #D4000 index fully corrected
e_d_4000 = 9 #error in d_4000
lc_4668 = 10 #log10(C4668) index fully corrected
e_lc_4668 = 11 #error in lc_4668
l_mgb = 12 #log10(Mgb) index fully corrected
e_l_mgb = 13 #error in l_mgb
e_width_OII = 16 #equivalent width of emission in [OII]3727
e_e_width_OII = 17 #error in e_width_OII
l_h_zeta_a = 18 #log10(HzetaA) index fully corrected
e_l_h_zeta_a = 19 #error in l_h_zeta_a
l_h_dg_a = 20 #Magnitude defined average of HdeltaA and HgammaA
e_l_h_dg_a = 21 #error in l_h_dg_a
l_fe_4383 = 22 #log10(Fe4383) index fully corrected
e_l_fe_4383 = 23 #error in l_fe_4383
l_h_beta_em = 24 #log10(Hbeta_G) index fully corrected
e_l_h_beta_em = 25 #error in l_h_beta_em
l_fe = 26 #log10(Fe)=log((Fe5270+F5335)/2) index fully corrected
e_l_fe = 27 #error in l_fe


def create_histogram(name_for_graph, data, column_to_graph, bin_size):
    bins = np.arange(0.0, 2.1, bin_size)
    graph_array = []
    f = open(data)
    csv_file = csv.reader(f)
    next(csv_file)
    for line in csv_file:
        graph_array.append(float(line[column_to_graph]))

    pyplot.hist(graph_array, bins)
    pyplot.title(name_for_graph + " Field Galaxies with Bin Size = " + str(bin_size))
    pyplot.xlabel(name_for_graph)
    pyplot.ylabel("Number (N)")
    pyplot.savefig(name_for_graph + "_bin_" + str(bin_size) + ".png")
    pyplot.show()

try:
     name_for_graph_input = str(raw_input("Name For Graph: "))
except ValueError:
    print "Not a String"

try:
     column_to_graph_input = int(raw_input("Column to Graph: "))
except ValueError:
    print "Not a Number"

try:
    bin_size_input = float(raw_input('Desired Bin Size: '))
except ValueError:
    print "Not a number"

data = 'GCP_spectroscopicdata.csv'
create_histogram(name_for_graph_input, data, column_to_graph_input, bin_size_input)

