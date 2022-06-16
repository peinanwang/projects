'''
Peinan Wang 
CS 5001 Spring 2022
Final Project

test_suite.py
'''


import unittest
from data_processing_functions import *
from DemographicData import DemographicData
from Neighbourhood import Neighbourhood
from object_creating_functions import *
from data_analysis_functions import *


VERBOSITY = 3

STRING = "first_line\nsecond_line\n \n\nanother_line!"
LIST_OF_STRINGS = ["first_line", "second_line", " ", "", "another_line!"]

RECENT_CENSUS_YEAR = 2016
OLD_CENSUS_YEAR = 2006

LENGTH = 5001
INDICES_TO_SELECT_2016 = [4, 5, 2594]
INDICES_TO_SELECT_2006 = [6, 424]

STR_0 = '"Male & Female, Total"'
CLEANED_STR_0 = ''
STR_1 = '"12,500"'
CLEANED_STR_1 = '12500'
STR_2 = '" 12,500 "'
CLEANED_STR_2 = ' 12500 '
STR_3 = '"2,300,000"'
CLEANED_STR_3 = '2300000'
STR_4 = '" 2,300,000 "'
CLEANED_STR_4 = ' 2300000 '
STR_5 = '"12500"'
CLEANED_STR_5 = '12500'

LIST_TO_CLEAN = [STR_0, STR_1, STR_2, STR_3, STR_4, STR_5]
CLEANED_LIST = [CLEANED_STR_0, CLEANED_STR_1, CLEANED_STR_2, CLEANED_STR_3,
                CLEANED_STR_4, CLEANED_STR_5]

TO_REMOVE_WHITESPACES = [" 120 ", " hello", "  ", "86 "]
LIST_NO_WHITESPACES = ["120", "hello", "", "86"]


SAMPLE_LINE = "123, 456,789,1011,1213, 1415 "
# list_linedata() will convert SAMPLE_LINE into a list of strings
# if SAMPLE_LINE is from 2016 Census data, the returned list should remove the 
# first two indices and the last two indices
# if SAMPLE LINE is from 2006 Census data, the returend list should remove the
# first index and the last two indices.
LINE_LIST_2016 = ["789", "1011"]  
LINE_LIST_2006 = ["456", "789", "1011"]

SAMPLE_LINE_0 = "A,  B,C , D, E  , F"
SAMPLE_LINE_1 = "111, 222, 333, 444, 555, 666 "
SAMPLE_LINE_2 = "100, 200,  300,400, 500 ,600  "

SAMPLE_DATA_LIST_1 = [["C",   "D"], 
                      ["333", "444"],
                      ["300", "400"]]

SAMPLE_DATA_LIST_2 = [["222", "333", "444"],
                      ["200", "300", "400"]]

SAMPLE_DATA_LIST_3 = [["A",   "B"], 
                      ["333", "444"],
                      ["300", "400"]]

INTEGER_VERSION_DATA_LST_3 = [["A", "B"], 
                             [333, 444],
                             [300, 400]]

URL =\
"https://webtransfer.vancouver.ca/opendata/csv/CensusLocalAreaProfiles2016.csv"


NAME_1 = "sample community 1"
POP_1 = 3000
IMMI_1 = 1000
IMMI_DENSITY_1 = 33.33
DEMO_DATA_1 = DemographicData(NAME_1, RECENT_CENSUS_YEAR, POP_1, IMMI_1)

NAME_2 = NAME_1
POP_2 = 2500
IMMI_2 = 500
IMMI_DENSITY_2 = 20.00
DEMO_DATA_2 = DemographicData(NAME_2, OLD_CENSUS_YEAR, POP_2, IMMI_2)

NAME_3 = "sample community 2"
POP_3 = 3200
IMMI_3 = 1600
IMMI_DENSITY_3 = 50.00
DEMO_DATA_3 = DemographicData(NAME_3, RECENT_CENSUS_YEAR, POP_3, IMMI_3)

NAME_4 = NAME_3
POP_4 = 4000
IMMI_4 = 1200
DEMO_DATA_4 = DemographicData(NAME_4, OLD_CENSUS_YEAR, POP_4, IMMI_4)
IMMI_DENSITY_4 = 30.00

NAME_5 = "sample community 3"
POP_5 = 3150
IMMI_5 = 2000
DEMO_DATA_5 = DemographicData(NAME_5, RECENT_CENSUS_YEAR, POP_5, IMMI_5)
IMMI_DENSITY_5 = 63.49

NAME_6 = NAME_5
POP_6 = 3000
IMMI_6 = 2100
DEMO_DATA_6 = DemographicData(NAME_6, OLD_CENSUS_YEAR, POP_6, IMMI_6)
IMMI_DENSITY_6 = 70.00

NEIGHBOURHOOD_1 = Neighbourhood(NAME_1, DEMO_DATA_1, DEMO_DATA_2)
NEIGHBOURHOOD_2 = Neighbourhood(NAME_3, DEMO_DATA_3, DEMO_DATA_4)
NEIGHBOURHOOD_3 = Neighbourhood(NAME_5, DEMO_DATA_5, DEMO_DATA_6)

OTHER = 10

DECIMAL_PLACES = 2
HUNDRED_PERCENT = 100

NAME_LST = [NAME_1, NAME_3, NAME_5] # list of neighbourhood names
POP_2016_LST = [POP_1,  POP_3,  POP_5] # list of 2016 total population
IMMI_2016_LST = [IMMI_1, IMMI_3, IMMI_5] # list of 2016 immigrant population
POP_2006_LST = [POP_2,  POP_4,  POP_6] # list of 2006 total population
IMMI_2006_LST = [IMMI_2, IMMI_4, IMMI_6] # list of 2006 immigrant population

SAMPLE_DATA = [NAME_LST,
               POP_2016_LST, 
               IMMI_2016_LST,
               POP_2006_LST,
               IMMI_2006_LST]

DEMO_DATA_LST_2016 = [DEMO_DATA_1, DEMO_DATA_3, DEMO_DATA_5]
DEMO_DATA_LST_2006 = [DEMO_DATA_2, DEMO_DATA_4, DEMO_DATA_6]
NEIGHBOURHOOD_LST = [NEIGHBOURHOOD_1, NEIGHBOURHOOD_2, NEIGHBOURHOOD_3]

IMMI_DENSITY_2016_LST = [IMMI_DENSITY_1, IMMI_DENSITY_3, IMMI_DENSITY_5]
IMMI_DENSITY_2006_LST = [IMMI_DENSITY_2, IMMI_DENSITY_4, IMMI_DENSITY_6]


class DataProcessingTest(unittest.TestCase):
    '''
    To test all functions in data_processing_functions.py 
    except for read_file(), which reads url and save web content into a string. 
    We assume read_file() works and will use this function to generate a raw 
    data for some of our tests
    '''
    def test_make_content_list(self):
        # To test if the function can split a string into a list by "\n"

        lst = make_content_list(STRING)
        self.assertEqual(lst, LIST_OF_STRINGS)
    
    def test_select_data(self):
        # To test if the function can take a list and select specified indices

        # create a list of 5000 elements
        lst = []
        for i in range(LENGTH):
            lst.append(i)

        selected_indices_2016 = select_data(lst, RECENT_CENSUS_YEAR)
        selected_indices_2006 = select_data(lst, OLD_CENSUS_YEAR)

        self.assertEqual(selected_indices_2016, INDICES_TO_SELECT_2016)
        self.assertEqual(selected_indices_2006, INDICES_TO_SELECT_2006)
    
    def test_clean_string(self):
        # To test if the function will replace some unwanted patterns in a
        # string with desired patterns
        
        cleaned_str_0 = clean_string(STR_0)
        cleaned_str_1 = clean_string(STR_1)
        cleaned_str_2 = clean_string(STR_2)
        cleaned_str_3 = clean_string(STR_3)
        cleaned_str_4 = clean_string(STR_4)
        cleaned_str_5 = clean_string(STR_5)
        
        self.assertEqual(cleaned_str_0, CLEANED_STR_0)
        self.assertEqual(cleaned_str_1, CLEANED_STR_1)
        self.assertEqual(cleaned_str_2, CLEANED_STR_2)
        self.assertEqual(cleaned_str_3, CLEANED_STR_3)
        self.assertEqual(cleaned_str_4, CLEANED_STR_4)
        self.assertEqual(cleaned_str_5, CLEANED_STR_5)
    
    def test_clean_data(self):
        # To test if the function will process a list of strings and apply 
        # the clean_string() to replace unwanted patterns in every element

        lst = LIST_TO_CLEAN
        clean_data(lst)
        self.assertEqual(lst, CLEANED_LIST)
    
    def test_remove_whitespace(self):
        lst = TO_REMOVE_WHITESPACES
        remove_whitespaces(lst)
        self.assertEqual(lst, LIST_NO_WHITESPACES)

    def test_list_linedata(self):
        # To test if the function can convert a single string to a list of 
        # strings as specified. 
        
        self.assertEqual(LINE_LIST_2016, 
                         list_linedata(SAMPLE_LINE, RECENT_CENSUS_YEAR))
        self.assertEqual(LINE_LIST_2006, 
                         list_linedata(SAMPLE_LINE, OLD_CENSUS_YEAR))     


    def test_make_data_list(self):
        # To test if the function can take a list of strings and make
        # a list of list as expected. 
        sample_data_2016 = [SAMPLE_LINE_0, SAMPLE_LINE_1, SAMPLE_LINE_2]
        sample_data_2006 = [SAMPLE_LINE_1, SAMPLE_LINE_2]

        self.assertEqual(SAMPLE_DATA_LIST_1, 
                         make_data_list(sample_data_2016, RECENT_CENSUS_YEAR))
        self.assertEqual(SAMPLE_DATA_LIST_2, 
                         make_data_list(sample_data_2006, OLD_CENSUS_YEAR))  
        

    def test_process_data(self):

        # Test if the function can parse 2016 Census data successfully
        web_text_2016 = read_file(URL)
        raw_data_2016 = make_content_list(web_text_2016)
        selected_data_2016 = select_data(raw_data_2016, RECENT_CENSUS_YEAR)
        clean_data(selected_data_2016)
        expected_data_list_2016 = make_data_list(selected_data_2016, 
                                                 RECENT_CENSUS_YEAR)

        actual_data_list_2016 = process_data(URL, RECENT_CENSUS_YEAR)

        self.assertEqual(expected_data_list_2016, actual_data_list_2016)

        # Test if the function can parse 2006 Census data successfully
        web_text_2006 = read_file(URL)
        raw_data_2006 = make_content_list(web_text_2006)
        selected_data_2006 = select_data(raw_data_2006, OLD_CENSUS_YEAR)
        clean_data(selected_data_2006)
        expected_data_list_2006 = make_data_list(selected_data_2006, 
                                                 OLD_CENSUS_YEAR)

        actual_data_list_2006 = process_data(URL, OLD_CENSUS_YEAR)

        self.assertEqual(expected_data_list_2006, actual_data_list_2006)
        

    def test_convert_str_to_int(self):
        # To test if the function can take a data list (list or lists) and
        # convert all numbers from string type into integers
        convert_str_to_int(SAMPLE_DATA_LIST_3)
        self.assertEqual(INTEGER_VERSION_DATA_LST_3, SAMPLE_DATA_LIST_3) 
                     

class testDemographicData(unittest.TestCase):
    def test_init(self):
        self.assertEqual(DEMO_DATA_1.neighbourhood_name, NAME_1)
        self.assertEqual(DEMO_DATA_1.year, RECENT_CENSUS_YEAR)
        self.assertEqual(DEMO_DATA_1.total_population, POP_1)
        self.assertEqual(DEMO_DATA_1.immi_population, IMMI_1)

    def test_str(self):
        expected_str = f"The {RECENT_CENSUS_YEAR} demographic data of " +\
                       f"{NAME_1}"
        self.assertEqual(expected_str, str(DEMO_DATA_1))

    def test_eq(self):
        self.assertFalse(DEMO_DATA_1 == DEMO_DATA_3)
        self.assertTrue(DEMO_DATA_1 == DEMO_DATA_2)
        self.assertFalse(DEMO_DATA_1 == OTHER)
    
    def test_calculate_immi_density(self):
        self.assertEqual(IMMI_DENSITY_1,
                         DEMO_DATA_1.calculate_immi_density())
        self.assertEqual(IMMI_DENSITY_2,
                         DEMO_DATA_2.calculate_immi_density())                        


class testNeighbourhood(unittest.TestCase):
    def test_init(self):
        self.assertEqual(NEIGHBOURHOOD_1.name, NAME_1)
        self.assertEqual(NEIGHBOURHOOD_1.demodata_2016, DEMO_DATA_1)
        self.assertEqual(NEIGHBOURHOOD_1.demodata_2006, DEMO_DATA_2)

    def test_str(self):
        expected_str = f"The population of {NAME_1} is {POP_1} (2016 Census)."
        self.assertEqual(expected_str, str(NEIGHBOURHOOD_1))

    def test_eq(self):
        self.assertFalse(NEIGHBOURHOOD_1 == NEIGHBOURHOOD_2)
        self.assertTrue(NEIGHBOURHOOD_1 == NEIGHBOURHOOD_3)
        self.assertFalse(NEIGHBOURHOOD_1 == OTHER)
    
    def test_calculate_population_growth(self):
        percentage = (POP_1 - POP_2) / POP_2 * HUNDRED_PERCENT
        pop_growth = round(percentage, DECIMAL_PLACES)
        self.assertEqual(pop_growth,
                         NEIGHBOURHOOD_1.calculate_population_growth())

    def test_calculate_immigration_growth(self):
        percentage = (IMMI_1 - IMMI_2) / IMMI_2 * HUNDRED_PERCENT
        immi_growth = round(percentage, DECIMAL_PLACES)
        self.assertEqual(immi_growth,
                         NEIGHBOURHOOD_1.calculate_immigration_growth())

    def test_calculate_immigrant_density_growth(self):
        percentage = (IMMI_DENSITY_1 - IMMI_DENSITY_2) / IMMI_DENSITY_2 \
                      * HUNDRED_PERCENT
        immi_desnsity_growth = round(percentage, DECIMAL_PLACES)
        self.assertEqual(immi_desnsity_growth,
                         NEIGHBOURHOOD_1.calculate_immigrant_density_growth())


class ObjectCreatingTest(unittest.TestCase):
    '''
    To test all functions in object_creating_functions.py, which takes the 
    data (a list of list) and creates a list of Neighbourhood instances.
    '''
    def test_list_2016_demographic_data(self):
        self.assertEqual(DEMO_DATA_LST_2016, 
                         list_2006_demographic_data(SAMPLE_DATA))

    def test_list_2006_demographic_data(self):
        self.assertEqual(DEMO_DATA_LST_2006, 
                         list_2006_demographic_data(SAMPLE_DATA))

    def test_list_neighbourhoods(self):
        self.assertEqual(NEIGHBOURHOOD_LST, 
                         list_neighbourhoods(SAMPLE_DATA))


class DataAnalysisTest(unittest.TestCase):
    '''
    To test all functions in data_analysis_functions.py, which takes a list of 
    Neighbourhood objects and analyzes dempgraphic trends
    '''

    def test_get_immigrant_density_list(self):
        immi_density_2016_lst \
        = get_immigrant_density_lst(NEIGHBOURHOOD_LST, RECENT_CENSUS_YEAR)

        immi_density_2006_lst \
        = get_immigrant_density_lst(NEIGHBOURHOOD_LST, OLD_CENSUS_YEAR)

        self.assertEqual(IMMI_DENSITY_2016_LST, immi_density_2016_lst)
        self.assertEqual(IMMI_DENSITY_2006_LST, immi_density_2006_lst)


    def test_find_demographic_trend(self):
        pop_growth_1 = NEIGHBOURHOOD_1.calculate_population_growth()
        pop_growth_2 = NEIGHBOURHOOD_2.calculate_population_growth()
        pop_growth_3 = NEIGHBOURHOOD_3.calculate_population_growth()
        pop_growth_lst = [pop_growth_1, pop_growth_2, pop_growth_3]

        immi_growth_1 = NEIGHBOURHOOD_1.calculate_immigration_growth()
        immi_growth_2 = NEIGHBOURHOOD_2.calculate_immigration_growth()
        immi_growth_3 = NEIGHBOURHOOD_3.calculate_immigration_growth()   
        immi_growth_lst = [immi_growth_1, immi_growth_2, immi_growth_3]

        immi_density_growth_1 \
        = NEIGHBOURHOOD_1.calculate_immigrant_density_growth()
        immi_density_growth_2 \
        = NEIGHBOURHOOD_2.calculate_immigrant_density_growth()
        immi_density_growth_3 \
        = NEIGHBOURHOOD_3.calculate_immigrant_density_growth()
        immi_density_growth_lst = [immi_density_growth_1,
                                   immi_density_growth_2,
                                   immi_density_growth_3]
        
        demographic_trends = (pop_growth_lst, 
                              immi_growth_lst, 
                              immi_density_growth_lst)
        
        self.assertEqual(demographic_trends,
                         find_demographic_trend(NEIGHBOURHOOD_LST))


def main():

     unittest.main(verbosity = VERBOSITY)


if __name__ == "__main__":
    main()
