import pycxsimulator
from pylab import *

import networkx as nx

def initialize():
    global g, nextg
    g = nx.karate_club_graph()
    for i, j in g.edges:
        g.edges[i, j]['weight'] = 0.5
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['state'] = 1 if g.nodes[i]['club'] == 'Mr. Hi' else 0
    nextg = g.copy()
    nextg.pos = g.pos
    
def observe():
    global g, nextg
    cla()
    nx.draw(g, cmap = cm.Spectral, vmin = 0, vmax = 1,
            node_color = [g.nodes[i]['state'] for i in g.nodes],
            edge_cmap = cm.binary, edge_vmin = 0, edge_vmax = 1,
            edge_color = [g.edges[i, j]['weight'] for i, j in g.edges],
            pos = g.pos)

alpha = 1 # diffusion constant
beta =  3 # rate of adaptive edge weight change
gamma = 3 # pickiness of nodes
Dt = 0.01 # Delta t

def update():
    global g, nextg
    for i in g.nodes:
        ci = g.nodes[i]['state']
        nextg.nodes[i]['state'] = ci + alpha * ( \
            sum([(g.nodes[j]['state'] - ci) * g.edges[i, j]['weight']
                 for j in g.neighbors(i)])) * Dt
    for i, j in g.edges:
        wij = g.edges[i, j]['weight']
        nextg.edges[i, j]['weight'] = wij + beta * wij * (1 - wij) * ( \
            1 - gamma * abs(g.nodes[i]['state'] - g.nodes[j]['state'])
            ) * Dt
    nextg.pos = nx.spring_layout(nextg, pos = g.pos, iterations = 5)
    g, nextg = nextg, g

pycxsimulator.GUI().start(func=[initialize, observe, update])


import pycxsimulator
from pylab import *
import networkx as nx

history = []
hops= {}
p=0.5
n = 200
t=0
def initialize():
    global g, nextg
    g = G_ba.copy()

    for node in g.nodes:
        g.nodes[node]['packets'] = list()
        g.nodes[node]['capacity'] = 0


    nextg = g.copy()
    nextg.pos = g.pos

def observe():
    global g, nextg
    cla()
    nx.draw(g, cmap = cm.Spectral, vmin = 0, vmax = 1,
            node_color = [g.nodes[i]['state'] for i in g.nodes],
            edge_cmap = cm.binary, edge_vmin = 0, edge_vmax = 1,
            edge_color = [g.edges[i, j]['weight'] for i, j in g.edges],
            pos = g.pos)
    

def update():
    global g, nextg
    failed   = []
    for node in (g.nodes):
        packets = g.nodes[node]['packets']
        next_packets=[]

        # remove failed node
        if len(packets) > g.nodes[node]['capacity']: 
            nextg.remove_edges_from([(node,neighbor) for neighbor in g.neighbors(node)])            
            continue

        for packet in packets:
            o, d, packet_id = packet
            hops[packet] += 1
            if d == node:
                # Packet reaches its destination
                continue
            
            else:
                next_packets.append(packet)
            
        
        while  len(next_packets) > 0:
            packet = next_packets.pop()
            o, d, packet_id = packet
            path = nx.shortest_path(g, source=node, target=d, weight="weight")      
            neighbor = path[1]
            nextg.nodes[neighbor]['packets'].append(packet)
 


        # generate a packet 
        die = random.uniform(0, 1)
        if die<p:
            dest = np.random.choice(list(g.nodes))
            packet = (node, dest, step)
            next_packets.append(packet)
            hops[packet] = 0

            
        # Update the next packets for the node
        nextg.nodes[node]['packets'] = next_packets 

    nextg.pos = nx.spring_layout(nextg, pos = g.pos, iterations = 5)
    history,append((t,g))
    g, nextg = nextg, g

pycxsimulator.GUI().start(func=[initialize, observe, update])
