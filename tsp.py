import networkx as nx

import random

from itertools import permutations

class TSP():
    def __init__(self):
        self.graph = None
        self.pos = None
        self.paths = None
        self.distance = float('inf')
        self.path = None

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

    def edge_colors(self, step_path=None):
        if self.graph is not None:
            nx.set_edge_attributes(self.graph, 'black', 'color')
            if self.path is not None:
                for index in range(len(self.path)):
                    nexti = index+1 if index < len(self.path)-1 else 0
                    self.graph[self.path[index]][self.path[nexti]]['color'] = 'green'
            if step_path is not None:
                for index in range(len(step_path)):
                    nexti = index+1 if index < len(step_path)-1 else 0
                    self.graph[step_path[index]][step_path[nexti]]['color'] = 'red'

    def reset(self):
        # Reseta os caminhos, distância mínima e caminho ótimo do grafo
        if self.graph is not None:
            self.paths = list(permutations(self.graph.nodes()))
        else:
            self.paths = None
        self.distance = float('inf')
        self.path = None
        self.edge_colors()
    
    def step_bruteforce(self):
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
                self.path = path
            self.edge_colors(step_path=path)
            return True
        else:
            self.edge_colors()
            return False
