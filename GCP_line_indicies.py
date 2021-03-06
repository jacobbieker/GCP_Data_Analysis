from __future__ import division
__author__ = 'Jacob Bieker'
import numpy as np
import matplotlib.pyplot as pyplot
import csv

#List of the columns for each data type in the CSV file
redshift = 3 #redshift
l_sigma = 4 #log10(Sigma) of velocity dispersion in km/s
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

'''
create_line_indicies_graph assumes that the data is in CSV format, and that the columns are the same for each of the data sets
'''


def create_line_indices_graph(name_for_graph, x_axis_name='', y_axis_name='', main_data='GCP_spectroscopicdata.csv', column_one_to_graph=None, column_two_to_graph=None, column_one_error_to_graph=None, column_two_error_to_graph=None, color_column=None, num_of_colors=1, bin_size=0.1):
    graph_one_array = []
    graph_two_array = []
    graph_one_array_error = []
    graph_two_array_error = []
    color_graph = []
    min_value = 1.8 #Because of the uncertainty in the measurements for below 1.8 in velocity dispersion
    max_value = 0.0
    f = open(main_data)
    main_csv_file = csv.reader(f)
    next(main_csv_file)
    for line in main_csv_file:
        if line[column_one_to_graph] is not '' and line[column_two_to_graph] is not '':
            graph_one_array.append(float(line[column_one_to_graph]))
        if column_two_to_graph is not None and line[column_two_to_graph] is not '' and line[column_one_to_graph] is not '':
            graph_two_array.append(float(line[column_two_to_graph]))
        if column_one_error_to_graph is not None and line[column_one_to_graph] is not '' and line[column_two_to_graph] is not '':
            graph_one_array_error.append(float(line[column_one_error_to_graph]))
        if column_two_error_to_graph is not None and line[column_two_to_graph] is not '' and line[column_one_to_graph] is not '':
            graph_two_array_error.append(float(line[column_two_error_to_graph]))
        if column_two_error_to_graph is not None and line[column_two_to_graph] is not '' and line[column_one_to_graph] is not '':
            color_graph.append((float(line[color_column])))

    sorted_color_graph = sorted(color_graph)

    print graph_one_array
    print graph_one_array_error
    print graph_two_array
    print graph_two_array_error
    #pyplot.scatter(graph_one_array, graph_two_array)
    pyplot.errorbar(xerr=graph_one_array_error, yerr=graph_two_array_error)
    pyplot.show()
'''
        if second_data is None: #Implies that the rest are empty as well
            x_values = np.arange(min_value, max_value, bin_size)
            fig_col_1 = pyplot.figure(1)
            fig_col_1.scatter(x_values, column_one_to_graph)
            if column_two_to_graph is not None:
                fig_col_2 = pyplot.figure(2)
                fig_col_2.scatter(x_values, column_two_to_graph)
            if column_one_error_to_graph is not None:
                graph_one_array_error.append(float(column_one_error_to_graph))
            if column_two_error_to_graph is not None:
                graph_two_array_error.append(float(column_two_error_to_graph))

        elif third_data is None: #Implies that the rest are empty as well
            x_values = np.arange(min_value, max_value, bin_size)
            fig_col_1 = pyplot.figure(1)
            fig_col_1.scatter(x_values, column_one_to_graph)
            if column_two_to_graph is not None:
                fig_col_2 = pyplot.figure(2)
                fig_col_2.scatter(x_values, column_two_to_graph)

            fig2_col_1 = pyplot.figure(21)
            fig2_col_1.scatter(x_values, column_one_to_graph)
            if column_two_to_graph is not None:
                fig2_col_2 = pyplot.figure(22)
                fig2_col_2.scatter(x_values, column_two_to_graph)
'''



create_line_indices_graph('STest', "Test One", "Test Two", column_one_to_graph=l_sigma, column_two_to_graph=l_h_beta_em, column_one_error_to_graph=e_l_sigma, column_two_error_to_graph=e_l_h_beta_em)