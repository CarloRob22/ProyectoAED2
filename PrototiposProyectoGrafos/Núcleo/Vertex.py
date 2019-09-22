# -*- coding: utf-8 -*-
from Núcleo.LinkedList import LinkedList
from Núcleo.Edge import Edge

class Vertex:
    def __init__(self,name):
        self.name = name
        self.edges = LinkedList()
    
    def setEdge(self,vertex,characteristic):
        self.edges.add(Edge(vertex,characteristic)) 