# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import time

# Importing classes
from building import building    
from citizen  import citizen
from city import city
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
from municipality import health_statistics

nr_people = 150	# number of citizens
nr_homes = 50 # number of homes
nr_workplaces =	15 # number of work_places
nr_socialplaces = 10 # number of social places 
city_size = 200 # the spatial dimension of the city
percentage = 0.01 # the approximate percentage of infected people at the beginning
contagiosity = 0.01 # the probability that you get infected if you are close to an infected person for a timestep
immunity_step = 1./600 #increase of immunity per step for the infected; it is chosen such that it is smaller than 1/(number of steps per day), so the infected person does not heal over one day
alpha = 10 # let it be! :D
plotting = True
my_city = city(nr_people, nr_homes, nr_workplaces, nr_socialplaces, city_size, percentage, contagiosity, immunity_step, alpha, 0)
# a duplicate of the city where no ones is sick and the disease is not contagiose
healthy_city = city(nr_people, nr_homes, nr_workplaces, nr_socialplaces, city_size, 0, 0, immunity_step, alpha, 0)

# create the population, assigning None to most of the attributions
volk = create_citizens(my_city)
seed_the_disease(my_city, volk)

# create the houses of the city 
home = create_buildings(my_city, 'home')

# create the work_places of the city 
work_place = create_buildings(my_city, 'work')

# create the socialplaces of the city and assign people to them
social_place = create_buildings(my_city, 'social_place')

[volk, home] = assign_volk_to_buildings_and_vice_versa(volk, home)
[volk, work_place] = assign_volk_to_buildings_and_vice_versa(volk, work_place)
[volk, social_place] = assign_volk_to_buildings_and_vice_versa(volk, social_place)


# setting the next_dest to home
setting_new_destination(volk, home, home)

for i in range(0, 200): #sending everybody home without getting sick
    one_full_step(healthy_city, volk, 'night')
    
for shift in range(0, 100):
    #setting the new destination
    if (shift % 3 == 0):
        setting_new_destination(volk, work_place, home)
        shift_duration_in_steps = 200
        time = 'morning'
    if (shift % 3 == 1):
        setting_new_destination(volk, social_place, home)
        shift_duration_in_steps = 200
        time = 'evening'
    if (shift % 3 == 2):
        setting_new_destination(volk, home, home)
        shift_duration_in_steps = 200
        time = 'night'
        
    [healthy, not_infected, immune, sick] = health_statistics(volk, 'v')

    commute_to_next_destionation(my_city, volk, home, work_place, social_place, time, plotting)

    [healthy, not_infected, immune, sick] = health_statistics(volk, 'v')

    for step in range(shift_duration_in_steps):
        one_partial_step(my_city, volk)

raw_input('press return to continue')
