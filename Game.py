from Graph import *
from Player import Player
import random

class Game:

    def __init__(self, numVertices, extra_turn):
        self.graph = Graph(numVertices)
        self.extra_turn = extra_turn
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.turn = self.player1

    # returns true if point awarded
    def remove_bar(self, player, v1, v2):
        removal = False
        self.graph.remove_edge(v1, v2)
        if v1 not in self.graph.adj_list:
            player.score += 1
            removal = True
        if v2 not in self.graph.adj_list:
            player.score += 1
            removal = True
        return removal

    
    def change_turns(self):
        if self.turn == self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1


    def make_choice(self, strategy):
        if not strategy and self.turn == self.player2:
            v1 = random.choice(list(self.graph.adj_list.keys()))
            v2 = random.choice(self.graph.adj_list[v1])
            return(v1, v2)

        
        min_degree = self.graph.get_min_degree()
        max_degree = self.graph.get_max_degree()
        if min_degree == 1 and len(self.graph.degree_d[min_degree]) > 1:
            leaves = self.graph.degree_d[min_degree]
            if self.extra_turn:
                one_to_two = self.graph.check_neighbor_degrees(leaves, 2)
                if one_to_two:
                    v1 = random.choice(one_to_two)
                    v2 = self.graph.adj_list[v1][0]
                    return (v1, v2)
            one_to_one = self.graph.check_neighbor_degrees(leaves, 1)
            if one_to_one:
                v1 = random.choice(one_to_one)
                v2 = self.graph.adj_list[v1][0]
            else:
                one_to_greatertwo = self.graph.check_neighbor_degrees_greater(leaves, 2)
                if one_to_greatertwo:
                    v1 = random.choice(one_to_greatertwo)
                    v2 = self.graph.adj_list[v1][0]
                else:
                    v1 = random.choice(leaves)
                    v2 = self.graph.adj_list[v1][0]
        elif min_degree == 1:
            v1 = self.graph.degree_d[min_degree][0]
            v2 = self.graph.adj_list[v1][0]
        else:
            degree_greater_two = []
            for degree in range(3, max_degree + 1):
                for vertex in self.graph.degree_d[degree]:
                    degree_greater_two.append(vertex)
            if degree_greater_two:
                greatertwo_to_greatertwo = self.graph.check_neighbor_degrees_greater(degree_greater_two, 2)
                if greatertwo_to_greatertwo:
                    v1 = random.choice(greatertwo_to_greatertwo)
                    neighbors_greater_two = []
                    for neighbor in self.graph.adj_list[v1]:
                        if len(self.graph.adj_list[neighbor]) > 2:
                            neighbors_greater_two.append(neighbor)
                    v2 = random.choice(neighbors_greater_two)
                else:
                    v1 = random.choice(degree_greater_two)
                    v2 = random.choice(self.graph.adj_list[v1])
            else:
                v1 = random.choice(list(self.graph.adj_list.keys()))
                v2 = random.choice(self.graph.adj_list[v1])
        return (v1, v2)
            
