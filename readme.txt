The Minority Game is a widely used model to reproduce market features.
In the basic Minority Game, an odd number N of agents compete in successive rounds where they can choose between two options, say −1 or 1, wanting to be in the minority side each round. The motivation is that, for example, if you want to sell an asset in the next time step, you want that the most part of people were willing to buy assets, so to increase its price when finally all perform an action. So, if you succeed you get a reward, otherwise you get punished. At the beginning of the game each agent is assigned a number of random strategies, which will govern the agent’s behaviour. To choose what strategy to use each round, each is assigned a score based on how well it has performed (virtually) so far,the one with leading score is used at a time step.


Material
method.py : Basic program where all necessary functions for the first part are defined. Two main groups of functions are defined, one for the basic analysis of the MG, with different functions in order to extract different kind of results. The second group includes modifications in order to study basic mechanisms in market dynamics, such as having different kinds of agents (types of customers) and the inclusion of privileged agents.
PlotCanvas.py : Basic program for the graph. It basically integrates a graph into PyQT which plots the results of each simulation and uses python in order to execute. 
App_framework.py: Runs the GUI
Nother.py- performs same task as app_famework (extraneous file.
Simulation.ui- Contains the predesigned QT interface
Start.py- runs the program
 
 
 
 
Tasks
 Basic naming game; volatility, phase transition, polarization, frozen agents and predictability.
 Basic naming game with change of variables; speeded up.
 Check the good convergence of the simulation in order to take good statistics.
 Analytical calculations to check numerical ones.
 Modeling market mechanism with minority game: Speculators and Producers, Noise traders, Quitters, multiple strategies, spies.
 Creative part: Imitation of successful strategies in an interwined dynamics scope, through a social layer defined as a complex graph with different kinds of topology (random, Small-World and Scale-free graph)
 Final manuscript explaining in great detail all the theory and results.

