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
from plotter import plot_info
from plotter import setup_plots
from create_citizens import seed_the_disease
from dynamics import one_full_step
from dynamics import one_partial_step
from dynamics import setting_new_destination
from dynamics import commute_to_next_destionation
from municipality import health_statistics

class simulation:
    # Class Attribute
    info = 'simulation'

    # Initializer / Instance Attributes
    def __init__(self,nr_people,nr_homes,nr_workplaces,nr_socialplaces,city_size,percentage,contagiosity,immunity_step):
        self.nr_people = nr_people	# number of citizens
        self.nr_homes =  nr_homes # number of homes
        self.nr_workplaces =	nr_workplaces # number of work_places
        self.nr_socialplaces = nr_socialplaces # number of social places 
        self.city_size = city_size # the spatial dimension of the city
        self.percentage = percentage # the approximate percentage of infected people at the beginning
        self.contagiosity = contagiosity # the probability that you get infected if you are close to an infected person for a timestep
        self.immunity_step = immunity_step #increase of immunity per step for the infected; it is chosen such that it is smaller than 1/(number of steps per day), so the infected person does not heal over one day
        self.alpha = 10 # let it be! :D
        self.live_cam = True # True: shows every one at every time step, False: no over of the city
        self.live_stat = False #updates the graph of information every timestep. If False, it only shows the change after each commute or shift
        self.my_city = city(self.nr_people, self.nr_homes, self.nr_workplaces, self.nr_socialplaces, self.city_size, self.percentage, self.contagiosity, self.immunity_step, self.alpha, 0, self.live_cam, self.live_stat)
        # a duplicate of the city where no ones is sick and the disease is not contagiose
        self.healthy_city = city(self.nr_people, self.nr_homes, self.nr_workplaces, self.nr_socialplaces, self.city_size, 0, 0, self.immunity_step, self.alpha, 0, False, False)

        # create the population, assigning None to most of the attributions
        self.volk = create_citizens(self.my_city)
        seed_the_disease(self.my_city, self.volk)

        # create the houses of the city 
        self.home = create_buildings(self.my_city, 'home')

        # create the work_places of the city 
        self.work_place = create_buildings(self.my_city, 'work')

        # create the socialplaces of the city and assign people to them
        self.social_place = create_buildings(self.my_city, 'social_place')

        [self.volk, self.home] = assign_volk_to_buildings_and_vice_versa(self.volk, self.home)
        [self.volk, self.work_place] = assign_volk_to_buildings_and_vice_versa(self.volk, self.work_place)
        [self.volk, self.social_place] = assign_volk_to_buildings_and_vice_versa(self.volk, self.social_place)

    def Run(self):
        # setup the figure
        setup_plots(self.my_city)
        plt.ion()
        # setting the next_dest to home
        setting_new_destination(self.volk, self.home, self.home)
        for i in range(0, 800): #sending everybody home without getting sick
            one_full_step(self.healthy_city, self.volk, 'night')

        [healthy, not_infected, immune, sick] = health_statistics(self.my_city, self.volk, 'v')

        shift = 0
        while (sick>0 and shift<100):
            #setting the new destination
            if (shift % 3 == 0):
                setting_new_destination(self.volk, self.work_place, self.home)
                shift_duration_in_steps = 100
                time = 'morning'
            if (shift % 3 == 1):
                setting_new_destination(self.volk, self.social_place, self.home)
                shift_duration_in_steps = 100
                time = 'evening'
            if (shift % 3 == 2):
                setting_new_destination(self.volk, self.home, self.home)
                shift_duration_in_steps = 100
                time = 'night'
                
            plot_info(self.my_city, self.volk, self.my_city.info_graph)            
            commute_to_next_destionation(self.my_city, self.volk, self.home, self.work_place, self.social_place, time)

            [healthy, not_infected, immune, sick] = health_statistics(self.my_city, self.volk, 'v')
            plot_info(self.my_city, self.volk, self.my_city.info_graph)            

            for step in range(shift_duration_in_steps):
                one_partial_step(self.my_city, self.volk)
                
            
            shift = shift + 1
        raw_input('press return to continue')
