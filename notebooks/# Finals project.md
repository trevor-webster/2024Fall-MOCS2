# Finals project

The purpose of the project is to study the property of [robustness][1] as defined by networksciencebook of a data network that sends packets between nodes of capacity limited by resource constraints. In [Data Networks][5], we push the discussion into the next sections

in this project, we have adapted the discussion from links to node

## Robustness 

Robustness is described in three parts

### Robustness
Robustness is measured by [inverse percolation][2]. It finds the critical threshold $f_c$ of fraction nodes are removed from the network at which the LCC is lost. The further the LCC holds together as the fraction of nodes are removed, is a higher $f_c$, and is indicative of further robustness. The critical threshold can be found for a general network from

$f_c = 1 - \frac{1}{\frac{k^2}{k}-1}$ (8.7) where nodes are randomly removed from the network.

###  Cascading failures
[Cascading failures](https://networksciencebook.com/chapter/8#cascading) whereby failure is induced by neighbors of node and failures propagate to neighbor nodes. This is in contrast to random removal above. The three considerations are
- flow 
- a rule for failure (flow excess to capacity to be shown)
- failure propagates to neighbor nodes


Because such failurs can be quantified by delay $D$ in a congestion problem that has been already studied in [Data Networks][5], we push the discussion into the next section

Cascading failures are studied the following problems

### Delay $D$ 


The delay $D$ is a function of both capacity and flow on a node, it can be expressed as

$D = 1/{\gamma}\sum_{i} \frac{F_i}{C_i - F_i} \le T$(5.40)

Delay $D$ is used as one measure of cascading failure because of these justifications 

> the cost function of Eqs. (5.29) and (5.30) represents a useful measure of performance in practice, principally
because it expresses qualitatively that congestion sets in when a flow $F$ approaches the
corresponding link capacity $C$ .


> When the offered load is excessive, a portion will be rejected by the flow control algorithm 

Because a rejected packet is retransmitted, it explains one mechanism that justifies why $D$ increases when failure happens,

According to (6.1) fitness is not assigned by any individual, but reflects the network’s collective perception of a node’s importance relative to the other nodes. We can, therefore, determine a node’s fitness by comparing its time evolution to the time evolution of other nodes in the network. 
- flow
- breakdown rule
- failure propagation quantified as $D$ and $S$ the size of the node failure

(where $F_i$ is flow measured in data units per unit time $\gamma$ is the total arrival rate into the network)

Delay is relevant to the robustness  When a network is congested, possibly due to sub-optimal assignment of capacity, packets fail at nodes where $F_i$ approaches $C_i$ and $D$ is high. Therefore this project finds failures that are from congestion and measurable by delay to be a distinct category of failures from the random failures measuruable by robustness $p_c$.


### Resilience 
> A system is resilient if it can adapt to internal and external errors by changing its mode of operation, without losing its ability to function. Hence resilience is a dynamical property that requires a shift in the system's core activities.
(8.8)

Resilience is evaluated by how well the network adapts to congestion.  Network congestion can begin to be quantified as flow $F_i$ expressed in data units/sec at node $i$. A cost function used in optimization includes capacity $C_i$ is

$ D_{ij}(F_{ij})=\frac{F_i}{C_i - F_i} $ ([Data Networks](https://web.mit.edu/dimitrib/www/Routing_Data_Nets.pdf) (5.30)

where delay $D_{ij}$ expresses qualitatively that congestion sets in when a flow $F_i$ approaches the corresponding capacity $C_i$ (434)

The flow and [breakdown rule] wasn't covered in depth in networksciencebook so t

We will find which of network routing models are more adaptive in the sense of (8.8) its use of topology by measuing congestion and potentially cascading failures to be described below. They could be argued as adaptive networks in the sense of [Sayama](https://math.libretexts.org/Bookshelves/Scientific_Computing_Simulations_and_Modeling/Introduction_to_the_Modeling_and_Analysis_of_Complex_Systems_(Sayama)/16%3A_Dynamical_Networks_I__Modeling/16.04%3A_Simulating_Adaptive_Networks) that the effectively used topology changes.

1. Shortest path routing, that is minimally adaptive, deterministic, and continues to use the shortest path, ignoring the flow and capacities of nodes.
2. Hot potato (deflection) routing ([Data Networks](https://web.mit.edu/dimitrib/www/Routing_Data_Nets.pdf) 372) is the candidate to be considered as adaptive, is nondeterministic, while also obeying the rule to minimize load on any one node ([Data Networks](https://web.mit.edu/dimitrib/www/Routing_Data_Nets.pdf) 367,437). It deflects packets to all neighbors randomly. It also has similarity to diffusion as described in Sayama to sum the inputs of a node's neighbors and move its state to its neighbors.


### Capacity assignment problem

As cascading failures follow a breakdown rule that is governed by capacity, the network topology  capacity can influence whether flow becomes failure then 

We solve the problem of capacity assignment as defined in 5.34 of [Data Networks](https://web.mit.edu/dimitrib/www/Routing_Data_Nets.pdf) to choose the capacity of each node $i$ so as to minimize the linear cost 

$\sum_{ij} p_{ij} C_{ij}$ 

that for the current study has been adapted for nodes ${i}$ as

$\sum_{i} p_{i} C_{i}$ where $p_i$ is a price per unit capacity, and e 


subject to constraint that delay $D$ not exceed a given constant $T$ (see Methods for its use in cascading failure)

$D = 1/{\gamma}\sum_{i} \frac{F_i}{C_i - F_i} \le T$(5.35)

The authors suggest that the optimal solution is a minimal connectivity topology that eliminates all links except those which have just enough capacity (442), and we will demonstrate if this holds.



by finding optimal topologies that minimize cost of within reliability and delay constraints. 

### Heuristic methods for capacity assignment

These methods perturb a network topology by changing capacities of nodes, searching around a current topology to be evaluated with respect to. (442)

We borrow and restate these methods. At the start of each iteration, there is available a current best topology and a trial topology.
1. Assign flows. Flows are found from statistics. We used the average flow per node
2. Evaluate delay $D$ per packet
3. Check reliability. We use the robustness measure $f_c$
4. Check cost improvement
5. Use some heuristic to change one or more capacities of the current best topology, thereby obtaining a trial topology that has not been considered before.

## Methods


Failure is simulated where a packet fails at a node when the node's capacity is exceeded. The packet is then retried on an end-to-end basis, recycled back into the network. The failure may propagate to other nodes. Cascading failure is to be studied if it emerges

Parameters to vary topologies are from Evolving networks 
- [internal links][7] by random attachment according to the Evolving Networks of networksciencebook
- [Aging][9] parameter $\nu$ that governs dependence of attachment proabability on node's age

### Capacity assignment problem



## Results

### Robustness

Robustness for internal links added by random attachment parameter $n$ showed a logarithmic growth of the critical fraction $f_c$ with respect to $n$ to loose the LCC, suggesting diminishing returns at $n=5$

Robustness for aging showed a negative power law relationship to aging parameter $nu$. Plotting on a semilog plot, shows a straight line, suggesting decay.

cascadin failures, 
nodes are colored by number failures

then we declare constraints and find lowest cost
- internal link


## Footnotes
  [1]: (https://networksciencebook.com/chapter/8#robustness)
  [2]: (https://networksciencebook.com/chapter/8#percolation-theory)
  [4]: (https://networksciencebook.com/chapter/8#summary8:~:text=Robustness%2C%20Resilience%2C%20Redundancy)
  [5]: https://web.mit.edu/dimitrib/www/Routing_Data_Nets.pdf
  [6]: https://networksciencebook.com/chapter/6#evolving-network
  [7]: https://networksciencebook.com/chapter/6#evolving-networks:~:text=Random%20Attachment%20(B%3D0)%0AIn%20this%20case%20the%20internal%20links
  [9]: https://networksciencebook.com/chapter/6#evolving-networks
  [8]: http://www.wolframalpha.com/input/?i=x%5E4-4x%5E2%2bx%2b1
  
