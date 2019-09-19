# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(398, 217)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 40, 121, 17))
        self.label.setObjectName("label")
        self.openFileLogin = QtWidgets.QPushButton(self.centralwidget)
        self.openFileLogin.setGeometry(QtCore.QRect(80, 110, 89, 25))
        self.openFileLogin.setObjectName("openFileLogin")
        self.newFileLogin = QtWidgets.QPushButton(self.centralwidget)
        self.newFileLogin.setGeometry(QtCore.QRect(220, 110, 89, 25))
        self.newFileLogin.setObjectName("newFileLogin")
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.label.setText(_translate("Login", "Network analysis "))
        self.openFileLogin.setText(_translate("Login", "Open File"))
        self.newFileLogin.setText(_translate("Login", "New File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
