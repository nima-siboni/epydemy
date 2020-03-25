import numpy as np
from citizen  import citizen
import matplotlib.pyplot as plt
from matplotlib import interactive
import time
from plotter import plotter
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
# immunity_step: increase of the immunity for a sick person after each timestep

def one_full_step(volk, alpha, system_size, contagiosity, immunity_step):
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
        if (volk[i].health_status == 0 and volk[i].immunity != 1):
            dirtiesness = earth[volk[i].pos[0], volk[i].pos[1]]
            probability = dirtiesness * contagiosity
            if (np.random.rand() < probability):
                volk[i].health_status = 1
    # increase the immunity of sick people towards 1, by steps of immunity_steps
    for i in range(0, nr_people):
        if (volk[i].health_status == 1 and volk[i].immunity < 1):
            volk[i].immunity += immunity_step
        if (volk[i].immunity >= 1): #recoverd
            volk[i].immunity = 1
            volk[i].health_status = 0


# one_partial_step is similar to one_full_step expect that particles dont move
# a partial step consists of
# it will be checked if people are in the same position at the updated positions, this is done by making
# each person who is infected leave a mark on the lattice position.
# Then later it will be checked if you are in a marked position. Depending on the strength of the mark, you get infected or not. 

# The inputs are
# volk: an array which consists of citizens,
# alpha: the tendency to go to the next destination (see description in class citizen)
# system_size: the spatial extension of the system
# contagiosity: the factor which determines how likely it is to get infected if you are in the same position with a sick person. This value is [0:1]
# immunity_step: increase of the immunity for a sick person after each timestep

def one_partial_step(volk, alpha, system_size, contagiosity, immunity_step):
    # useful constants
    nr_people = np.size(volk)

    # creating earth for peole to leave their traces
    earth = np.zeros((system_size, system_size))

    # loop over all people and  make them leave their traces on the earth
    for i in range(0, nr_people):
        if (volk[i].alive == 1):
            earth[volk[i].pos[0], volk[i].pos[1]] += volk[i].health_status

    # now for every healthy person we check the trace of everybody else on the location of that person
    for i in range(0, nr_people):
        if (volk[i].health_status == 0 and volk[i].immunity != 1):
            dirtiesness = earth[volk[i].pos[0], volk[i].pos[1]]
            probability = dirtiesness * contagiosity
            if (np.random.rand() < probability):
                volk[i].health_status = 1
                
    # increase the immunity of sick people towards 1, by steps of immunity_steps
    for i in range(0, nr_people):
        if (volk[i].health_status == 1 and volk[i].immunity < 1):
            volk[i].immunity += immunity_step
        if (volk[i].immunity >= 1): #recoverd
            volk[i].immunity = 1
            volk[i].health_status = 0

# setting the destination of the volk to their "building". If "building" doesnt exist (for example for someone who is not social)
# then the destination is set to plan_b_building. This should be a place such that everybody has one (for example home or work which are exclusive)
def setting_new_destination(volk, building, plan_b_building):
    nr_people = np.size(volk)
    building_type = building[0].usage
    #if (building_type == 'home' or building_type == 'work'):
    #    exclusive = True
    #else:
    #    exclusive = False
    if (building_type == 'home'):
        msg = 'home shift started'
    elif (building_type == 'work'):
        msg = 'work shift started'
    elif (building_type == 'social_place'):
        msg = 'time to socialize'
    else:
        msg = 'sth went wrong'
    print(msg)
    
    for i in range(0,nr_people):


        if (building_type == 'work'):
            volk[i].next_dest = building[volk[i].work].pos

        if (building_type == 'home'):
            volk[i].next_dest = building[volk[i].home].pos

        if (building_type == 'social_place'):
            if np.size(volk[i].social_places)>0:
		desiredsocialplace  = np.random.randint(np.size(volk[i].social_places))
		volk[i].next_dest = socialplace[volk[i].social_places[desiredsocialplace]].pos
	    else:
		volk[i].next_dest = plan_b_building[volk[i].home].pos
		


def commute_to_next_destionation(volk, alpha, city_size, contagiosity, immunity_step, home, work_place, social_place):

    print('... commute started')

    nr_arrived = 0
    nr_people = np.size(volk)

    while (nr_arrived < nr_people):

        nr_arrived = 0

        one_full_step(volk, alpha, city_size, contagiosity, immunity_step)
        # checking if everybody has arrived
        for i in range(nr_people):
            if np.array_equal(volk[i].pos, volk[i].next_dest):
                nr_arrived += 1
        # plotting
        plt.clf()    
        plotter(home, 'r^')
        plotter(work_place, 'bs')
        plotter(volk, 'go')
        plotter(social_place, 'r+')
        plt.pause(0.0005)

    print('... everyone arrived')
