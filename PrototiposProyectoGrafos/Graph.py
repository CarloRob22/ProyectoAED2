import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.json = {}
        self.fig = nx.Graph()

    def __str__(self):
        return str(self.json)

    def addVertex(self, name):
        if name not in self.json.keys():
            self.json[name] = []

    def addEdge(self, vertex1, vertex2):
        self.addVertex(vertex1)
        self.addVertex(vertex2)
        if vertex2 not in self.json[vertex1]:
            self.json[vertex1].append(vertex2)
        if vertex1 not in self.json[vertex2]:
            self.json[vertex2].append(vertex1)

    def buildGraph(self,content):
        content = content.split("\n")
        for i in range(len(content) - 1):
            if content[i].count("\t") == 0:
                self.addVertex(content[i].lstrip("\t"))
            if content[i + 1].count("\t") == content[i].count("\t") + 1:
                for j in range(i + 1, len(content) - 1):
                    self.addEdge(content[i].lstrip("\t"), content[j].lstrip("\t"))
                    if content[j + 1].count("\t") == content[i].count("\t"):
                        break

    def showDraw(self):
        for vertice, aristas in self.json.items():
            self.fig.add_node("%s" % vertice)
            for arista in aristas:
                self.fig.add_node("%s" % arista)
                self.fig.add_edge("%s" % vertice, "%s" % arista, weight=1)
        position = nx.spring_layout(self.fig)
        labels={(vertex1,vertex2): weigth["weight"] for vertex1,vertex2,weigth in self.fig.edges(data=True)}
        nx.draw(self.fig,position, with_labels=True)
        nx.draw_networkx_edge_labels(self.fig,position,edge_labels=labels,font_color="red")
        plt.show()