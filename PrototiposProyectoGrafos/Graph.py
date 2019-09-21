from LinkedList import LinkedList
from Vertex import Vertex
from Attribute import Attribute
import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self):
        self.vertices = LinkedList()
        self.graph = {}
    
    def addVertex(self,nameVertex):
        self.vertices.add(Vertex(nameVertex))

    def addEdge(self,nameVertexOrigin,nameVertexDestination,attribute = Attribute()):
        vertexOrigin = self.vertices.search(nameVertexOrigin)
        vertexOrigin.setEdge(nameVertexDestination,attribute)

    def connectedVertices(self,x):
        s = {}
        vertex_x = self.vertices.search(x)
        for edge in vertex_x.edges:
            s["%s" % edge.name] = "%s" % edge.weight
        for vertex in self.vertices:
            if(vertex.edges.alreadyExist(vertex_x)):
                for edge in vertex.edges:
                    if(edge.name == x):
                        s["%s" % vertex.name] = "%s" % edge.weight
        return s
    def connectedVerticesOfX(self,x):
        s = {}
        vertex_x = self.vertices.search(x)
        for edge in vertex_x.edges:
            s["%s" % edge.name] = "%s" % edge.weight
        return s
   
    def getGraph(self):
        for vertex in self.vertices:
            self.graph[vertex.name] = self.connectedVerticesOfX(vertex.name)
        
        return self.graph

    def makeGraph(self):
        G = nx.DiGraph()
        
        self.graph = self.getGraph()
        for v,edges in self.graph.items():
            G.add_node("%s" % (v))
            if(edges):
                for e,w in edges.items():
                    G.add_edge("%s" % v,"%s" % e,weight=w)
        
        edge_labels=dict([((u,v,),d['weight'])
                      for u,v,d in G.edges(data=True)])
        
        pos=nx.circular_layout(G)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,edge_color = 'b',
        arrowsize=20, arrowstyle='fancy',font_color="red")

        nx.draw(G,pos,with_labels = True, node_size=500)
        plt.savefig("graph.png")
        plt.close()

    def buildGraph(self,txtPlain):
        #self.graph = {}
        #self.vertices = LinkedList()
        content = iter(txtPlain.split("\n"))
        lastVertex = ""
        destVertex = ""
        for line in content:
            if(line == ""): break
            if line.count("\t") == 0:
                self.addVertex(line.lstrip("\t"))
                lastVertex = line.lstrip("\t")
            if line.count("\t") == 1:
                destVertex = line.lstrip("\t")
                prop = []
                for _ in range(5):
                    value = next(content).lstrip("\t")
                    prop.append(value.split(":"))
                    print(prop)
                attribute = Attribute(prop[0][1],prop[1][1],prop[2][1],prop[3][1],prop[4][1])
                print(prop)
                self.addEdge(lastVertex,destVertex,attribute) 

    #con derecho de autor 
'''
    def findPaths(self, graph, vertex, destination, path = [], visited = []):
        #Agrego el vertice actual a la ruta y lo marco como visitado(para evitar ciclos)
        visited.append(vertex)
        path.append(vertex)

        #Si el vertice actual es mi destino, imprimo la ruta seguida
        if (vertex == destination):
            print(path)

        #Si no es el destino, se iteran las aristas del vertice actual
        else:
            for edge in graph[vertex]:
                #Si la arista actual no se encuentra en los visitados, se llama recursivamente la función 
                #para seguir avanzando
                if(not edge in visited):
                    self.findPaths(graph, edge, destination, path, visited)

        #Luego de encontrar el destino, se retrocede un paso para poder buscar mas posibles caminos
        path.pop()
        visited.pop()
    '''
'''
        currentVertex,s = self.vertices,{}
        current = currentVertex.first
        while(current):
            
            if(current.value.name == x):
                edge = current.value.edges
                current_edge = edge.first
                while(current_edge):
                    s["%s" % current_edge.value.name] = None
                    current_edge = current_edge.next
            
            if(current.value.edges.alreadyExist(vertex_x)):
                s["%s" % current.value.name] = None
            current = current.next
        return list(s.keys())
      
x = "A"
g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addEdge("A","C",Attribute(2))
g.addEdge("A","C",Attribute(1))
g.addEdge("A","B",Attribute(3))
g.addEdge("B","D",Attribute(4))
g.addEdge("D","A",Attribute(5))
g.addEdge("E","B",Attribute(6))

print(g.vertices)
print(g.vertices.first.value.edges)
#print(g.connectedVertices("A"))
print("Las rutas de %s son  %s" % (x,g.connectedVertices(x)) ) 
print(g.getGraph())
g.showGraph()
'''