Title: Graphs
Date: 2017-07-01
Category: Graphs
Slug: graphs
Summary: Graph Theory


Under Construction...

#### Graph Notebooks

* <a href="https://nbviewer.jupyter.org/github/raoulbia/ipython/blob/master/induced_voltages.ipynb?flush_cache=true" target="_blank">Vertex Voltages and Delivered Current</a>
* <a href="https://nbviewer.jupyter.org/github/raoulbia/ipython/blob/master/mimimum_spanning_tree.ipynb?flush_cache=true" target="_blank">Minimum Spanning Tree</a>
* <a href="https://github.com/raoulbia/ipython/blob/master/random_walks_on_grid.ipynb?flush_cache=true" target="_blank">Random Walks on a Grid</a>
* <a href="https://nbviewer.jupyter.org/github/raoulbia/ipython/blob/master/pagerank.ipynb?flush_cache=true" target="_blank">Google PageRank Step By Step</a>
* <a href="https://nbviewer.jupyter.org/github/raoulbia/ipython/blob/master/random_walk_with_restart.ipynb?flush_cache=true" target="_blank">Random Walk with Restart</a>
* <a href="https://nbviewer.jupyter.org/github/raoulbia/ipython/blob/master/laplacian_applications.ipynb?flush_cache=true" target="_blank">Application of Laplacian Matrix</a>
* <a href="https://nbviewer.jupyter.org/github/raoulbia/ipython/blob/master/basic_graph_operations.ipynb?flush_cache=true" target="_blank">Basic Operations</a>


#### Knowledge Graphs

* *"Knowledge Discovery is the nontrivial extraction of implicit, previously unknown, and potentially useful information
from data."* (Frawley et al., 1992)

* *"A Knowledge Graph is a directed graph $G = (V, E, R, g)$, where V , E, and R denote
the node, edge, and relation sets, respectively, and $g : E \rightarrow  R$
is a function labeling each edge with a semantic relation or predicate. "* (Shiralkar et al., 2017)


#### Graph Expansion

Adding Facts to a Knowledge Graph - Illustration of 1-, and 2-Hop Graph Expansion in Python: 
<a href="https://nbviewer.jupyter.org/github/raoulbia/jupyter-notebooks/blob/master/KG-Expansion-proteins.svg?flush_cache=true" target="_blank">Proteins KG example</a> and
<a href="https://nbviewer.jupyter.org/github/raoulbia/jupyter-notebooks/blob/master/KG-Expansion-startrek.svg?flush_cache=true" target="_blank">Star Trek KG example</a>


#### How one node may be reached from another one

* A *walk* is an unrestricted sequence of nodes in which a node or an edge may appear more than once. Its length is simply the number of edges in the walk.
* A *trail* is a walk in which no edge is repeated but nodes may be visited more than once.
* A *path* is a trail in which no edge or node is repeated.
* A *cycle* is a trail with at least 3 nodes in which start and end node are the same.
* A *geodesic* between two nodes is a shortest path between them.

#### Connected vs. Strongly Conncected

* An undirected graph is *connected* if, for every pair of nodes *u* and *v*, there is a path from *u* to *v*.
* A directed graph is *strongly connected* if, for every two nodes *u* and *v*, there is a path from *u* to *v* and a path from *v* to *u*.


#### Trees

* An undirected graph is a tree if it is connected and does not contain a cycle.
* A spanning tree of G is a tree that contains all the vertices of G.
* Adding a new edge to a spanning tree always creates a cycle.


#### Explaining RelatednessThe task of explaining the relationship between two or more query nodes involves measuring the relevance of paths in
the graph that connect those query nodes. The connecting paths represent the implicit relations between the query nodes.

* By extension, measuring the relevance of connecting paths involves measuring the relevance of the nodes that are on
  those connecting paths.

* A relevant node is a central node for the (indirect) relation between the query nodes.

* "So, while the nodes that are on relevant connecting paths are explicit and simple — just a set of nodes — they represent
implicit information." (Langohr et al., 2012)


#### The relative importance of nodes

Rusinowska et al. (2011) describe the process of finding the top-k relatively important nodes w.r.t. some query nodes, two steps are required:

* Measure the strength of relations

     * Centrality measures: degree, closeness and betweeness

     * Prestige methods: degree prestige (think PageRank where a node’s importance is determined by the importance of its
       neighbors) and proximity prestige

* Node Ranking

     * RW-based methods


#### What are the characteristics relevant to measuring centrality?

*Network flow processes and the dimensions along which they differ*

* flow pocesses vary along mechansism dimensions:

      * copy mechansims: serial and parallel diffusion via replication
      * move mechansim: objects are indivisible and can only be in one place at a time

* flow pocesses vary along trajectory dimensions: shortest paths, paths, trails or walks

The authors use those two dimensions to construct a topology of flow processes as shown in Table 1 of Borgatti, 2005.

*Indivisibility*

* Objects can only be in one place at a time

      * nodes and edges are used more than once: networked economy > walk-based transfer e.g. money (see also Markov process)
      * nodes may be visited more than once but edges are not re-used: distribution networks > used goods trails
      * nodes and edges are not re-used: delivery networks > package arrives through shortest paths

* Objects can be in several places at once

      * replication flows in which objects are spread one at a time (serial duplication)

           * does not pass same edge twice but can pass the same node more than once: informal network of persons > gossip trails

      * replication flows in which objects are diffused simultaneously (parallel duplication):

           * radio broadcast
           * email communication: nodes and edges visited only once  > path
           * speaker influences audience through interaction: nodes and edges visited only once  > path
           * infection / disease: nodes and edges visited only once  > path

#### Commonly encountered flow processes

* diffusion flows where it matters to be first to get it:

      * general information e.g. R&D technology

* diffusion flows where it matters to know the target and to take the shortest path:

      * package delivery, traffic, telecomms

* flows where reception speed (i.e. shortest path) does not matter i.e. flow has no target and and does not prefer to
  take shortest path

      * gossip
      * infections and diseases

* flows in which traffic is able to move via unrestricted walks rather than being constrained by trails, paths or geodesics:

      * no assumption of transfer or replication one at a time
      * rather it assumes that each node affects all of its neighbours simultaneously (parallel duplication)
      * ideally suited for influence type processes: attitudes, beliefs

           * a node's importance is determined by the importance of its neighbors thus this is also referred to as **prestige**
           * degree centrality can be viewed as a *immediate* influence measure
           * eigenvector centrality can be viewed as a *long-term direct* influence measure


##### Vertex degree centrality measure

* For a random walk on a graph, the limiting probabilities for the nodes are proportional to degree. Hence, the proportion of times that a node is visited is a function of its degree.
* This means that degree centrality is an appropriate measure for **walk-based transfer processes such as the money exchange process**.


##### Spanning vs. Induced Subgraphs ([video](https://www.youtube.com/watch?v=dPHkyRvLtIU&app=desktop))

* A spanning subgraph is a subgraph obtained only by edge deletions. The vertex set of the subgraph is the entire vertex set of the original graph.

* A subgraph obtained only by vertex deletion is called an induced subgraph. When deleting a vertex one must also delete all its incident edges.
The edge set of an induced subgraph is therefore a subset of the edge set of the original graph.


##### Conclusions

It is important to match centrality measures to appropriate kinds of flow processes and the implicit flow characteristics they assume.

#### References

Rusinowska, A., Berghammer, R., De Swart, H. and Grabisch, M. 2011. Social networks: Prestige, centrality, and influence (Invited paper). IN:  de Swart (ed.) RAMICS 2011. Lecture Notes in Computer Science (LNCS) 6663. Springer, pp. 22–39.

Borgatti, S.P. 2005. Centrality and network flow. Social Networks, 27(1), pp.55–71.

Frawley, W.J., Piatetsky-Shapiro, G. and Matheus, C.J. 1992. Knowledge Discovery in Databases: An Overview. AI Mag., 13(3), pp.57–70.

Shiralkar, P., Flammini, A., Menczer, F. and Ciampaglia, G.L. 2017. Finding Streams in Knowledge Graphs to Support Fact Checking. arXiv:1708.07239 [cs].


