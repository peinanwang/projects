'''
get_data_from_file.py

This file processes the csv flight data and creates matrices for flight time
and flight price
'''

import pandas as pd

SIZE = 11
TIME_ROW = 2
TIME_COL = 2
PRICE_ROW = 17
PRICE_COL = 2

def parse_data(filename):
    '''
    Function: parse_data
    Purpose: to get the matrix of price and time
    Parameter:
        filename -- name of the csv file
    Returns the matrix of time and price, and a dictionary showing
        the mapping of place and index
    '''

    data = pd.read_csv(filename)
    
    time_matrix = data.values[TIME_ROW: TIME_ROW + SIZE, TIME_COL: TIME_COL + SIZE]
    for i in range(len(time_matrix)):
        for j in range(len(time_matrix[i])):
            if pd.isna(time_matrix[i][j]):
                time_matrix[i][j] = float('inf')
            else:
                time_matrix[i][j] = parse_time(time_matrix[i][j])
    
    price_matrix = data.values[PRICE_ROW: PRICE_ROW + SIZE, PRICE_COL: PRICE_COL + SIZE]
    for i in range(len(price_matrix)):
        for j in range(len(price_matrix[i])):
            if pd.isna(price_matrix[i][j]):
                price_matrix[i][j] = float('inf')
            else:
                price_matrix[i][j] = int(price_matrix[i][j])

    return time_matrix, price_matrix


def parse_time(time):
    '''
    Function: parse_time
    Purpose: to tranfer time string into number of minutes
    Parameter:
        time -- the string of the time, whose format is "xhym"
    Returns the number of minutes
    '''
    hour_and_min = time.split('h')
    hour = hour_and_min[0]
    minute = hour_and_min[1].strip('m')
    if minute == "":
        minute = 0
    return int(hour) * 60 + int(minute)
