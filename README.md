# Combinatorics Game Simulator
Generates specific graph types and simulates the winner of a two-person combinatorics game based on a set of strategies

## "Stars and Bars"
This combinatorics game is played on a graph of vertices (represented as stars) with edges between them. Each player takes a turn removing an edge from the graph. If a star/vertex is left with no neighbors then it "falls" off the graph and can be collected by the last player to remove an edge. After all edges are removed, the player having collected the most stars is the winner.

## Implementation
The Graph class utilizes an adjacency list to keep track of the "gameboard." The following graph types were simulated given a set of n vertices:
* Bipartite
* Clique
* Cycle
* Randomly connected
