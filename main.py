from  PyQt5 import QtWidgets
from  PyQt5.uic  import  loadUi
from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )
import  numpy  as  np 
import random
from itertools import count
import matplotlib.pyplot as mp
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from  matplotlib.backends.backend_qt5agg  import  FigureCanvas
from  matplotlib.figure  import  Figure
from start import *
import methods as mtd

class  MatplotlibWidget ( QtWidgets.QMainWindow ):
    
    def  __init__ ( self ):
        
        QtWidgets.QMainWindow . __init__ ( self )

        loadUi ( "simulation.ui" , self )
        self . setWindowTitle ( "MINORITY GAME GROUP 3" )
        self . runSim . clicked . connect ( self . PlotCanvas. plot )



app  =  QtWidgets.QApplication ([]) 
window  =  MatplotlibWidget () 
window.setFixedWidth(1605)
window.setFixedHeight(1006)

window . show () 
app . exec_ ()
