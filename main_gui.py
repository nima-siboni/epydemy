from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
import matplotlib.pyplot as plt
import numpy as np

from backend import simulation    

energy = 100
hours = 4

class Hello(FloatLayout):
    def __init__(self,**kwargs):
        super(Hello,self).__init__(**kwargs)
        


        self.label1 = Label(text = "nr_people", size_hint=(0.47, .05),pos_hint={'x':0.02, 'y':.9})
        self.text1 = TextInput(text='400', size_hint=(0.47, .05),pos_hint={'x':0.51, 'y':0.9})
        
        self.label2 = Label(text = "nr_homes", size_hint=(0.47, .05),pos_hint={'x':0.02, 'y':.85})
        self.text2 = TextInput(text='100', size_hint=(0.47, .05),pos_hint={'x':0.51, 'y':0.85})
        
        self.label3 = Label(text = "nr_workplaces", size_hint=(0.47, .05),pos_hint={'x':0.02, 'y':.8})
        self.text3 = TextInput(text='10', size_hint=(0.47, .05),pos_hint={'x':0.51, 'y':0.8})
        
        self.label4 = Label(text = "nr_socialplaces", size_hint=(0.47, .05),pos_hint={'x':0.02, 'y':.75})
        self.text4 = TextInput(text='40', size_hint=(0.47, .05),pos_hint={'x':0.51, 'y':0.75})
        
        self.label5 = Label(text = "city_size", size_hint=(0.47, .05),pos_hint={'x':0.02, 'y':.7})
        self.text5 = TextInput(text='100', size_hint=(0.47, .05),pos_hint={'x':0.51, 'y':0.7})
        
        self.label6 = Label(text = "percentage", size_hint=(0.47, .05),pos_hint={'x':0.02, 'y':.65})
        self.text6 = TextInput(text='0.1', size_hint=(0.47, .05),pos_hint={'x':0.51, 'y':0.65})

        self.label7 = Label(text = "contagiosity", size_hint=(0.47, .05),pos_hint={'x':0.02, 'y':.6})
        self.text7 = TextInput(text='0.0003', size_hint=(0.47, .05),pos_hint={'x':0.51, 'y':0.6})
        
        self.label8 = Label(text = "immunity_step", size_hint=(0.47, .05),pos_hint={'x':0.02, 'y':.55})
        self.text8 = TextInput(text='0.001', size_hint=(0.47, .05),pos_hint={'x':0.51, 'y':0.55})

        self.start_button = Button(text = "Start", size_hint=(.47, .1),pos_hint={'x':0.02, 'y':0.4},on_press = self.start)
        self.stop_button = Button(text = "Stop", size_hint=(.47, .1),pos_hint={'x':0.51, 'y':0.4},on_press = self.stop)

        self.LabelOut = Label(text = "Output", size_hint=(0.96, .3),pos_hint={'x':0.02, 'y':.1})


        self.add_widget(self.label1)
        self.add_widget(self.text1)
        self.add_widget(self.label2)
        self.add_widget(self.text2)
        self.add_widget(self.label3)
        self.add_widget(self.text3)
        self.add_widget(self.label4)
        self.add_widget(self.text4)
        self.add_widget(self.label5)
        self.add_widget(self.text5)
        self.add_widget(self.label6)
        self.add_widget(self.text6)
        self.add_widget(self.label7)
        self.add_widget(self.text7)
        self.add_widget(self.label8)
        self.add_widget(self.text8)
        
        self.add_widget(self.start_button)
        self.add_widget(self.stop_button)
        
        self.add_widget(self.LabelOut)

    def start(self,event):
        
        nr_people = int(self.text1.text)
        nr_homes = int(self.text2.text)
        nr_workplaces = int(self.text3.text)
        nr_socialplaces = int(self.text4.text)
        city_size = int(self.text5.text)
        percentage = float(self.text6.text)
        contagiosity = float(self.text7.text)
        immunity_step = float(self.text8.text)
        self.Sim = simulation(nr_people,nr_homes,nr_workplaces,nr_socialplaces,city_size,percentage,contagiosity,immunity_step)
        self.Sim.Run()
        
    def stop(self,event):
        # somehow stop the simulation!
        return

class epydemy(App):
    def build(self):
        return Hello()
if __name__=="__main__":
     epydemy().run()
