# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

# Importing classes
from building import building    
from citizen  import citizen

# Importing functions/routines
from create_buildings import create_building
from create_buildings import create_building_and_assign_volk
from plotter import plotter
from create_citizens import create_citizens

nr_people = 300; # number of citizens
nr_homes =  100; # number of homes
city_size = 200; # the spatial dimension of the city

# create the population, assigning None to most of the attributions
volk = create_citizens(city_size, nr_people)

# create the buildings of the city and assign people to the houses
home =  create_building_and_assign_volk(city_size, volk, nr_homes, 'home')

sum = 0
for i in range(0, nr_homes):
#    print(home[i].peoples_id)
    sum+=home[i].number()
print(sum)
print(np.size(home))

#for i in range(0,nr_people):
#    print(volk[i].home+1)

plotter(home,'rs')
plotter(volk,'go')
plt.show()
