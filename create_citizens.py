import numpy as np
from citizen import citizen

def create_citizens(city_size, nr_people):
    volk = np.empty(nr_people, dtype=object)
    for i in range(0, nr_people):
        posi = np.random.randint(city_size,size=2)
        volk[i] = citizen(posi, None, None, None, None)
    return volk
