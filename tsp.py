import networkx as nx

import random

from itertools import permutations

class TSP():
    def __init__(self):
        self.graph = None
        self.pos = None
        self.paths = None
        self.disp_nodes = None
        self.next_node = None
        self.distance = float('inf')
        self.path = ()
        # 0 = brute; 1 = nearest.
        self.algorithm = 0

    def random_graph(self):
        # Reseta os atributos do algoritmo
        self.reset()

        # Gera um grafo completo com 4 ou 5 vértices
        self.graph = nx.complete_graph(random.randint(4, 5))
        self.pos = nx.spring_layout(self.graph)

        # Inicializa o atributo de cor das arestas para preto
        nx.set_edge_attributes(self.graph, 'black', 'color')

        # Gera os pesos das arestas aleatoriamente para valores entre 10 e 50
        for (u, v) in self.graph.edges():
            self.graph[u][v]['weight'] = random.randint(10, 50)

        # Gera os caminhos do grafo (combinações de todos os vértices)
        self.paths = list(permutations(self.graph.nodes()))

        # Gera a lista de nós do grafo e inicializa o nó inicial
        self.disp_nodes = list(self.graph.nodes())
        self.next_node = self.disp_nodes.pop()

    def edge_colors(self, step_path=None):
        if self.graph is not None:
            nx.set_edge_attributes(self.graph, 'black', 'color')
            if self.path is not None:
                for index in range(len(self.path)-1):
                    self.graph[self.path[index]][self.path[index+1]]['color'] = '#2fff28'
            if step_path is not None:
                for index in range(len(step_path)):
                    nexti = index+1 if index < len(step_path)-1 else 0
                    self.graph[step_path[index]][step_path[nexti]]['color'] = 'red'

    def reset(self):
        # Reseta os caminhos, distância mínima e caminho ótimo do grafo
        if self.graph is not None:
            self.paths = list(permutations(self.graph.nodes()))
            self.disp_nodes = list(self.graph.nodes())
            self.next_node = self.disp_nodes.pop()
        else:
            self.paths = None
            self.disp_nodes = None
            self.next_node = None
        self.distance = float('inf')
        self.path = ()
        self.edge_colors()
    
    def step_bruteforce(self):
        if self.algorithm == 1:
            self.algorithm = 0
            self.reset()
        if len(self.paths) > 0:
            # Remove um caminho da lista de caminhos
            path = self.paths.pop()
            dist = 0
            # Itera sobre os pares de vértices do caminho, calculando a distância
            for index in range(len(path)):
                nexti = index+1 if index < len(path)-1 else 0
                dist += self.graph[path[index]][path[nexti]]['weight']
            if dist < self.distance:
                self.distance = dist
                self.path = path + (path[0],)
            self.edge_colors(step_path=path)
            return True
        else:
            self.edge_colors()
            return False

    def step_nearest(self):
        if self.algorithm == 0:
            self.algorithm = 1 
            self.reset()
        if self.next_node is not None:
            min_node = None
            min_dist = float('inf')
            # Itera sobre os nós restantes do conjunto
            for node in self.disp_nodes:
                dist = self.graph[self.next_node][node]['weight']
                if dist < min_dist:
                    min_node = node
                    min_dist = dist
            self.path += (self.next_node,)
            self.next_node = min_node
            if self.next_node is not None:
                index = self.disp_nodes.index(self.next_node)
                self.disp_nodes.pop(index)
            self.edge_colors()
            return True
        else:
            if self.path[0] != self.path[-1]:
                self.path += (self.path[0],)
                self.edge_colors()
                return True
            else:
                self.edge_colors()
                return False
