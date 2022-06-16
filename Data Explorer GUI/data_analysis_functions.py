'''
Peinan Wang 
CS 5001 Spring 2022
Final Project

data_analysis_functions.py
'''


RECENT_CENSUS_YEAR = 2016
OLD_CENSUS_YEAR = 2006


def get_immigrant_density_lst(neighbourhood_list, year):
    '''
    Function: get_immigrant_density_lst
    Purpose:  take a list of Neighbourhood instances and create a list of
              the immigrant density of each neighbourhood. The data can be from
              either the 2006 census data or the 2016 census data
    Param:    - a list of Neighbourhood instances
              - year; either 2006 ot 2016
    Return:   a list of immigrant density
    '''
    immi_density_lst = []

    if year == RECENT_CENSUS_YEAR:
        for neighbourhood in neighbourhood_list:
            immi_density = neighbourhood.demodata_2016.calculate_immi_density()
            immi_density_lst.append(immi_density)

    elif year == OLD_CENSUS_YEAR:
        for neighbourhood in neighbourhood_list:
            immi_density = neighbourhood.demodata_2006.calculate_immi_density()
            immi_density_lst.append(immi_density)

    return immi_density_lst


def find_demographic_trend(neighbourhood_list):
    '''
    Function: find_demographic_trend
    Purpose:  take a list of Neighbourhood instances and analyze the 
              demographic trend of each neighbourhood
    Param:    a list of Neighbourhood instances
    Return:   three lists showing each neighbourhood's demographic trend
              in total population, immigrant population, and immigrant density
    '''
    pop_growth_list = []
    immi_growth_list = []
    immi_density_growth_list = []

    for neighbourhood in neighbourhood_list:

        pop_growth = neighbourhood.calculate_population_growth()
        immi_growth = neighbourhood.calculate_immigration_growth()
        immi_density_growth \
            = neighbourhood.calculate_immigrant_density_growth()

        pop_growth_list.append(pop_growth)
        immi_growth_list.append(immi_growth)
        immi_density_growth_list.append(immi_density_growth)

    return (pop_growth_list,
           immi_growth_list,
           immi_density_growth_list)
