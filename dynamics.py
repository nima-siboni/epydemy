import numpy as np
from citizen  import citizen
# one_full_step consists of
# everybody who is alive would make one step
# it will be checked if people are in the same position at the updated positions, this is done by making
# each person who is infected leave a mark on the lattice position.
# Then later it will be checked if you are in a marked position. Depending on the strength of the mark, you get infected or not. 

# The inputs are
# volk: an array which consists of citizens,
# alpha: the tendency to go to the next destination (see description in class citizen)
# system_size: the spatial extension of the system
# contagiosity: the factor which determines how likely it is to get infected if you are in the same position with a sick person. This value is [0:1]

def one_full_step(volk, alpha, system_size, contagiosity):
    # useful constants
    nr_people = np.size(volk)

    # creating earth for peole to leave their traces
    earth = np.zeros((system_size, system_size))

    # loop over all people and move them one step and make them leave their traces on the earth
    for i in range(0, nr_people):
        if (volk[i].alive == 1):
            volk[i].one_step(alpha, system_size)
            earth[volk[i].pos[0], volk[i].pos[1]] += volk[i].health_status

    # now for every healthy person we check the trace of everybody else on the location of that person
    for i in range(0, nr_people):
        if (volk[i].health_status == 0):
            dirtiesness = earth[volk[i].pos[0], volk[i].pos[1]]
            probability = dirtiesness * contagiosity
            if (np.random.rand() < probability):
                volk[i].health_status = 1
    
