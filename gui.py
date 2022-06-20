# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1315, 783)
        MainWindow.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cpu_frame = QtWidgets.QFrame(self.centralwidget)
        self.cpu_frame.setGeometry(QtCore.QRect(170, 40, 360, 411))
        self.cpu_frame.setAutoFillBackground(False)
        self.cpu_frame.setStyleSheet("border-width:2px;\n"
"border-color: rgb(0, 243, 255);\n"
"border-style:inset;\n"
"")
        self.cpu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cpu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cpu_frame.setObjectName("cpu_frame")
        self.cpu_label = QtWidgets.QLabel(self.cpu_frame)
        self.cpu_label.setGeometry(QtCore.QRect(130, 10, 100, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.cpu_label.setFont(font)
        self.cpu_label.setStyleSheet("color: rgb(0, 243, 255);\n"
"border-width: 0px;")
        self.cpu_label.setObjectName("cpu_label")
        self.label = QtWidgets.QLabel(self.cpu_frame)
        self.label.setGeometry(QtCore.QRect(30, 70, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 243, 255);\n"
"border-width:0px")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hardware Monitor"))
        self.cpu_label.setText(_translate("MainWindow", "CPU"))
        self.label.setText(_translate("MainWindow", "Usage: 0%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())