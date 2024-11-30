import pycxsimulator
from pylab import *
from math import *

import networkx as nx

def initialize():
    global g, nextg
    g = nx.karate_club_graph()
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['state'] = 1 if random() < .5 else 0
    nextg = g.copy()
    nextg.pos = g.pos
    
def observe():
    global g, nextg
    cla()
    nx.draw(g, cmap = cm.Spectral, vmin = 0, vmax = 1,
            node_color = [g.nodes[i]['state'] for i in g.nodes],
            pos = g.pos)

alpha = 1 # diffusion constant
Dt = 0.01 # Delta t

#hot potato diffusion
def update():
    global g, nextg
    for i in g.nodes:
        ci = g.nodes[i]['state'] 
        nextg.nodes[i]['state'] = ci + alpha * (
            sum(1 if g.nodes[j]['state'] > 0 else 0 for j in g.neighbors(i) )  # Sum positive neighbors' states
            - 1 * g.degree(i)
) * Dt

    g, nextg = nextg, g

pycxsimulator.GUI().start(func=[initialize, observe, update])
