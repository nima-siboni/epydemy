# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import time
import random
# Importing classes
from building import building    
from citizen  import citizen
from city import city
# Importing functions/routines
from create_citizens import create_citizens
from create_buildings import create_buildings
from municipality import assign_volk_to_buildings_and_vice_versa
from plotter import plot_info
from plotter import setup_plots
from create_citizens import seed_the_disease
from dynamics import one_full_step
from dynamics import one_partial_step
from dynamics import setting_new_destination
from dynamics import commute_to_next_destionation
from municipality import health_statistics

random.seed(0)
np.random.seed(0)
nr_people = 400	# number of citizens
nr_homes =  100 # number of homes
nr_workplaces =	10 # number of work_places
nr_socialplaces = 40 # number of social places 
city_size = 100 # the spatial dimension of the city
percentage = 0.01 # the approximate percentage of infected people at the beginning
contagiosity = 0.000001 # the probability that you get infected if you are close to an infected person for a timestep
immunity_step = 1./100/24/15 #increase of immunity per step for the infected; it is chosen such that it is smaller than 1/(number of steps per day), so the infected person does not heal over one day
alpha = 10 # let it be! :D
live_cam = False # True: shows every one at every time step, False: no over of the city
live_stat = False # True:updates the graph of information every timestep. If False, it only shows the change after each commute or shift
my_city = city(nr_people, nr_homes, nr_workplaces, nr_socialplaces, city_size, percentage, contagiosity, immunity_step, alpha, 0, live_cam, live_stat)
# a duplicate of the city where no ones is sick and the disease is not contagiose
healthy_city = city(nr_people, nr_homes, nr_workplaces, nr_socialplaces, city_size, 0, 0, immunity_step, alpha, 0, False, False)


# setup the figure
setup_plots(my_city)
plt.ion()
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

for i in range(0, 800): #sending everybody home without getting sick
    one_full_step(healthy_city, volk, 'night')

[healthy, not_infected, immune, sick] = health_statistics(my_city, volk, 'v')


shift = 0
while (sick > 0):
    #setting the new destination
    if (shift % 3 == 0):
        setting_new_destination(volk, work_place, home)
        shift_duration_in_steps = 800
        time = 'morning'
    if (shift % 3 == 1):
        setting_new_destination(volk, social_place, home)
        shift_duration_in_steps = 400
        time = 'evening'
    if (shift % 3 == 2):
        setting_new_destination(volk, home, home)
        shift_duration_in_steps = 1200
        time = 'night'
        
    plot_info(my_city, volk, my_city.info_graph)            
    commute_to_next_destionation(my_city, volk, home, work_place, social_place, time)

    [healthy, not_infected, immune, sick] = health_statistics(my_city, volk, 'v')
    plot_info(my_city, volk, my_city.info_graph)            

    for step in range(shift_duration_in_steps):
        one_partial_step(my_city, volk)
        
    
    shift = shift + 1
raw_input('press return to continue')
