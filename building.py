import numpy as np
class building:
    info = 'a place which has a coordinate and also a list of people associated with it'
    def __init__(self, pos, peoples_id, building_type):
        self.pos = pos
        self.peoples_id = peoples_id
        self.usage = building_type
    def number(self):
        return(np.size(self.peoples_id))        
    def distance(self, another_building):
        return abs(self.pos[0] - another_building.pos[0]) + abs(self.pos[1] - another_building.pos[1])
