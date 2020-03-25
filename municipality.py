import numpy as np
import random as random
# this function get a list of input
# volk: the list of people
# building: the list building
# and assign people to buildings randomly. It also fill in the attribute "peoples_id" for each building with the people in it.
# the function returns both volk and buildings as outputs

def assign_volk_to_buildings_and_vice_versa(volk, building):

    # first lets see if the building is of a exclusive type or not:
    # a building is exclusive if each person can be associated with only one of those buildings
    # e.g. here home/work is exclusive as you have "one and only one" home/work
    # but social places you can have as many as you like or might not have any
    usage = building[0].usage
    if (usage == 'home' or usage == 'work'):
        exclusive = True
    else:
        exclusive = False
    
    nr_people = np.size(volk)
    nr_building = np.size(building)
    
    # first we go for a the case of exclusive buildings
    # a list with size of people is created first, then it is shuffled and sliced at random positions (with nr_building) slices.
    # then all people in the ith slices is assinged to building i.
    # also the id of the ith building (which is simply i) is assigned to each person in that slice.
    # in this way by construct all the people are assigned to the buildings, and all the buildings have at least one person

    if (exclusive == True):

        all_people_list = np.arange(nr_people)
        np.random.shuffle(all_people_list);

        cutpoint = random.sample(range(nr_people), nr_building + 1) # the random points at which the above list of people is cut...
        # ... from cutpoint[i] to cutpoint[i+1] is assigned to building i.
        # ... the cutpoint list should start by cutpoint[0]=0 and cutpoint[nr_building]= nr_people   
        cutpoint.sort()
        cutpoint[0] = 0
        cutpoint[nr_building]= nr_people

        for bid in range(nr_building):
            # assiging some people to building number bid
            building[bid].peoples_id = np.asarray( all_people_list[ cutpoint[bid] : cutpoint[bid+1] ]) 
            # assigning the building id (bid) to the same people
            for i in range(cutpoint[bid], cutpoint[bid+1]):
                pid = all_people_list[i]
                # this part should be modified if usages of buildings are modified
                if (usage == 'home'):
                    volk[pid].home = bid
                if (usage == 'work'):
                    volk[pid].work = bid
                    
    if (exclusive == False):
        for bid in range(nr_building):
            all_people_list = np.arange(nr_people)
            np.random.shuffle(all_people_list);
            nr_people_in_this_place = np.random.randint(1, nr_people + 1)
            people_in_this_place = all_people_list[0 : nr_people_in_this_place]
            # assiging some people to building number bid
            building[bid].peoples_id = people_in_this_place
            # assigning the building id (bid) to the same people
            for i in range(nr_people_in_this_place):
                pid = people_in_this_place[i]
                # this part should be modified if usages of buildings are modified
                if (usage == 'social_place'):
                    volk[pid].social_places = np.append(volk[pid].social_places, int(bid))
                
    return volk, building

def health_statistics(volk, verbose):
    nr_people = np.size(volk)
    sick = 0
    immune = 0
    not_infected = 0
    recovered_or_immune = 0 #if there is no vaccination the only immune people are the recovered people!
    for i in range(nr_people):
        if (volk[i].health_status == 0 and volk[i].immunity == 1):
            recovered_or_immune += 1
        if (volk[i].health_status == 0 and volk[i].immunity == 0):
            not_infected += 1
        if (volk[i].health_status == 1 ):
            sick += 1
        immune += volk[i].immunity
    healthy = recovered_or_immune + not_infected
    if (verbose == 'v'):
        print('nr healthy: '+ str(healthy) + '  (not_infected: '+ str(not_infected) + ', immune: ' + str(recovered_or_immune) + '),    nr sick: ' + str(sick)) 
    return healthy, not_infected, recovered_or_immune, sick
