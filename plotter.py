import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
interactive(True)
def plotter(sth,smhow):
    m = np.size(sth)
    data = np.zeros((m,2))
    for i in range(0,m):
        data[i,:] = sth[i].pos
    plt.plot(data[:,0],data[:,1],smhow)


