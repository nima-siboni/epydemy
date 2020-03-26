# epydemy

### An agent-based epidemy simulator in Python

A city with its citizens and their social life are simulated where a contagious disease is spreading.  

The city consists of :

- a number of people,  
- their houses where the number of inhabitants differ from house to house (and happily no homeless person in our city),  
- a number of work places with a random distribution of number of employees,  
- a number of gathering places for people to socialize (and transmit diseases!!!), social people have many places to socialize, not-social people go home instead, and  
- a municipality which might intervene with people's life.  

Everyday people go happily from home to work to gathering places and back to home!
  
Meanwhile there is a disease (with tunable contagiosity rate) is spreading via contact between people! Infected people either die (not yet implemented, thanks god!) or get immune.  
  
The results of the simulation are used to feed a neural network for predicting the probability of catching the disease for each individual based on a certain number of features.

You can start the simulation simply by

```
python simulation.py

```
To run the gui version first install the dependencies

``` 
pip3 install kivy

```
then run 
```
python main_gui.py

```
