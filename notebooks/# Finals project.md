# Finals project

The purpose of the project is to study the property of [robustness][1] as defined by networksciencebook of a data network that sends packets between nodes of capacity limited by resource constraints.

## Robustness is described in two parts

Robustness is described in two parts

1. Robustness is measured by [inverse percolation][2]. It finds the critical threshold $f_c$ of fraction nodes are removed from the network at which the LCC is lost. The further the LCC holds together as the fraction of nodes are removed, is a higher $f_c$, and is indicative of further robustness. The critical threshold can be found for a general network from

$f_c = 1 - \frac{1}{\frac{k^2}{k}-1}$ (8.7) where nodes are randomly removed from the network.

2.  [Cascading failures](https://networksciencebook.com/chapter/8#cascading) whereby failure is induced by neighbors node and failures propagate to neighbor nodes. The three considerations are
- flow 
- a rule for failure (flow excess to capacity to be shown)
- failure propagates to neighbor nodes

Robustness can be characterized as a more static evaluation of the 

Because such failurs can be quantified by delay $D$ a problem that has been already studied in [Data Networks][5], we push the discussion into the next sections




2. Resilience 
> A system is resilient if it can adapt to internal and external errors by changing its mode of operation, without losing its ability to function. Hence resilience is a dynamical property that requires a shift in the system's core activities.
(8.8)

Resilience is evaluated by how well the network adapts to congestion.  Network congestion can begin to be quantified as flow $F_i$ expressed in data units/sec at node $i$. A cost function used in optimization includes capacity $C_i$ is

$ D_{ij}(F_{ij})=\frac{F_i}{C_i - F_i} $ ([Data Networks](https://web.mit.edu/dimitrib/www/Routing_Data_Nets.pdf) (5.30)

where delay $D_{ij}$ expresses qualitatively that congestion sets in when a flow $F_i$ approaches the corresponding capacity $C_i$ (434)

The flow and [breakdown rule] wasn't covered in depth in networksciencebook so t

We will find which of network routing models are more adaptive in the sense of (8.8) its use of topology by measuing congestion and potentially cascading failures to be described below. They could be argued as adaptive networks in the sense of [Sayama](https://math.libretexts.org/Bookshelves/Scientific_Computing_Simulations_and_Modeling/Introduction_to_the_Modeling_and_Analysis_of_Complex_Systems_(Sayama)/16%3A_Dynamical_Networks_I__Modeling/16.04%3A_Simulating_Adaptive_Networks) that the effectively used topology changes.

1. Shortest path routing, that is minimally adaptive, deterministic, and continues to use the shortest path, ignoring the flow and capacities of nodes.
2. Hot potato (deflection) routing ([Data Networks](https://web.mit.edu/dimitrib/www/Routing_Data_Nets.pdf) 372) is the candidate to be considered as adaptive, is nondeterministic, while also obeying the rule to minimize load on any one node ([Data Networks](https://web.mit.edu/dimitrib/www/Routing_Data_Nets.pdf) 367,437). It deflects packets to all neighbors randomly. It also has similarity to diffusion as described in Sayama to sum the inputs of a node's neighbors and move its state to its neighbors.

The next purpose is to solve the problem of capacity assignment as defined in 5.34 of [Data Networks](https://web.mit.edu/dimitrib/www/Routing_Data_Nets.pdf) to choose the capacity of each node $i$ so as to minimize the linear cost 

$\sum_{i} p_{i} C_{i}$ where $p_i$ is a price per unit capacity, 


subject to constraint that delay not exceed a given constant $T$

$D = 1/{\gamma}\sum_{i} \frac{F_i}{C_i - F_i} \le T$(5.35)

The authors suggest that the optimal solution is a minimal connectivity topology that eliminates all links except those which have just enough capacity (442), and we will demonstrate if this holds.



by finding optimal topologies that minimize cost of within reliability and delay constraints. 

The delay $D$ is a function of both capacity and flow on a node, it can be expressed as

$D = 1/{\gamma}\sum_{i} \frac{F_i}{C_i - F_i} \le T$(5.40)

(where $F_i$ is flow measured in data units per unit time $\gamma$ is the total arrival rate into the network)

however it can be readily found in data on hops for packet to reach destination. Delay is relevant to the robustness  When a network is congested, possibly due to sub-optimal assignment of capacity, packets fail at nodes where $F_i$ approaches $C_i$ and $D$ is high. Therefore this project finds failures that are from congestion and measurable by delay to be a distinct category of failures from the random failures measuruable by robustness $p_c$.


https://networksciencebook.com/chapter/6#evolving-network

## Methods
Failure is simulated where a packet fails at a node when the node's capacity is exceeded. The packet is then retried on an end-to-end basis, recycled back into the network. The failure may propagate to other nodes. Cascading failure is to be studied if it emerges

Parameters to vary topologies are from Evolving networks 
- [internal links][7] by random attachment according to the Evolving Networks of networksciencebook
- [Aging][9] parameter $\nu$ that governs dependence of attachment proabability on node's age


## Results

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
  
