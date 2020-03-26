import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
from city import city
from municipality import health_statistics
interactive(True)

def setup_plots(city):
    if (city.live_cam == True):
        city.fig = plt.figure(figsize=(6,6))
        tmp = city.fig
        grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
        city.birdseyeview = tmp.add_subplot(grid[0:3, :])
        city.birdseyeview.set_xlim([0,city.city_size])
        city.birdseyeview.set_ylim([0,city.city_size])
        city.info_graph =  tmp.add_subplot(grid[3:4, :])
        city.birdseyeview.set_xlim([0,city.city_size])
        city.info_graph.set_ylim([0, city.nr_people])

    if (city.live_cam == False):
        city.fig = plt.figure(figsize=(6,6))
        tmp = city.fig
        grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
        city.info_graph =  tmp.add_subplot(grid[:, :])
        city.info_graph.set_ylim([0, city.nr_people])
        
def plot_birdseyeview(sth, smhow, smwhere):
    
    plt.ion()
    m = np.size(sth)
    data = np.zeros((m,2))
    if (sth[0].info == 'human'):
        human = True
        health_state_data = [None] * m
    else:
        human = False
        
    for i in range(0,m):
        data[i,:] = sth[i].pos
        if (human == True):
            health_state_data[i] = 'black' # default
            if (sth[i].health_status == 1):
                health_state_data[i] = 'orange'
            if (sth[i].immunity == 1):
                health_state_data[i] = 'gray'
    if (human == True):
        smwhere.scatter(data[:,0], data[:,1], c=health_state_data)
    else:
        smwhere.plot(data[:,0], data[:,1], smhow)

def plot_info(city, volk, smwhere):
    plt.ion()
    [healthy, not_infected, immune, sick] = health_statistics(city, volk, 'm')
    if (city.live_stat == True):
        xmin = max([city.timestep-40, 0])
    else:
        xmin = max([0, city.timestep/4-40])
        
    xmax = city.timestep + 10
    smwhere.set_xlim([xmin, xmax])
    smwhere.scatter([city.timestep], [not_infected], c='black')
    smwhere.scatter([city.timestep], [sick], c='orange')
    smwhere.scatter([city.timestep], [immune], c='gray')
    plt.pause(0.001)
def clear_birdseyeview(city):
    plt.ion()
    city.birdseyeview.clear()
#    tmp = city.fig
#    grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
#    city.birdseyeview = tmp.add_subplot(grid[:-1, 1:])
#    city.info_graph =  tmp.add_subplot(grid[:-1, 0])
#    city.fig.clf()
#    city.birdseyeview = city.fig.add_subplot(1, 1, 1)

#def clear_birdseyeview(city):
#    city.fig.clf()
#    city.birdseyeview = city.fig.add_subplot(1, 1, 1)
