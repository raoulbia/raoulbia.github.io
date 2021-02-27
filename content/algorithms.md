Title: Algorithms
Date: 2017-10-02
Category: Algorithms
Slug: Algorithms
Summary: Some notes about Algorithms

On this page I keep some notes abbout Algorithms. It's work in progress and all might not be 
accurate. I will improve this page as my grasp of the key differences between the core algorithm 
families improves. 

**Introduction**

Many graph-based problems are of the non-deterministic polynomial time (NP) problem family.  
Specifically this means that graph-based problems can often not be solved efficiently w.r.t. time and 
space. For example, consider that the optimal solution for a given graph-based problem involves 
visiting all nodes and vertices in the graph. Such an exhaustive search is unfeasible with large 
graphs consisting of millions of nodes and vertices.

**Algorithms**

There are several alternative strategies to deal with NP problems that avoid the limitations of 
exhaustive search. These strategies do not, in general, find optimal solutions, but can find solutions 
that are reasonably close to being optimal. Such strategies include 

* greedy algorithms
* heuristic algorithms 
* approximation algorithms
* randomized algorithms 

The idea of greedy algorithm is to solve a problem by making a “locally optimal choice at each stage
with the hope of finding a global optimum ”. 
 
Heuristic algorithm try to solve a problem by “proceeding to a solution by trial and error or by 
rules that are only loosely defined ”. 

The lines between greedy and heuristic algorithms are often blurred and many algorithms exhibit 
characteristics of both. 

Approximation algorithms are essentially heuristic algorithms with a provable guarantee on the 
quality of the obtained near-optimal solution.

Randomized algorithms may be nonintuitive because they lack the control of traditional algorithms.
Some randomized algorithms are *Las Vegas algorithms*, which deliver solutions that are guaranteed 
to be exact, despite the fact that they rely on making random decisions. Yet most randomized 
algorithms are *Monte Carlo algorithms*. These algorithms are not guaranteed to return exact solutions,
but they do quickly find approximate solutions. Because of their speed, they can be run many times, 
allowing us to choose the best approximation from thousands of runs.
