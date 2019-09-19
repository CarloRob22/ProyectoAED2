from form import *
from Graph import *

class MainWindow(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openFile)
        self.graph = Graph()
        self.content = ""

    def openFile(self):
        explorer = QtWidgets.QFileDialog()
        directory = explorer.directory().canonicalPath()
        print(directory)
        name,typeFile = explorer.getOpenFileName(self,"Open File",directory,"Texto(*.txt)")
        file = open(name,"r")
        self.content = file.read()
        file.close()
        self.textEdit.append(self.content)
        self.createGraph()

    def createGraph(self):
        content = self.content.split("\n")
        for i in range(len(content)-1):
            if content[i].count("\t") == 0:
                self.graph.addVertex(content[i].lstrip("\t"))
            if content[i+1].count("\t") == content[i].count("\t")+1:
                for j in range(i+1,len(content)-1):
                    self.graph.addEdge(content[i].lstrip("\t"),content[j].lstrip("\t"))
                    if content[j+1].count("\t") == content[i].count("\t"):
                        break
        self.graph.showDraw()
if __name__=="__main__":
    apt = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    apt.exec_()