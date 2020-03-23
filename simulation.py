# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive

import time
# Importing classes
from building import building    
from citizen  import citizen

# Importing functions/routines
from create_buildings import create_building
from create_buildings import create_building_and_assign_volk
from plotter import plotter
from create_citizens import create_citizens
from create_citizens import seed_the_disease
from dynamics import one_full_step

nr_people = 150	# number of citizens
nr_homes = 50 # number of homes
nr_workplaces =	15 # number of workplaces
city_size = 200 # the spatial dimension of the city
percentage = 0.05 # the approximate percentage of infected people at the beginning
contagiosity = 0.001 # the probability that you get infected if you are close to an infected person for a timestep
immunity_step = 1./600 #increase of immunity per step for the infected; it is chosen such that it is smaller than 1/(number of steps per day), so the infected person does not heal over one day

# create the population, assigning None to most of the attributions
volk = create_citizens(city_size, nr_people)
seed_the_disease(volk, percentage)
# create the houses of the city and assign people to them
home = create_building_and_assign_volk(city_size, volk, nr_homes, 'home')
# create the workplaces of the city and assign people to them
workplace = create_building_and_assign_volk(city_size, volk, nr_workplaces, 'work')

sum = 0
for i in range(0, nr_homes):
#    print(home[i].peoples_id)
    sum+=home[i].number()
print(sum)
print(np.size(home))

sum = 0
for i in range(0, nr_workplaces):
#    print(home[i].peoples_id)
    sum+=workplace[i].number()
print(sum)

# setting the next_dest to home
for i in range(0,nr_people):
    volk[i].next_dest = home[volk[i].home].pos


#plotter(workplace,'bs')
plotter(home,'rs')
plotter(volk,'go')


for i in range(0,100):
    one_full_step(volk, 2, city_size, 0, 0)
    
for shift in range(0,100):
	# setting the next_dest to destination for this shift
    for i in range(0,nr_people):
        if np.remainder(shift,2)==0:
            volk[i].next_dest = home[volk[i].home].pos
        if np.remainder(shift,2)==1:
            volk[i].next_dest = workplace[volk[i].work].pos
    print('next dest assigned')        
    for step in range(0,200):
        plt.clf()    
        one_full_step(volk, 2, city_size, contagiosity, immunity_step)
        plotter(home, 'r^')
        plotter(workplace, 'bs')
        plotter(volk, 'go')
        plt.pause(0.01)

raw_input('press return to continue')
