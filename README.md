# Combinatorics Game Simulator
Generates specific graph types and simulates the winner of a two-person combinatorics game based on a set of strategies

## "Stars and Bars"
This combinatorics game is played on a graph of vertices (represented as stars) with edges between them. Each player takes a turn removing an edge from the graph. If a star/vertex is left with no neighbors then it "falls" off the graph and can be collected by the last player to remove an edge. After all edges are removed, the player having collected the most stars is the winner.

## Implementation
The Graph class utilizes an adjacency list to keep track of the "gameboard." All graph modifications are handled by this class. The following graph types were simulated given a set of n vertices:
* Bipartite
* Clique
* Cycle
* Randomly connected

Main.py uses the Game class to simulate games. Within the game class, the make_choice method computes the best edge to remove based upon StrategyFlowChart.png

## Results of Simulations
Simulations were run for graphs of 5, 10, 15, and 20 vertices. Half of these tests used a rule that granted players an additional turn if they collected a star on their current turn. The score of player 1, who went first, was compared to player 2’s score following each game to determine the winner. Following each game, both scores were reset. For this first set of simulations, each player made their edge choice based on StrategyFlowChart.png. For each number of vertices (5, 10, 15, 20), the simulation was run 1000 times. The results can be found in SimulationResults.xlsx.

