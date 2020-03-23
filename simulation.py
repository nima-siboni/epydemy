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

nr_people = 1200; # number of citizens
nr_homes = 400; # number of homes
nr_workplaces = 40 # number of workplaces
city_size = 400; # the spatial dimension of the city

# create the population, assigning None to most of the attributions
volk = create_citizens(city_size, nr_people)

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
print(np.size(home))

for i in range(0,nr_people):
    print(volk[i].home)
    print("workplace "+str(volk[i].work))
plotter(workplace,'bs')
plotter(home,'rs')
plotter(volk,'go')
plt.show()
