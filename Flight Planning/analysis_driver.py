'''
This is the driver file for CS 5002 Final Project.
'''

from dijkstra_algorithm import Graph
from get_data_from_file import parse_data


CITY_DICT = {0 : "Shanghai", 1 : "Beijing", 2 : "Guangzhou",  3 : "Hong Kong", 
             4 : "Wuhan", 5 : "Seoul", 6 : "Tokyo", 7 : "San Francisco", 
             8 : "Vancouver", 9 : "Toronto", 10 : "Calgary"}


def find_flight_path(city_vertex):
    '''
    Function:  find_flight_path
    Purpose:   find the shortest path and the cheapest path to fly from a city
    Parameter: city_vertex, an integer from 0 to 10.
    Return:    none
    '''
    city = CITY_DICT[city_vertex]
    
    time_matrix, price_matrix = parse_data("flight_info.csv")
    
    print(f"\n\nFlights leaving {city} with the shortest flight duration:\n")
    Graph(time_matrix).dijkstra(city_vertex)

    print(f"\nFlights leaving {city} with the lowest price:\n")
    Graph(price_matrix).dijkstra(city_vertex)


def main():
    for i in range(len(CITY_DICT)):
        find_flight_path(i)


if __name__ == "__main__":
    main()
