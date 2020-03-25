# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import time

# Importing classes
from building import building    
from citizen  import citizen

# Importing functions/routines
from create_citizens import create_citizens
from create_buildings import create_buildings
from municipality import assign_volk_to_buildings_and_vice_versa
from plotter import plotter
from create_citizens import seed_the_disease
from dynamics import one_full_step
from dynamics import one_partial_step
from dynamics import setting_new_destination
from dynamics import commute_to_next_destionation

nr_people = 150	# number of citizens
nr_homes = 50 # number of homes
nr_workplaces =	15 # number of work_places
nr_socialplaces = 10 # number of social places 
city_size = 200 # the spatial dimension of the city
percentage = 0.05 # the approximate percentage of infected people at the beginning
contagiosity = 0.001 # the probability that you get infected if you are close to an infected person for a timestep
immunity_step = 1./600 #increase of immunity per step for the infected; it is chosen such that it is smaller than 1/(number of steps per day), so the infected person does not heal over one day
alpha = 2 # let it be! :D

# create the population, assigning None to most of the attributions
volk = create_citizens(city_size, nr_people)
seed_the_disease(volk, percentage)

# create the houses of the city 
home = create_buildings(city_size, nr_homes, 'home')

# create the work_places of the city 
work_place = create_buildings(city_size, nr_workplaces, 'work')

# create the socialplaces of the city and assign people to them
social_place = create_buildings(city_size, nr_socialplaces, 'social_place')

[volk, home] = assign_volk_to_buildings_and_vice_versa(volk, home)
[volk, work_place] = assign_volk_to_buildings_and_vice_versa(volk, work_place)
[volk, social_place] = assign_volk_to_buildings_and_vice_versa(volk, social_place)

sum = 0
for i in range(0, nr_homes):
#    print(home[i].peoples_id)
    sum+=home[i].number()
print(sum)
print(np.size(home))

sum = 0
for i in range(0, nr_workplaces):
#    print(home[i].peoples_id)
    sum+=work_place[i].number()
print(sum)

# setting the next_dest to home
for i in range(0,nr_people):
    volk[i].next_dest = home[volk[i].home].pos


#plotter(work_place,'bs')
plotter(home,'rs')
plotter(volk,'go')


for i in range(0, 100):
    one_full_step(volk, 2, city_size, 0, 0)
    
for shift in range(0, 100):
    #setting the new destination
    if (shift % 3 == 0):
        setting_new_destination(volk, work_place, home)
        shift_duration_in_steps = 50
    if (shift % 3 == 1):
        setting_new_destination(volk, social_place, home)
        shift_duration_in_steps = 50
    if (shift % 3 == 2):
        setting_new_destination(volk, home, home)
        shift_duration_in_steps = 50
        
    commute_to_next_destionation(volk, alpha, city_size, contagiosity, immunity_step, home, work_place, social_place)

    for step in range(shift_duration_in_steps):
        one_partial_step(volk, alpha, city_size, contagiosity, immunity_step)
        
raw_input('press return to continue')
