import matplotlib.pyplot as plt
class city:
    info = 'a container for city/disease properties'

    def __init__(self, nr_people, nr_homes, nr_workplaces, nr_socialplaces, city_size, percentage, contagiosity, immunity_step, alpha, timestep, live_cam, live_stat, mute, max_individual_sociality):
        self.nr_people = nr_people	# number of citizens
        self.nr_homes = nr_homes # number of homes
        self.nr_workplaces = nr_workplaces # number of work_places
        self.nr_socialplaces = nr_socialplaces  # number of social places
        self.city_size = city_size  # the spatial dimension of the city
        self.percentage = percentage # the approximate percentage of infected people at the beginning
        self.contagiosity = contagiosity # the probability that you get infected if you are close to an infected person for a timestep
        self.immunity_step = immunity_step #increase of immunity per step for the infected; it is chosen such that it is smaller than 1/(number of steps per day), so the infected person does not heal over one day
        self.alpha = alpha # let it be! :D
        self.timestep = timestep
        self.reportfile = open("time_resolved_health_reports.dat","w+")
        self.finalreportfile = open("health_reports.dat","w+")
        self.live_cam = live_cam
        self.live_stat = live_stat
        self.fig = None
        self.birdseyeview = None
        self.info_graph = None
        self.mute = mute
        self.max_individual_sociality = max_individual_sociality # the maximum number of social places that a person might go
        
                
