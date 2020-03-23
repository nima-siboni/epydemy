import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
interactive(True)
def plotter(sth,smhow):
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
        plt.scatter(data[:,0], data[:,1], c=health_state_data)
    else:
        plt.plot(data[:,0], data[:,1], smhow)

