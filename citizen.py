import numpy as np
class citizen:

    # Class Attribute
    info = 'human'

    # Initializer / Instance Attributes
    def __init__(self, pos, home, work, social_places, next_dest):
        self.pos = pos
        self.home = home
        self.work = work
        self.social_places = social_places
        self.next_dest = next_dest
        
    # one_step takes a random walk with preference toward the next step
    # alpha determines how likely it is to go the next_dest:
    # alpha = 1 leads to no preference
    # alpha > 1 leads to approaching the next_dest
    # alpha < 1 leads to further distancing from the next_dest
    def one_step(self, alpha):
        r = np.random.rand()
        if (r > 1/(1+alpha)): # approching the next_dest
            self.pos[0] = self.pos[0] + np.sign(self.next_dest[0] - self.pos[0])
            self.pos[1] = self.pos[1] + np.sign(self.next_dest[1] - self.pos[1])
        else: # going away from it
            self.pos[0] = self.pos[0] - np.sign(self.next_dest[0] - self.pos[0])
            self.pos[1] = self.pos[1] - np.sign(self.next_dest[1] - self.pos[1])
                        
