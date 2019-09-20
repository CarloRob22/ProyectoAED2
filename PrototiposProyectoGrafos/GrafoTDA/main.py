from mainwindow import *
from login import *
from Graph import *


class mainwindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.editor.textChanged.connect(self.enabledButtons)
        self.fileName = None
        self.save.clicked.connect(self.saveFile)
        self.saveAs.clicked.connect(self.saveAsFile)
        self.makeGraph.clicked.connect(self.buildGraph)
        self.openFile.clicked.connect(self.openAFile)

    def openAFile(self):
        explorer = QtWidgets.QFileDialog()
        currentDir = explorer.directory().canonicalPath()
        name, typefilter = explorer.getOpenFileName(None, "Open File", currentDir, "Text (*.txt)")
        file = open(name)
        content = file.read()
        file.close()
        self.editor.setText(content)
        self.disableButtons()

    def buildGraph(self):
        graph = Graph()
        graph.buildGraph(self.editor.toPlainText())
        graph.showGraph()

    def saveAsFile(self):
        filename,_ = QtWidgets.QFileDialog.getSaveFileName(None,"Save As","","Text(*.txt)")
        content = self.editor.toPlainText()
        file = open(filename,"w")
        file.write(content)
        file.close()
        self.fileName = filename
        self.disableButtons()

    def saveFile(self):
        content = self.editor.toPlainText()
        file = open(self.fileName,"w")
        file.write(content)
        file.close()
        self.disableButtons()

    def enabledButtons(self):
        if self.fileName:
            self.save.setEnabled(True)
        self.saveAs.setEnabled(True)

    def disableButtons(self):
        self.save.setEnabled(False)
        self.saveAs.setEnabled(False)

class MainWindow(QtWidgets.QMainWindow,Ui_Login):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.openFileLogin.clicked.connect(self.loginOpenFile)
        self.mainWindow = mainwindow()
        self.newFileLogin.clicked.connect(self.loginNewFile)

    def loginNewFile(self):
        self.hide()
        self.mainWindow.show()
        self.mainWindow.save.setEnabled(False)
        self.mainWindow.saveAs.setEnabled(False)

    def loginOpenFile(self):
        self.hide()
        explorer = QtWidgets.QFileDialog()
        currentDir = explorer.directory().canonicalPath()
        name,typefilter = explorer.getOpenFileName(None,"Open File",currentDir,"Text (*.txt)")
        file = open(name)
        content = file.read()
        file.close()
        self.mainWindow.editor.setText(content)
        self.mainWindow.fileName=name
        self.mainWindow.save.setEnabled(False)
        self.mainWindow.saveAs.setEnabled(False)
        self.showMain()

    def showMain(self):
        self.hide()
        self.mainWindow.show()

if __name__=="__main__":
    apt = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    apt.exec_()