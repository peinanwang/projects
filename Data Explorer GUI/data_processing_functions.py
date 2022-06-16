'''
Peinan Wang 
CS 5001 Spring 2022
Final Project

data_processing_functions.py
'''


import re
import requests


RECENT_CENSUS_YEAR = 2016
OLD_CENSUS_YEAR = 2006

ROWS_TO_SELECT_2016 = [4, 5, 2594] # we only need 3 rows in Census 2016 table
ROWS_TO_SELECT_2006 = [6, 424] # we only need 2 rows in Census 2006 table

DELIMITER = ","


PATTERN_0 = '"Male & Female, Total"'
REPLACE_0 = ''

PATTERN_1 = '("\d+),(\d+")'   # e.g. "12,500" -- 12500
REPLACE_1 = r'\1\2'

PATTERN_2 = '(" \d+),(\d+ ")' # e.g. " 12,500 " -- 12500
REPLACE_2 = r'\1\2'  

PATTERN_3 = '("\d+),(\d+),(\d+")'  # e.g. "2,300,000" -- 2300000
REPLACE_3 = r'\1\2\3'

PATTERN_4 = '(" \d+),(\d+),(\d+ ")' # e.g. " 2,300,000 " -- 2300000
REPLACE_4 = r'\1\2\3'

PATTERN_5 = '"' # e.g. "5000" -- 5000
REPLACE_5 = ""

TO_CLEAN = {PATTERN_0 : REPLACE_0,\
            PATTERN_1 : REPLACE_1,\
            PATTERN_2 : REPLACE_2,\
            PATTERN_3 : REPLACE_3,\
            PATTERN_4 : REPLACE_4,\
            PATTERN_5 : REPLACE_5}

START_COLUMN_2016_DATA = 2
START_COLUMN_2006_DATA = 1
SKIPPED_COLUMN = 2 # the last two columns in the csv table will not be used.


def read_file(url):
    '''
    Function: read_file
    Purpose:  take the URL and read web content into a single string
    Param:    url - a string
    Return:   a string
              When HTTPError or ConnectionError is raised, print the 
              information to the terminal and exit the program
    '''  
    try:
        web_content = requests.get(url)
        web_text = web_content.text
        return web_text
    
    except requests.HTTPError:
        print("The URL is not valid")
        exit()
        
    except requests.ConnectionError:
        print("There is a problem accessing the website")
        exit()


def make_content_list(raw_data):
    '''
    Function: make_content_list
    Purpose:  take the raw data (a string) and make a list of lines(strings)
    Param:    a string
    Return:   a list of strings
    '''
    content_list = raw_data.split("\n")

    return content_list


def select_data(content_list, year):
    '''
    Function: select_data
    Purpose:  take the list of lines(strings) from either 2016 or 2006 census 
              data and select lines as needed
    Param:    - a list of strings
              - year - an integer, either 2006 or 2016
    Return:   - a list of selected strings
    '''

    selected_data = []

    if year == RECENT_CENSUS_YEAR:
        rows_to_select = ROWS_TO_SELECT_2016
    elif year ==OLD_CENSUS_YEAR:
        rows_to_select = ROWS_TO_SELECT_2006

    for row_number in rows_to_select:
        selected_data.append(content_list[row_number])
    
    return selected_data


def clean_string(string):
    '''
    Function: clean_string
    Purpose:  replace some unwanted patterns in a string with desired patterns
    Param:    a string
    Return:   a string
    '''
    string_to_clean = string

    for pattern in TO_CLEAN:
        replaced_with = TO_CLEAN[pattern]
        cleaned_string = re.sub(pattern, replaced_with, string_to_clean)
        string_to_clean = cleaned_string

    return cleaned_string


def clean_data(data):
    '''
    Function: clean_data
    Purpose:  take a list of strings and clean each string by replace
              unwanted patterns
    Param:    a list of strings
    Return:   a list of strings
    '''
    for i in range(len(data)):
        str = data[i]   
        cleaned_str = clean_string(str)
        data[i] = cleaned_str


def remove_whitespaces(string_list):
    '''
    Function: remove_whitespaces
    Purpose:  remove the leading and trailing whitespaces of each string
    Param:    a string list
    Return:   none
    '''
    for i in range(len(string_list)):
        str = string_list[i]
        string_list[i] = str.strip()


def list_linedata(linedata, year):
    '''
    Function: list_linedata
    Purpose:  convert a line of data from a single string to a list of strings
    Param:    - linedata - a string
              - year - an integer, either 2006 or 2016            
    Return:   a list of strings
    '''
    string_list = linedata.split(DELIMITER)
    
    remove_whitespaces(string_list)

    if year == 2016:
        start_column = START_COLUMN_2016_DATA
    elif year == 2006:
        start_column = START_COLUMN_2006_DATA

    list = []

    for i in range(start_column, len(string_list) - SKIPPED_COLUMN):
        to_add = string_list[i]
        list.append(to_add)
    
    return list


def make_data_list(data, year):
    '''
    Function: make_data_list
    Purpose:  clean the census data and save data as a list of string-lists
    Param:    - data - a list of strings
              - year - an integer, either 2006 or 2016
    Return:   a list of lists
    '''
    data_list = []

    for i in range(len(data)):
        row = list_linedata(data[i], year)
        data_list.append(row)
    
    return data_list


def process_data(url, year):
    '''
    Function: process_data
    Purpose:  take the csv url and the cencus year and parse the data into 
              a list of string-lists
    Param:    - url - a string
              - year - an integer, either 2006 or 2016
    Return:   a list of lists containing all the data needed
    '''
                         
    web_text = read_file(url)
    
    raw_data = make_content_list(web_text)

    selected_data = select_data(raw_data, year)

    clean_data(selected_data)

    data_list = make_data_list(selected_data, year)

    return data_list


def convert_str_to_int(data_list):
    '''
    Function: convert_str_to_int
    Purpose:  take the data list (a list of lists) can convert all numbers 
              from text to integer
    Param:    a list of lists
    Return:   a list of lists
    '''
    for i in range(1, len(data_list)):

        row = data_list[i]

        for j in range(len(row)):
            row[j] = int(row[j])
