'''
Peinan Wang 
CS 5001 Spring 2022
Final Project

graphing_functions.py
'''


import matplotlib.pyplot as plt
import pandas as pd


START_COLUMN_AX1 = 1
END_COLUMN_AX1 = 3
COLUMN_AX2 = 3

WIDTH = 9
HEIGHT = 5

GRAPH_HEADER_1 = ("Neighbhourhood", "2006 Census Population", 
            "2016 Census Population", "Total Population Growth %")

GRAPH_HEADER_2 = ("Neighbhourhood", "2006 Immigrant Population", 
            "2016 Immigrant Population", "Immigrant Population Growth %")

GRAPH_HEADER_3 = ("Neighbhourhood", "2006 Immigrant Density", 
            "2016 Immigrant Density", "Immigrant Density Growth %")

GRAPH_1A = "Total Population"
GRAPH_1B = "Demographic Trend - Total Population Change"
GRAPH_2A = "Immigrant Population"
GRAPH_2B = "Demographic Trend - Immigrant Population Change"
GRAPH_3A = "Immigrant Density"
GRAPH_3B = "Demographic Trend - Immigrant Density Change"

OPTION_1 = "1"  
OPTION_2 = "2" 
OPTION_3 = "3" 


def make_bar_graph_from_data_frame(df, xticklabels, title1, title2):
    '''
    Function: make_bar_graph_from_data_frame
    Purpose:  create two bar graph subplots
    Param:    - df, a data frame
              - xticklables, a list of strings
              - title1, the title for the first graph
              - title2, the title for the second graph
    Return:   none
    '''

    figure1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, 
                                       figsize=(WIDTH, HEIGHT))

    columns = df.columns.values

    df[columns[START_COLUMN_AX1:END_COLUMN_AX1]].plot(kind='bar', 
                                                      legend=True, 
                                                      ax=ax1)

    df[columns[COLUMN_AX2]].plot(kind='bar', legend=True, ax=ax2)

    ax1.set_xticklabels(xticklabels)
    ax1.set_title(title1)
    ax2.set_title(title2)

    # rotate xtick labels by 30 degrees and right align them
    figure1.autofmt_xdate()

    # show the plot without blocking code execution
    plt.show(block=False)


def create_graph(graph_option, names, pop_2006_lst, pop_2016_lst, 
                 immi_pop_2006_lst, immi_pop_2016_lst, immi_density_2006_lst,
                 immi_density_2016_lst, pop_growth_lst, immi_growth_lst,
                 immi_density_growth_lst):
    '''
    Function: create_graph
    Purpose:  create graphs based on the graph option
    Param:    - graph option: either "1", "2", or "3"
              - names; the list of neighbhourhood names
              - pop_2006_lst; list of 2006 population
              - pop_2016_lst; list of 2016 population
              - immi_pop_2006_lst: list of 2006 immigrant population
              - immi_pop_2016_lst: list of 2016 immigrant population
              - immi_density_2006_lst: list of 2006 immigrant density 
              - immi_density_2016_lst: list of 2016 immigrant density
              - pop_growth_lst: list of population change %
              - immi_growth_lst: list of immigrant population change %
              - immi_density_growth_lst: list of immigrant density change %
    Return:   - a list of selected strings
    '''
    if graph_option == OPTION_1:
        data = (names, pop_2006_lst, pop_2016_lst, pop_growth_lst)
        header = GRAPH_HEADER_1
        title_a = GRAPH_1A
        title_b = GRAPH_1B
    elif graph_option == OPTION_2:
        data = (names, immi_pop_2006_lst, immi_pop_2016_lst, immi_growth_lst)
        header = GRAPH_HEADER_2
        title_a = GRAPH_2A
        title_b = GRAPH_2B
    elif graph_option == OPTION_3:
        data = (names, immi_density_2006_lst, 
                immi_density_2016_lst, immi_density_growth_lst)
        header = GRAPH_HEADER_3
        title_a = GRAPH_3A
        title_b = GRAPH_3B

    data_dictionary = dict(zip(header, data))

    data_frame = pd.DataFrame(data_dictionary)

    column_to_sort = data_frame.columns[3]

    sorted_df = data_frame.sort_values(by=column_to_sort, ascending=False)

    label_column = sorted_df.columns[0]

    xticklabels = sorted_df[label_column].tolist()
         
    make_bar_graph_from_data_frame(sorted_df, 
                                   xticklabels,
                                   title_a,
                                   title_b)
