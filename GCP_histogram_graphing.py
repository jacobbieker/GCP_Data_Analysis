from __future__ import division
__author__ = 'Jacob Bieker'
import csv
import numpy as np
import matplotlib.pyplot as pyplot

#List of the columns for each data type in the CSV file
redshift = 3 #redshift
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
    max_bin = 0.0
    min_bin = 0.0
    graph_array = []
    f = open(data)
    csv_file = csv.reader(f)
    next(csv_file)
    for line in csv_file:
        graph_array.append(float(line[column_to_graph]))
        if float(line[column_to_graph]) > max_bin:
            max_bin = float(line[column_to_graph]) + bin_size
        if float(line[column_to_graph]) < min_bin:
            min_bin = float(line[column_to_graph])

    bins = np.arange(min_bin, max_bin, bin_size)
    pyplot.hist(graph_array, bins)
    pyplot.title(name_for_graph + " For Field Galaxies with Bin Size = " + str(bin_size))
    pyplot.xlabel(name_for_graph)
    pyplot.ylabel("Number (N)")
    pyplot.savefig(name_for_graph + "_bin_" + str(bin_size) + ".png")
    pyplot.show()

try:
     name_for_graph_input = str(raw_input("Name For Graph: "))
except ValueError:
    print "Not a String"

print ("Columns available to graph: " + '\n' + "Redshift: " + str(redshift) + '\n' + "Sigma: " + str(l_sigma) + '\n' + "CN3883: " + str(cn_3883) + '\n' + "D4000: " + str(d_4000) + '\n' + "LC4668: " + str(lc_4668) + '\n' + "MGB: " + str(l_mgb) + '\n' + "Equiv. Width OII: " + str(e_width_OII) + '\n' + "H zeta A: " + str(l_h_zeta_a) + '\n' + "H dg A: " + str(l_h_dg_a) + '\n' + "Fe4383: " + str(l_fe_4383) + '\n' + "H beta G: " + str(l_h_beta_em) + '\n' + "Fe: " + str(l_fe))

try:
     column_to_graph_input = int(raw_input("Column to Graph: "))
except ValueError:
    print "Not a Number"

try:
    bin_size_input = float(raw_input('Desired Bin Size: '))
except ValueError:
    print "Not a number"

data_file = 'GCP_spectroscopicdata.csv'
create_histogram(name_for_graph_input, data_file, column_to_graph_input, bin_size_input)

