import random

class Graph:

    def __init__(self, numVertices):
        self.v = [chr(i) for i in range(65, 65 + numVertices)]
        self.adj_list = {key: [] for key in self.v}
        self.degree_d = {}


    def make_degree_d(self):
        max_degree = 0
        for vertex in self.adj_list:
            degree = len(self.adj_list[vertex])
            max_degree = max(max_degree, degree)
            if degree not in self.degree_d:
                self.degree_d[degree] = [vertex]
            else:
                self.degree_d[degree].append(vertex)

            for i in range(1, max_degree):
                if i not in self.degree_d:
                    self.degree_d[i] = []

    def get_min_degree(self):
        min_degree = 1
        while len(self.degree_d[min_degree]) == 0:
            min_degree +=1
        return min_degree

    def get_max_degree(self):
        max_degree = 0
        for degree in range(1, len(self.degree_d) + 1):
            if len(self.degree_d[degree]) > 0:
                max_degree = degree
        return max_degree

    def make_bipartite_graph(self):
        middleIndex = len(self.v)//2
        a = self.v[:middleIndex]
        b = self.v[middleIndex:]
        for aVertex in a:
            for bVertex in b:
                if bVertex not in self.adj_list[aVertex]:
                    self.adj_list[aVertex].append(bVertex)
                    self.adj_list[bVertex].append(aVertex)
        self.make_degree_d()
            

    def make_cycle_graph(self):
        for i in range(len(self.v)):
            adj1 = (i - 1) % len(self.v)
            adj2 = (i + 1) % len(self.v)
            self.adj_list[self.v[i]].append(self.v[adj1])
            self.adj_list[self.v[i]].append(self.v[adj2])
        self.make_degree_d()


    def make_clique_graph(self):
        for i in range(len(self.v)):
            for j in range(len(self.v)):
                if i != j and j not in self.adj_list[self.v[i]]:
                    self.adj_list[self.v[i]].append(self.v[j])
        self.make_degree_d()


    def make_random_graph(self):
        for i in range(len(self.v)):
            for j in range(len(self.v)):
                if i != j and j not in self.adj_list[self.v[i]] and random.random() < .5:
                    self.adj_list[self.v[i]].append(self.v[j])
                    self.adj_list[self.v[j]].append(self.v[i])
        for i in range(len(self.v)):
            if len(self.adj_list[self.v[i]]) == 0:
                other_vertices = []
                for j in range(len(self.v)):
                    if j != i:
                        other_vertices.append(self.v[j])
                adj_vert = random.choice(other_vertices)
                self.adj_list[self.v[i]].append(adj_vert)
                self.adj_list[adj_vert].append(self.v[i])
        self.make_degree_d()
        

    # accepts list of vertices
    # returns list of these vertices who have neighbors with degree = passed in degree
    def check_neighbor_degrees(self, vertices, neighbor_degree):
        new_vertices = []
        for vertex in vertices:
            for adj_vert in self.adj_list[vertex]:
                if vertex not in new_vertices and len(self.adj_list[adj_vert]) == neighbor_degree:
                    new_vertices.append(vertex)
        return new_vertices

    # accepts list of vertices 
    # returns list of these vertices who have neighbors with degree >= passed in degree
    def check_neighbor_degrees_greater(self, vertices, neighbor_degree):
        new_vertices = []
        for vertex in vertices:
            for adj_vert in self.adj_list[vertex]:
                if vertex not in new_vertices and len(self.adj_list[adj_vert]) > neighbor_degree:
                    new_vertices.append(vertex)
        return new_vertices


    def remove_edge(self, v1, v2):
        v1_degree = len(self.adj_list[v1])
        self.adj_list[v1].remove(v2)
        self.degree_d[v1_degree].remove(v1)
        if v1_degree > 1:
            self.degree_d[v1_degree - 1].append(v1)
        else:
            del self.adj_list[v1]


        v2_degree = len(self.adj_list[v2])
        self.adj_list[v2].remove(v1)
        self.degree_d[v2_degree].remove(v2)
        if v2_degree > 1:
            self.degree_d[v2_degree - 1].append(v2)
        else:
            del self.adj_list[v2]
