import numpy as np
import random as random
from city import city
# this function get a list of input
# volk: the list of people
# building: the list building
# and assign people to buildings randomly. It also fill in the attribute "peoples_id" for each building with the people in it.
# the function returns both volk and buildings as outputs

def assign_volk_to_buildings_and_vice_versa(city, volk, building):

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
        for pid in range(nr_people):
            all_buildings_list = np.arange(nr_building)
            np.random.shuffle(all_buildings_list);
            nr_buildings_for_this_person = np.random.randint(0, city.max_individual_sociality + 1)
            buildings_for_this_person = all_buildings_list[0 : nr_buildings_for_this_person]
            # assiging some people to building number bid
            volk[pid].social_places = buildings_for_this_person
            # assigning the building id (bid) to the same people
            for i in range(nr_buildings_for_this_person):
                bid = buildings_for_this_person[i]
                # this part should be modified if usages of buildings are modified
                if (usage == 'social_place'):
                    building[bid].peoples_id = np.append(building[bid].peoples_id, int(pid))
                
    return volk, building

def health_statistics(city, volk, verbose):
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
        city.reportfile.write(str(city.timestep)+ ' ' + str(healthy) + ' ' + str(not_infected) + '  ' + str(recovered_or_immune) + '  ' + str(sick)+'\n')
        city.reportfile.flush()
    return healthy, not_infected, recovered_or_immune, sick


def detailed_health_report(city, volk, home, work, social_place):

    nr_people = np.size(volk)

    for i in range(nr_people):
        home_id = volk[i].home
        my_home = home[home_id]
        nr_people_in_home = my_home.number()
        list_of_social_places = volk[i].social_places
        work_id = volk[i].work
        my_work = work[work_id]
        nr_people_at_work = my_work.number()
        distance_work_home = my_home.distance(my_work)
                                                         
        # lets gather some data about the socializing places of the individual number i
        nr_socialplaces = np.size(list_of_social_places)
        social_sum = 0
        social_max = 0
        distance_work_social_place = 0
        distance_home_social_place = 0
        
        for j in range(0, nr_socialplaces):
            spid = int(list_of_social_places[j])
            this_social_place = social_place[spid]
            tmp = this_social_place.number()
            social_sum += tmp
            if ( tmp > social_max ):
                social_max = tmp
            distance_work_social_place += my_work.distance(this_social_place) / nr_socialplaces
            distance_home_social_place += my_home.distance(this_social_place) / nr_socialplaces

        total_distance = distance_home_social_place + distance_work_social_place + distance_work_home
        
        if (i==0):
            city.finalreportfile.write('# (1) id \t\n# (2) nr_people_in_home \t\n# (3) nr_people_at_work \t\n# (4) nr_socialplaces \t\n# (5) total_number of people in the socialing places \t\n# (6) maximum number of people in socialing places \t\n# (7) distance_work_home \t\n# (8) ave distance_work_social_place \t\n# (9) distance_home_social_place \t\n# (10) ave total_distance \t\n# (11) status \n')
        city.finalreportfile.write(str(i)+ ' ' + str(nr_people_in_home) + ' ' + str(nr_people_at_work) + '  ' + str(nr_socialplaces) + '  ' + str(social_sum) + '  ' + str(social_max)+ '  ' + str(distance_work_home) + '  ' + str(distance_work_social_place) + '  ' + str(distance_home_social_place) + '  ' + str(total_distance) + '  ' + str(volk[i].immunity) + '\n')
        
    
def create_city_from_a_cookbook(inputfilename):

    print('# inputfile: '+ inputfilename+'\n')

    inputfile = open(inputfilename, 'r')
    random_seed = int(inputfile.readline().split()[0]) # the random seed
    print('# random seed: '+str(random_seed)+'\n')
    nr_people = int(inputfile.readline().split()[0]) # number of citizens
    print('# nr_people: '+str(nr_people)+'\n')
    nr_homes = int(inputfile.readline().split()[0]) # number of homes
    print('# nr_homes: '+str(nr_homes)+'\n')
    nr_workplaces = int(inputfile.readline().split()[0]) # number of work_places
    print('# nr_workplaces: '+str(nr_workplaces)+'\n')
    nr_socialplaces = int(inputfile.readline().split()[0]) # number of social places 
    print('# nr_socialplaces: '+str(nr_socialplaces)+'\n')
    city_size = int(inputfile.readline().split()[0]) # the spatial dimension of the city
    print('# city_size: '+str(city_size)+'\n')
    percentage = float(inputfile.readline().split()[0]) # the approximate percentage of infected people at the beginning
    print('# percentage: '+str(percentage)+'\n')
    contagiosity = float(inputfile.readline().split()[0]) # the probability that you get infected if you are close to an infected person for a timestep inputfile.readline().split()[0]
    print('# contagiosity: '+str(contagiosity)+'\n')
    immunity_step = float(inputfile.readline().split()[0]) #increase of immunity per step for the infected; it is chosen such that it is smaller than 1/(number of steps per day), so the infected person does not heal over one day
    print('# immunity_step: '+str(immunity_step)+'\n')
    alpha = float(inputfile.readline().split()[0]) # let it be! :D
    print('# alpha: '+str(alpha)+'\n')
    
    # True: shows every one at every time step, False: no over of the city
    live_cam = inputfile.readline().strip().split()[0]
    if (live_cam == 'False'):
        live_cam = False 
    else:
        live_cam = True
    print('# live_cam: '+str(live_cam)+'\n')

    # True:updates the graph of information every timestep. If False, it only shows the change after each commute or shift
    live_stat = inputfile.readline().strip().split()[0]
    if (live_stat == 'False'):
        live_stat = False 
    else:
        live_stat = True
    print('# live_stat: '+str(live_stat)+'\n')

    # True: completely mutes the graphical outputs
    mute = inputfile.readline().strip().split()[0]
    if (mute == 'False'):
        mute = False 
    else:
        mute = True
    print('# mute: '+str(mute)+'\n')
    
    max_individual_sociality = int(inputfile.readline().split()[0]) # maximum number of social places that one can go
    print('# max_individual_sociality: '+str(max_individual_sociality)+'\n')
    
    random.seed(random_seed)
    np.random.seed(random_seed)
    my_city = city(nr_people, nr_homes, nr_workplaces, nr_socialplaces, city_size, percentage, contagiosity, immunity_step, alpha, 0, live_cam, live_stat, mute, max_individual_sociality)

    return my_city

def city_statistics(city, volk, home, work_place, social_place):

    sociality = np.zeros(city.nr_people)
    for i in range(0, city.nr_people):
        sociality[i] = np.size(volk[i].social_places)
    hy, hx = np.histogram(sociality, density = True)
    hxcorrected = np.zeros(np.size(hy))
    for binid in range(0,np.size(hy)):
        hxcorrected[binid] = 0.5*(hx[binid] + hx[binid+1])
    np.savetxt('sociality.hist', np.transpose((hxcorrected,hy)))

    
    workspace_pop = np.zeros(city.nr_workplaces)
    for i in range(0, city.nr_workplaces):
        workspace_pop[i] = work_place[i].number()
    hy, hx = np.histogram(workspace_pop, density = True)
    hxcorrected = np.zeros(np.size(hy))
    for binid in range(0,np.size(hy)):
        hxcorrected[binid] = 0.5*(hx[binid] + hx[binid+1])
    np.savetxt('workspace_population.hist', np.transpose((hxcorrected,hy)))


    socialplaces_pop = np.zeros(city.nr_socialplaces)
    for i in range(0, city.nr_socialplaces):
        socialplaces_pop[i] = social_place[i].number()
    hy, hx = np.histogram(socialplaces_pop, density = True)
    hxcorrected = np.zeros(np.size(hy))
    for binid in range(0,np.size(hy)):
        hxcorrected[binid] = 0.5*(hx[binid] + hx[binid+1])
    np.savetxt('socialplaces_population.hist', np.transpose((hxcorrected,hy)))
    
    
    homes_pop = np.zeros(city.nr_homes)
    for i in range(0, city.nr_homes):
        homes_pop[i] = home[i].number()
    hy, hx = np.histogram(homes_pop, density = True)
    hxcorrected = np.zeros(np.size(hy))
    for binid in range(0,np.size(hy)):
        hxcorrected[binid] = 0.5*(hx[binid] + hx[binid+1])
    np.savetxt('homes_population.hist', np.transpose((hxcorrected,hy)))
    
    
