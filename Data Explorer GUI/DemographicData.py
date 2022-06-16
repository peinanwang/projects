'''
Peinan Wang 
CS 5001 Spring 2022
Final Project - Milestone 1

DemographicData.py
Class: DemographicData
'''


DECIMAL_PLACES = 2
HUNDRED_PERCENT = 100


class DemographicData:
    '''
    Class:     DemographicData
    Attribute: neighbourhood_name - string;
               year - the census year; a non-negative integer
               total_population - a non-negative integer
               immi_population - a non-negative integer
    Method:    calculate_immi_density
    '''
    def __init__(self, 
                 neighbourhood_name, 
                 year, 
                 total_population,
                 immi_population):
        '''
        Method:  __init__
        Purpose: construct an instance of DemographicData class
        Param:   self
                 neighbourhood_name - string
                 year - an integer
                 total_population - an integer
                 immi_population - an integer
        Return:  none
                 raise ValueError if year
        '''
        
        self.neighbourhood_name = neighbourhood_name
        self.year = year
        self.total_population = total_population
        self.immi_population = immi_population


    def __str__(self):
        '''
        Method:  __str__
        Purpose: create a string representation of the DemographicData instance
        Param:   self
        Return:  a string
        ''' 
        return f"The {self.year} demographic data of {self.neighbourhood_name}"


    def __eq__(self, other):
        '''
        Method:  __eq__
        Purpose: compare two DemographicData instances by the neighbourhood 
                 name
        Param:   self
                 other - another instance of DemographicData 
        Return:  True if the two DemographicData instances have the same 
                 neighbourhood name 
                 False otherwise
        '''
        if not isinstance(other, DemographicData):
            return False

        return self.neighbourhood_name == other.neighbourhood_name


    def calculate_immi_density(self):
        '''
        Method:  calculate_immi_density
        Purpose: calculate the immigrant density of the neighbourhood
        Param:   self
        Return:  an float, rounded to 2 decimal places
        '''
        immi_density = (self.immi_population / self.total_population
                       * HUNDRED_PERCENT)

        return round(immi_density, DECIMAL_PLACES)
