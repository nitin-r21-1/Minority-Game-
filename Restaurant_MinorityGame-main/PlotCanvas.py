# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import methods as mtd
import random
import matplotlib.pyplot as mp
INPUT_PARAMS = {'weather_condition' : 1 , 'rate_of_spread': .5 , 'restaurant_capacity' : 100 ,'un_employment_rate': 0.1,  'num_agents' : 80 , 'num_rounds' : 20}
NUM_STRGY = 10
NUM_RESTAURANTS = 10 
AVG_RESTAURANT_CAP= 1000 
population= 100

class agent:
    def __init__(self, strgy):
        self.strgy = strgy
        self.top_strgy = random.randint(0,9) #giving random strategy the best strategy
        self.top_strgy_score = 0
    def best_strgy(self , idx):
        self.top_strgy = idx
    def increase_top_score(self):
        self.top_strgy_score +=1
    def decrease_top_score(self):
        self.top_strgy_score = max(0,self.top_strgy_score-1)
    def cur_predict(self, num):
        self.predicted_going = num
    def get_cur_predict(self):
        return self.predicted_going


class strgy:
    """docstring for ."""
    def __init__(self, weights):
        self.w = arg
        self.best_score = 0








class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)


    def plot(self):
        mp.clf()
        agents = mtd.compute_agent_strgy( NUM_STRGY , INPUT_PARAMS )
        Global_mem = mtd.compute_random_mem(population)
        thrs_hold = mtd.compute_thrshold(NUM_RESTAURANTS, AVG_RESTAURANT_CAP, INPUT_PARAMS)
        for index in range(0,INPUT_PARAMS['num_rounds']):
            agent_decision , num_going , num_notgoing = mtd.compute_agent_decision(agents, Global_mem ,thrs_hold)
            ax = self.figure.add_subplot(111)
            ax.plot(index, num_going, 'or')
            ax.set_title('Minority Game Simulation')
            self.draw() 
            winner_loser= mtd.get_winner_loosers( agent_decision, num_going, num_notgoing)
            for agent in agents:
                mtd.compute_new_best(agents,winner_loser, agent_decision, num_going, Global_mem) 
    def twotwo(self):
        print("22222")
        #ax = self.figure.add_subplot(111)
        #ax.plot(index, num_going, 'or')
        #ax.set_title('Minority Game Simulation')
    #def retrieve(self):    
