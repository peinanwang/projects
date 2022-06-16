'''
Peinan Wang 
CS 5001 Spring 2022
Final Project

object_creating_functions.py
'''


from Neighbourhood import Neighbourhood
from DemographicData import DemographicData


MOST_RECENT_CENSUS = 2016
OLD_CENSUS = 2006

NEIGHBOURHOOD_INDEX = 0
POP_2016_INDEX = 1
IMMI_2016_INDEX = 2
POP_2006_INDEX = 3
IMMI_2006_INDEX = 4


def list_2016_demographic_data(data):
    '''
    Function: list_2016_demographic_data
    Purpose:  create DemographicData instances for all neighbourhoods
    Param:    a list of list
    Return:   a list of DemographicData instances
    '''
    demographics2016_list = []

    for i in range(len(data[0])):

        neighbourhood_name = data[NEIGHBOURHOOD_INDEX][i]
        year = MOST_RECENT_CENSUS
        total_population = data[POP_2016_INDEX][i]
        immi_population = data[IMMI_2016_INDEX][i]

        demo_data = DemographicData(neighbourhood_name, 
                                    year, total_population,
                                    immi_population)
       
        demographics2016_list.append(demo_data)
    
    return demographics2016_list


def list_2006_demographic_data(data):
    '''
    Function: list_2006_demographic_data
    Purpose:  create DemographicData instances for all neighbourhoods
    Param:    a list of list
    Return:   a list of DemographicData instances
    '''
    demographics2006_list = []

    for i in range(len(data[0])):

        neighbourhood_name = data[NEIGHBOURHOOD_INDEX][i]
        year = OLD_CENSUS
        total_population = data[POP_2006_INDEX][i]
        immi_population = data[IMMI_2006_INDEX][i]

        demo_data = DemographicData(neighbourhood_name, 
                                    year,
                                    total_population,
                                    immi_population)

        demographics2006_list.append(demo_data)
    
    return demographics2006_list


def list_neighbourhoods(data):
    '''
    Function: list_neighbourhoods
    Purpose:  create a list of the Neighbourhood instances
    Param:    a list of list
    Return:   a list of Neighbourhood instances
    '''
    demographic2016_list = list_2016_demographic_data(data)
    demographic2006_list = list_2006_demographic_data(data)
    
    neighbourhood_list = []

    for i in range(len(data[0])):

        name = data[NEIGHBOURHOOD_INDEX][i]
        demo_data_2016 = demographic2016_list[i]
        demo_data_2006 = demographic2006_list[i]
        neighbourhood = Neighbourhood(name, demo_data_2016, demo_data_2006)
        neighbourhood_list.append(neighbourhood)
    
    return neighbourhood_list
