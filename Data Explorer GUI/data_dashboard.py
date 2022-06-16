'''
Peinan Wang 
CS 5001 Spring 2022
Final Project

data_dashboard.py
'''


from data_processing_functions import process_data, convert_str_to_int

from object_creating_functions import list_neighbourhoods

from data_analysis_functions import get_immigrant_density_lst,\
                                    find_demographic_trend

from gui_functions import data_viewer


CENSUS_DATA_2016 =\
"https://webtransfer.vancouver.ca/opendata/csv/CensusLocalAreaProfiles2016.csv"

CENSUS_DATA_2006 =\
"https://webtransfer.vancouver.ca/opendata/csv/CensusLocalAreaProfiles2006.csv"

RECENT_CENSUS_YEAR = 2016
OLD_CENSUS_YEAR = 2006

NEIGHBOURHOOD_INDEX = 0
POP_2016_INDEX = 1
IMMI_2016_INDEX = 2
POP_2006_INDEX = 3
IMMI_2006_INDEX = 4


def main():

    # select and clean the data
    data_list = process_data(CENSUS_DATA_2016, RECENT_CENSUS_YEAR)
    data_list_2006 = process_data(CENSUS_DATA_2006, OLD_CENSUS_YEAR) 
    data_list.extend(data_list_2006)

    convert_str_to_int(data_list)

    # prepare a list of neighbourhood objects
    neighbourhood_list = list_neighbourhoods(data_list)

    # prepare columns for the data frame
    # the data frame will be used to generate bar charts
    names = data_list[NEIGHBOURHOOD_INDEX]
    pop_2016_lst = data_list[POP_2016_INDEX]
    pop_2006_lst = data_list[POP_2006_INDEX]
    immi_pop_2016_lst = data_list[IMMI_2016_INDEX]
    immi_pop_2006_lst = data_list[IMMI_2006_INDEX]

    immi_density_2016_lst \
    = get_immigrant_density_lst(neighbourhood_list, RECENT_CENSUS_YEAR)

    immi_density_2006_lst \
    = get_immigrant_density_lst(neighbourhood_list, OLD_CENSUS_YEAR)
        
    pop_growth_lst, immi_growth_lst, immi_density_growth_lst \
    = find_demographic_trend(neighbourhood_list)

    # start the GUI and display bar charts based on the user's selection
    data_viewer(names, pop_2006_lst, pop_2016_lst, immi_pop_2006_lst,
                immi_pop_2016_lst, immi_density_2006_lst,
                immi_density_2016_lst, pop_growth_lst, immi_growth_lst,
                immi_density_growth_lst)


if __name__ == "__main__":
    main()
