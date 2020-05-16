import numpy as np
import pygame as pg

class Graph(dict):

    graph = {}

    def __init__(self):
        self = dict()

    def add_vertex(self, key, edges=None):
        if edges is None:
            edges = []
        self[key]=edges

    def add_edge(self, key, edge=None):
        self[key].append(edge)

    def get_edges(self, key):
        return self[key]

    def show_vertex(self, vertex):
        edges = self[vertex]
        return str(vertex)+'->'+'->'.join(self[vertex])

    def get_matrix(self):
        keys = [key for key in self] #vertices
        keys.sort()
        n = len(keys) #number of vertices 
        matrix = np.zeros((n,n), dtype=int)
        for i in range(n):
            for j in range(n):
                matrix[i][j]=self.is_edge(keys[i],keys[j])
        print(matrix)

    def is_edge(self,v1,v2):
        if v2 in self.get(v1):
            return 1
        else:
            return 0

    def draw(self):
        pg.init()
        screen = pg.display.set_mode([500,500])
        pg.display.set_caption('Grapher')
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            screen.fill((30,33,39))
            pg.draw.circle(screen,(0,0,0),(250,250),75)
            pg.display.flip()
        pg.quit()

if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex('a', edges=['b','c'])
    graph.add_vertex('b', edges=['a','c'])
    graph.add_vertex('c', edges=['a','b'])
    graph.add_vertex('d')
    graph.add_edge('a','d')
    graph.add_edge('d','a')
    graph.add_vertex('e')
    graph.get_matrix()
    graph.draw()
