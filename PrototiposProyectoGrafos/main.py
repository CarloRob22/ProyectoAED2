from mainWindowGUI import *
from Graph import *
from embeddedimageGUI import *



class EnbeddedImageWindow(QtWidgets.QMainWindow,Ui_ImageWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.makeGraphButton.clicked.connect(self.buildGraph)
        self.openFileButton.clicked.connect(self.openAFile)
        self.windowImage = EnbeddedImageWindow()
        self.makeTableButton.clicked.connect( self.getRouteInTerminal)

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
            graph.getRoads(x,y)

if __name__=="__main__":
    apt = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    apt.exec_()
