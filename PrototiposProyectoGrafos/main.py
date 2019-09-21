from mainWindowGUI import *
from Graph import *
from embeddedimageGUI import *
from RouteTable import *
from PyQt5 import uic



class EnbeddedImageWindow(QtWidgets.QMainWindow,Ui_ImageWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.center()

    # Este metodo centra la ventana

    def center(self):
        frame = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

class RouteTable(QtWidgets.QMainWindow,Ui_ImageWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self) 
        self.setWindowTitle("Route Table")
        self.setMaximumSize(16777215,16777215)
        self.setMinimumSize(16777215,16777215)

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.center()
        self.makeGraphButton.clicked.connect(self.buildGraph)
        self.openFileButton.clicked.connect(self.openAFile)
        self.windowImage = EnbeddedImageWindow()
        self.makeTableButton.clicked.connect( self.buildTable)

    # Este metodo centra la ventana

    def center(self):
        frame = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

    def openAFile(self):
        explorer = QtWidgets.QFileDialog()
        currentDir = explorer.directory().canonicalPath()
        name, typefilter = explorer.getOpenFileName(None, "Open File", currentDir, "Text (*.txt)")
        if name:
            file = open(name)
            content = file.read()
            file.close()
            self.editor.setText(content)

    def buildGraph(self):
        graph = Graph()
        graph.buildGraph(self.editor.toPlainText())
        graph.makeGraph()
        self.showGraph()

    def showGraph(self):
        self.windowImage.setStyleSheet("background-image: url(%s)" % "graph.png")
        self.windowImage.show()

    def getRouteInTerminal(self):
        graph = Graph()
        graph.buildGraph(self.editor.toPlainText())
        x = self.initialServer.text()
        y = self.finalServer.text()
        if(x != "" and y != ""):
            roads = graph.getRoads(x,y)
            if(roads):
                s = graph.getWeigthOfRoads(roads)
                for k,v in s.items():
                    print("Ruta: %s, Peso: %s" % (roads[k],v))
                print("-"*50)

    def buildTable(self):
        uic.loadUi("RouteTable.ui, self")
        content = []
        graph = Graph()
        graph.buildGraph(self.editor.toPlainText())
        x = self.initialServer.text()
        y = self.finalServer.text()
        roads = graph.getRoads(x,y)
        if roads:
            roadWeigth = graph.getWeigthOfRoads(roads)

            invertedRoadWeigth = dict((v, k) for k, v in roadWeigth.items())

            sortedWeigths = list(invertedRoadWeigth.keys())
            sortedWeigths.sort()

            content.append("-"*50)
            content.append("Tabla de rutas de %s a %s" %(x,y))
            content.append("-"*50)
            content.append("Peso|ruta")
            for i in sortedWeigths:
                content.append("-" * 50)
                content.append("%s|%s" % (i,roads[invertedRoadWeigth[i]]))

            print("\n".join(content))

if __name__=="__main__":
    apt = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    apt.exec_()
