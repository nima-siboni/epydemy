import numpy as np
from building import building

# this function return a list of buildings (with size nr_building, obtained from city), in a city of size (city_size, obtained from city), 
# and assign nr_people (obtained from city) people to these buildings, and return the list of buildings
def create_buildings(city, buildingtype):
    city_size = city.city_size
    if (buildingtype == 'home'):
        nr_building = city.nr_homes
    if (buildingtype == 'work'):
        nr_building = city.nr_workplaces
    if (buildingtype == 'social_place'):
        nr_building = city.nr_socialplaces
        
    result = np.empty(nr_building, dtype=object)
    # First add one person per house
    for i in range(0, nr_building):
        posi = np.random.randint(city_size,size=2)
        result[i] = building(posi, None, buildingtype)
    return result
