'''
Peinan Wang 
CS 5001 Spring 2022
Final Project

Neighbourhood.py
Class: Neighbourhood
'''


from DemographicData import DemographicData


SMALL_DIFFERENCE = 0.05
DECIMAL_PLACES = 2
HUNDRED_PERCENT = 100


class Neighbourhood:
    '''
    Class:     Neighbourhood
    Attribute: name - string;
               demodata_2016 - an instance of DemographicsData class
               demodata_2006 - an instance of DemographicsData class
    Method:    calculate_population_growth
               calculate_immigration_growth
               calculate_immigrant_density_growth
    '''
    def __init__(self, name, demographic_data_2016, demographic_data_2006):
        '''
        Method:  __init__
        Purpose: construct an instance of Neighbourhood class
        Param:   self
                 demodata_2016 - an instance of DemographicsData class
                 demodata_2006 - an instance of DemographicsData class
        Return:  none
        '''
        self.name = name
        self.demodata_2016 = demographic_data_2016
        self.demodata_2006 = demographic_data_2006


    def __str__(self):
        '''
        Method:  __str__
        Purpose: create a string representation of the Neighbourhood instance
        Param:   self
        Return:  a string
        ''' 
        total_population = self.demodata_2016.total_population
        return f"The population of {self.name} is {total_population} " +\
               "(2016 Census)."


    def __eq__(self, other):
        '''
        Method:  __eq__
        Purpose: compare two Neighbourhood instances by total populations 
                 in 2016
        Param:   self
                 other - another instance of Neighbourhood
        Return:  True if the population difference between two neighbourhoods 
                 is significantly small (<= 5%)
                 False otherwise
        '''

        if not isinstance(other,Neighbourhood):
            return False

        population_self = self.demodata_2016.total_population
        population_other = other.demodata_2016.total_population

        if  abs((population_self - population_other) / population_other)\
            <= SMALL_DIFFERENCE:
            return True
        else:
            return False


    def calculate_population_growth(self):
        '''
        Method:  calculate_population_growth
        Purpose: calculate the change of total population from 2006 to 2016 in 
                 percentage
        Param:   self
        Return:  an float, rounded to 2 decimal places
        '''
        population_2016 = self.demodata_2016.total_population
        population_2006 = self.demodata_2006.total_population
        
        growth = population_2016 - population_2006
        percentage = growth / population_2006 * HUNDRED_PERCENT

        return round(percentage, DECIMAL_PLACES)
        

    def calculate_immigration_growth(self):
        '''
        Method:  calculate_immigration_growth
        Purpose: calculate the change of immigrant population from 2006 to 
                 2016 in percentage
        Param:   self
        Return:  an float, rounded to 2 decimal places
        '''
        immi_population_2016 = self.demodata_2016.immi_population
        immi_population_2006 = self.demodata_2006.immi_population
        
        growth = immi_population_2016 - immi_population_2006 
        percentage = growth / immi_population_2006 * HUNDRED_PERCENT

        return round(percentage, DECIMAL_PLACES)
    

    def calculate_immigrant_density_growth(self):
        '''
        Method:  calculate_immigrant_density_growth
        Purpose: calculate the change of immigrant density from 2006 to 2016 
                 in percentage
        Param:   self
        Return:  an float, rounded to 2 decimal places
        '''
        immi_density_2016 = self.demodata_2016.calculate_immi_density()
        immi_density_2006 = self.demodata_2006.calculate_immi_density()
        
        growth = immi_density_2016 - immi_density_2006
        percentage = growth / immi_density_2006 * HUNDRED_PERCENT

        return round(percentage, DECIMAL_PLACES)
