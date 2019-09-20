from embeddedimageGUI import *

class EnbeddedImageWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)


if __name__=="__main__":
    apt = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    apt.exec_()
