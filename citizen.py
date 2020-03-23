import numpy as np
class citizen:

    # Class Attribute
    info = 'human'

    # Initializer / Instance Attributes
    def __init__(self, pos, home, work, social_places, next_dest, health_status):
        self.pos = pos
        self.home = home
        self.work = work
        self.social_places = social_places
        self.maxsocial_places = 5
        self.minsocial_places = 0
        self.next_dest = next_dest
        self.alive = 1 # 0: dead, 1: alive. The default value is 1 (i.e. we dont need to create dead people)
        self.immunity = 0 # [0,1): not immue, 1: immue # The default value is 0 as no one is born immune; no vaccine either
        self.health_status = health_status # 0: healthy, 1: infected
        
    # one_step takes a random walk with preference toward the next step
    # alpha determines how likely it is to go the next_dest:
    # alpha = 1 leads to no preference
    # alpha > 1 leads to approaching the next_dest
    # alpha < 1 leads to further distancing from the next_dest
    def one_step(self, alpha, system_size):
        r = np.random.rand()
        if (r > 1/(1+alpha)): # approching the next_dest
            self.pos[0] = self.pos[0] + np.sign(self.next_dest[0] - self.pos[0])
            self.pos[1] = self.pos[1] + np.sign(self.next_dest[1] - self.pos[1])
        else: # going away from it
            self.pos[0] = self.pos[0] - np.sign(self.next_dest[0] - self.pos[0])
            self.pos[1] = self.pos[1] - np.sign(self.next_dest[1] - self.pos[1])

        # applying a reflecting boundary condition
        # it is assumed that the earth is a flat square
        if (self.pos[0] < 0):
            self.pos[0] = 0
        if (self.pos[0] >= system_size):
            self.pos[0] = system_size - 1;
        if (self.pos[1] < 0):
            self.pos[1] = 0
        if (self.pos[1] >= system_size):
            self.pos[1] = system_size - 1;
            
            
