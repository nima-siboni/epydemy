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
from dynamics import send_people_home
from municipality import health_statistics
from municipality import detailed_health_report
from municipality import create_city_from_a_cookbook
from municipality import city_statistics

inputfile = 'inputfile.dat' #only the first word is used in each line. the rest is just discarded

my_city = create_city_from_a_cookbook(inputfile)

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

[volk, home] = assign_volk_to_buildings_and_vice_versa(my_city, volk, home)
[volk, work_place] = assign_volk_to_buildings_and_vice_versa(my_city, volk, work_place)
[volk, social_place] = assign_volk_to_buildings_and_vice_versa(my_city, volk, social_place)

# give a report of population distributions
city_statistics(my_city, volk, home, work_place, social_place)

# setting the next_dest to home and move people there
setting_new_destination(volk, home, home)
send_people_home(my_city, volk, home)

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
        
    if (my_city.mute == False):
        plot_info(my_city, volk, my_city.info_graph)            
    commute_to_next_destionation(my_city, volk, home, work_place, social_place, time)

    [healthy, not_infected, immune, sick] = health_statistics(my_city, volk, 'v')
    if (my_city.mute == False):
        plot_info(my_city, volk, my_city.info_graph)            

    for step in range(shift_duration_in_steps):
        one_partial_step(my_city, volk)
        
    
    shift = shift + 1

detailed_health_report(my_city, volk, home, work_place, social_place)

raw_input('press return to continue')

