import numpy as np
from citizen import citizen

def create_citizens(city):
    city_size = city.city_size
    nr_people = city.nr_people
    volk = np.empty(nr_people, dtype=object)
    for i in range(0, nr_people):
        posi = np.random.randint(city_size,size=2)
        next_dest = np.empty(2)
        health_status_i = 0; # 0: healthy, 1: infected, -1: immune
        volk[i] = citizen(posi, None, None, np.empty(0), next_dest, 0)
    return volk

def seed_the_disease(city, volk):
    percentage = city.percentage
    nr_people = np.size(volk)
    for i in range(0, nr_people):
        if (np.random.rand() < percentage):
            volk[i].health_status = 1
