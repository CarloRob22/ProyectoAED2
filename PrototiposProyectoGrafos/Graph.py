from LinkedList import LinkedList
from Vertex import Vertex
from Attribute import Attribute
import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self): 
        self.vertices = LinkedList()
        self.graph = {}

    '''Agrega vertices a la lista de la instancia grafo'''
    def addVertex(self,nameVertex): 
        self.vertices.add(Vertex(nameVertex))

    '''Agregar aristas entre dos vertices y un atributo que servira para calcular el peso'''
    def addEdge(self,nameVertexOrigin,nameVertexDestination,attribute = Attribute()):                                                                                    
        vertexOrigin = self.vertices.search(nameVertexOrigin) #Obtener el vertice origen de la lista 
        vertexOrigin.setEdge(nameVertexDestination,attribute) #Al vertice origen se le agregara una arrista

    '''Retorna un Dict de los vertices con direccion a X y las aristas de X(Con su respectivo peso)'''
    def connectedVertices(self,x):
        s = {}
        vertex_x = self.vertices.search(x)  #obtenet el vertice x en la listaEnlazada
        
        #Almacena las aristas de X
        for edge in vertex_x.edges:     
            s["%s" % edge.name] = "%s" % edge.weight    #en el dict creado agrega un key(el vertice a que apunta x) con el valor de su peso
        
        #Almacena los vertices con direccion a X
        for vertex in self.vertices:    #iterar todos los vertices del grafo
            if(vertex.edges.alreadyExist(vertex_x)): #buscar si dentro del vertice actual se encuentra X
                for edge in vertex.edges:   #Debido a que existe se iteran las aristas del vertice actual
                    if(edge.name == x):     #buscar cual arista es el que apunta a x
                        s["%s" % vertex.name] = "%s" % edge.weight  #Agregar un key con el vertice actual y su nombre
        return s

    '''Retorna un Dict de las aristas de X'''
    def connectedVerticesOfX(self,x):
        s = {}
        #Almacena las aristas de X(mismo  proceso anterior)
        vertex_x = self.vertices.search(x)
        for edge in vertex_x.edges:
            s["%s" % edge.name] = "%s" % edge.weight
        return s
   
    '''Crea un grafo con forma de Dict con la actual instancia de la listaEnlazada'''
    def getGraph(self):
        for vertex in self.vertices: #iterar todos los vertices de la listaEnlazada
            self.graph[vertex.name] = self.connectedVerticesOfX(vertex.name) #crea Dict del nombre del vertice con sus aristas y peso 
        
        return self.graph

    '''Crea un objeto grafico del grafo y lo convierte como una imagen'''
    def makeGraph(self):
        G = nx.DiGraph()   
        
        self.graph = self.getGraph() #convierte el grafo de la ListaEnlazada del objeto a un Dict para facilitar su uso
        
        for v,edges in self.graph.items():
            G.add_node("%s" % (v))      #Agrega el vertice actual a la grafica
            if(edges):  
                for e,w in edges.items(): #e:vertice al que se apunta, w:peso de la arista
                    G.add_edge("%s" % v,"%s" % e,weight=w)  
        
        edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)]) #De algun modo hace que el peso de la imagen se vea bien        
        pos=nx.circular_layout(G)#Hace que los vertices se coloquen de manera circular
        
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,edge_color = 'b',
        arrowsize=20, arrowstyle='fancy',font_color="red") #personalizar caracteristicas de las aristas de grafica

        nx.draw(G,pos,with_labels = True, node_size=500)#personalizar caracteristicas de la grafica
        plt.savefig("graph.png")#Crea una imagen de la grafica y la convierte en un archivo png
        plt.close()

    '''Del contenido de un texto Plano va creando el grafo dentrod de la lista enlazada'''
    def buildGraph(self,txtPlain):
        
        #se crea una lista del contenido separado por salto de linea y se hace iterable(para hacer uso del next())
        content = iter(txtPlain.split("\n"))    
        lastVertex = ""
        destVertex = ""
        for line in content:
            if(line == ""): break
            if line.count("\t") == 0:   #En caso de ser un vertice
                self.addVertex(line.lstrip("\t")) #Agrega Vertice a la lista enlazada del grafo
                lastVertex = line.lstrip("\t")
            if line.count("\t") == 1:   #En caso de ser un vertice al que apunta el ultimo vertice
                destVertex = line.lstrip("\t")
                prop = []
                for _ in range(5): #Guarda los sigueinte 5 lineas en un arreglo y las separa por ":"
                    value = next(content).lstrip("\t") 
                    prop.append(value.split(":"))
                attribute = Attribute(prop[0][1],prop[1][1],prop[2][1],prop[3][1],prop[4][1]) #crea los atributos de la arista
                self.addEdge(lastVertex,destVertex,attribute) #Agrega la arista a la lista enlazada del ultimo vertice
