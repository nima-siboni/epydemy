import numpy as np
from building import building

# this function return a list of buildings (with size nr_building), in a city of size (city_size), and assign nr_people people to these buildings, and return the list of buildings
def create_building(city_size, nr_people, nr_building):
    upper_limit_reached = False
    total_nr_assigned = 0
    building = np.empty(nr_building, dtype=object)
    # First add one person per house
    for i in range(0, nr_building):
        a = np.array([i])
        posi = np.random.randint(city_size,size=2)
        building[i] = building(posi, a)
        total_nr_assigned = total_nr_assigned + 1
        
    for i in range(0, nr_building):
        nr_new_people_in_this_house = np.random.randint(1, high = int(nr_people / nr_building))
        if (total_nr_assigned + nr_new_people_in_this_house <= nr_people ):
            upper_limit = total_nr_assigned + nr_new_people_in_this_house
        else:
            upper_limit = nr_people
                    
        if (upper_limit_reached == False):
            new_habitants = np.arange(total_nr_assigned, upper_limit)
            building[i].peoples_id = np.concatenate((building[i].peoples_id, new_habitants))

        total_nr_assigned = upper_limit
        
        if (total_nr_assigned == nr_people):
            upper_limit_reached = True
            
    return building


# this function return a list of buildings (with size nr_building), in a city of size (city_size), and assign a list of people (volk) to these buildings, and return the list of buildings. It also assing the building id to individuals in the volk (to building_name)
def create_building_and_assign_volk(city_size, volk, nr_building, building_name):
    nr_people = np.size(volk)
    upper_limit_reached = False
    total_nr_assigned = 0
    buildings = np.empty(nr_building, dtype=object)
    # First add one person per house
    for i in range(0, nr_building):
        a = np.array([i])
        posi = np.random.randint(city_size,size=2)
        buildings[i] = building(posi, a)
        total_nr_assigned = total_nr_assigned + 1
        if (building_name=='home'):
            volk[i].home = i
        if (building_name=='work'):
            volk[i].work = i
            
    while (total_nr_assigned < nr_people):    
        for i in range(0, nr_building):
            nr_new_people_in_this_house = np.random.randint(1, high =  2*int(nr_people / nr_building)+1)
            if (total_nr_assigned + nr_new_people_in_this_house <= nr_people ):
                upper_limit = total_nr_assigned + nr_new_people_in_this_house
            else:
                upper_limit = nr_people
                    
            if (upper_limit_reached == False):
                new_habitants = np.arange(total_nr_assigned, upper_limit)
                buildings[i].peoples_id = np.concatenate((buildings[i].peoples_id, new_habitants))
                for pid in range(total_nr_assigned, upper_limit):
                    if (building_name=='home'):
                        volk[pid].home = i
                    if (building_name=='work'):
                        volk[pid].work = i
                
            total_nr_assigned = upper_limit
        
            if (total_nr_assigned == nr_people):
                upper_limit_reached = True
        
    return buildings
