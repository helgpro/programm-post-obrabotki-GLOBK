# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 456)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"background-color: rgb(170, 0, 127);")
        MainWindow.setIconSize(QtCore.QSize(100, 100))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lon_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lon_1.setGeometry(QtCore.QRect(250, 160, 113, 20))
        self.lon_1.setStyleSheet("color: rgb(255, 255, 127);")
        self.lon_1.setObjectName("lon_1")
        self.lat_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lat_1.setGeometry(QtCore.QRect(250, 190, 113, 20))
        self.lat_1.setStyleSheet("color: rgb(255, 255, 127);")
        self.lat_1.setObjectName("lat_1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 0, 561, 61))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"\n"
"color: rgb(255, 255, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 121, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("lgps_ico.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 80, 401, 41))
        self.label_3.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 127);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 50, 361, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 410, 361, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.cor_lon = QtWidgets.QLabel(self.centralwidget)
        self.cor_lon.setGeometry(QtCore.QRect(10, 160, 211, 20))
        self.cor_lon.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.cor_lon.setObjectName("cor_lon")
        self.cor_lan = QtWidgets.QLabel(self.centralwidget)
        self.cor_lan.setGeometry(QtCore.QRect(10, 190, 201, 20))
        self.cor_lan.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.cor_lan.setObjectName("cor_lan")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(400, 240, 71, 21))
        self.toolButton.setStyleSheet("color: rgb(255, 0, 255);\n"
"background-color: rgb(206, 206, 206);")
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 400, 151, 31))
        self.pushButton.setStyleSheet("background-color: rgb(249, 249, 249);\n"
"color: rgb(255, 255, 127);\n"
"color: rgb(255, 2, 243);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"")

        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.label_5.setGeometry(QtCore.QRect(20, 230, 151, 31))
        self.label_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 127);")
        self.label_5.setObjectName("label_5")
        self.lon_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lon_2.setGeometry(QtCore.QRect(390, 160, 113, 20))
        self.lon_2.setStyleSheet("color: rgb(255, 255, 127);")
        self.lon_2.setObjectName("lon_2")
        self.lat_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lat_2.setGeometry(QtCore.QRect(390, 190, 113, 20))
        self.lat_2.setStyleSheet("color: rgb(255, 255, 127);")
        self.lat_2.setObjectName("lat_2")
        self.importfile = QtWidgets.QLineEdit(self.centralwidget)
        self.importfile.setGeometry(QtCore.QRect(172, 240, 211, 20))
        self.importfile.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.importfile.setObjectName("importfile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "postGLOBK"))
        self.label.setText(_translate("MainWindow", "Лаборатория изучения современных"))
        self.label_3.setText(_translate("MainWindow", " космической геодезии (ЛGPS)"))
        self.label_4.setText(_translate("MainWindow", " движений   земной коры методами"))
        self.cor_lon.setText(_translate("MainWindow", "Ограничение по координатам lon"))
        self.cor_lan.setText(_translate("MainWindow", "Ограничение по координатам lat"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Старт"))
        self.label_5.setText(_translate("MainWindow", "Имортировать фаил"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())