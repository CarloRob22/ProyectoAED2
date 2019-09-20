# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1007, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.editor = QtWidgets.QTextEdit(self.centralwidget)
        self.editor.setGeometry(QtCore.QRect(80, 10, 611, 501))
        self.editor.setObjectName("editor")
        self.originNode = QtWidgets.QLineEdit(self.centralwidget)
        self.originNode.setGeometry(QtCore.QRect(740, 50, 151, 41))
        self.originNode.setObjectName("originNode")
        self.endNode = QtWidgets.QLineEdit(self.centralwidget)
        self.endNode.setGeometry(QtCore.QRect(740, 120, 151, 41))
        self.endNode.setObjectName("endNode")
        self.makeTable = QtWidgets.QPushButton(self.centralwidget)
        self.makeTable.setGeometry(QtCore.QRect(770, 210, 89, 25))
        self.makeTable.setObjectName("makeTable")
        self.makeGraph = QtWidgets.QPushButton(self.centralwidget)
        self.makeGraph.setGeometry(QtCore.QRect(770, 270, 89, 25))
        self.makeGraph.setObjectName("makeGraph")
        self.openFile = QtWidgets.QPushButton(self.centralwidget)
        self.openFile.setGeometry(QtCore.QRect(140, 540, 111, 31))
        self.openFile.setObjectName("openFile")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(330, 540, 101, 31))
        self.save.setObjectName("save")
        self.saveAs = QtWidgets.QPushButton(self.centralwidget)
        self.saveAs.setGeometry(QtCore.QRect(500, 540, 111, 31))
        self.saveAs.setObjectName("saveAs")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(910, 60, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(910, 130, 67, 17))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.makeTable.setText(_translate("MainWindow", "Make Table"))
        self.makeGraph.setText(_translate("MainWindow", "Make Graph"))
        self.openFile.setText(_translate("MainWindow", "Open New File"))
        self.save.setText(_translate("MainWindow", "save"))
        self.saveAs.setText(_translate("MainWindow", "save as"))
        self.label.setText(_translate("MainWindow", "Origin"))
        self.label_2.setText(_translate("MainWindow", "End"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
