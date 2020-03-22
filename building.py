import numpy as np
class building:
    info = 'a place which has a coordinate and also a list of people associated with it'
    def __init__(self, pos, peoples_id):
        self.pos = pos
        self.peoples_id = peoples_id
    def number(self):
        return(np.size(self.peoples_id))        
