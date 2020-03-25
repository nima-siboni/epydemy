import numpy as np
from building import building

# this function return a list of buildings (with size nr_building), in a city of size (city_size), 
# and assign nr_people people to these buildings, and return the list of buildings
def create_buildings(city_size, nr_building, buildingtype):
    upper_limit_reached = False
    total_nr_assigned = 0
    result = np.empty(nr_building, dtype=object)
    # First add one person per house
    for i in range(0, nr_building):
        posi = np.random.randint(city_size,size=2)
        result[i] = building(posi, None, buildingtype)
    return result
