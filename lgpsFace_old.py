# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test4.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 586)
        MainWindow.setStyleSheet("background-color: rgb(170, 0, 127);\n"
"color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 60, 361, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 510, 461, 23))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 461, 61))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"\n"
"color: rgb(255, 255, 127);")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 201, 31))
        self.label_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 127);")
        self.label_5.setObjectName("label_5")
        self.importfile = QtWidgets.QLineEdit(self.centralwidget)
        self.importfile.setGeometry(QtCore.QRect(250, 270, 211, 20))
        self.importfile.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.importfile.setObjectName("importfile")
        self.cor_lan = QtWidgets.QLabel(self.centralwidget)
        self.cor_lan.setGeometry(QtCore.QRect(10, 220, 201, 20))
        self.cor_lan.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.cor_lan.setObjectName("cor_lan")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(470, 270, 71, 21))
        self.toolButton.setStyleSheet("color: rgb(255, 0, 255);\n"
"background-color: rgb(206, 206, 206);")
        self.toolButton.setObjectName("toolButton")
        self.lon_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lon_2.setGeometry(QtCore.QRect(390, 190, 113, 20))
        self.lon_2.setStyleSheet("color: rgb(255, 255, 127);")
        self.lon_2.setObjectName("lon_2")
        self.lat_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lat_1.setGeometry(QtCore.QRect(250, 220, 113, 20))
        self.lat_1.setStyleSheet("color: rgb(255, 255, 127);")
        self.lat_1.setObjectName("lat_1")
        self.cor_lon = QtWidgets.QLabel(self.centralwidget)
        self.cor_lon.setGeometry(QtCore.QRect(10, 190, 211, 20))
        self.cor_lon.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.cor_lon.setObjectName("cor_lon")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 90, 401, 41))
        self.label_3.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 127);")
        self.label_3.setObjectName("label_3")
        self.lat_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lat_2.setGeometry(QtCore.QRect(390, 220, 113, 20))
        self.lat_2.setStyleSheet("color: rgb(255, 255, 127);")
        self.lat_2.setObjectName("lat_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 510, 101, 31))
        self.pushButton.setStyleSheet("background-color: rgb(249, 249, 249);\n"
"color: rgb(255, 255, 127);\n"
"color: rgb(255, 2, 243);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lon_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lon_1.setGeometry(QtCore.QRect(250, 190, 113, 20))
        self.lon_1.setStyleSheet("color: rgb(255, 255, 127);")
        self.lon_1.setObjectName("lon_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 121, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("lgps_ico.png"))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 310, 141, 16))
        self.label_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.importfile_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.importfile_2.setGeometry(QtCore.QRect(250, 300, 211, 20))
        self.importfile_2.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.importfile_2.setObjectName("importfile_2")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(470, 300, 71, 21))
        self.toolButton_2.setStyleSheet("color: rgb(255, 0, 255);\n"
"background-color: rgb(206, 206, 206);")
        self.toolButton_2.setObjectName("toolButton_2")
        self.cor_lan_2 = QtWidgets.QLabel(self.centralwidget)
        self.cor_lan_2.setGeometry(QtCore.QRect(10, 420, 181, 20))
        self.cor_lan_2.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.cor_lan_2.setObjectName("cor_lan_2")
        self.cor_lon_2 = QtWidgets.QLabel(self.centralwidget)
        self.cor_lon_2.setGeometry(QtCore.QRect(10, 360, 191, 20))
        self.cor_lon_2.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.cor_lon_2.setObjectName("cor_lon_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(250, 360, 61, 21))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(250, 390, 61, 21))
        self.spinBox_2.setObjectName("spinBox_2")
        self.cor_lon_3 = QtWidgets.QLabel(self.centralwidget)
        self.cor_lon_3.setGeometry(QtCore.QRect(10, 390, 191, 20))
        self.cor_lon_3.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.cor_lon_3.setObjectName("cor_lon_3")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(250, 420, 61, 21))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(250, 450, 61, 21))
        self.spinBox_4.setObjectName("spinBox_4")
        self.cor_lan_3 = QtWidgets.QLabel(self.centralwidget)
        self.cor_lan_3.setGeometry(QtCore.QRect(10, 450, 181, 20))
        self.cor_lan_3.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.cor_lan_3.setObjectName("cor_lan_3")
        self.spinBox_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(540, 370, 61, 21))
        self.spinBox_5.setObjectName("spinBox_5")
        self.cor_lon_4 = QtWidgets.QLabel(self.centralwidget)
        self.cor_lon_4.setGeometry(QtCore.QRect(340, 370, 191, 20))
        self.cor_lon_4.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.cor_lon_4.setObjectName("cor_lon_4")
        self.cor_lan_4 = QtWidgets.QLabel(self.centralwidget)
        self.cor_lan_4.setGeometry(QtCore.QRect(340, 430, 181, 20))
        self.cor_lan_4.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.cor_lan_4.setObjectName("cor_lan_4")
        self.spinBox_6 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_6.setGeometry(QtCore.QRect(540, 420, 61, 21))
        self.spinBox_6.setObjectName("spinBox_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 21))
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
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", " движений   земной коры методами"))
        self.label.setText(_translate("MainWindow", "Лаборатория изучения современных"))
        self.label_5.setText(_translate("MainWindow", "Файлы временных рядов .pos"))
        self.cor_lan.setText(_translate("MainWindow", "Ограничение по координатам lat"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.cor_lon.setText(_translate("MainWindow", "Ограничение по координатам lon"))
        self.label_3.setText(_translate("MainWindow", " космической геодезии (ЛGPS)"))
        self.pushButton.setText(_translate("MainWindow", "Старт"))
        self.label_6.setText(_translate("MainWindow", "Фаил скоростей"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.cor_lan_2.setText(_translate("MainWindow", "Ограничение по скорости E"))
        self.cor_lon_2.setText(_translate("MainWindow", "Ограничение по ошибке  E_err  "))
        self.cor_lon_3.setText(_translate("MainWindow", "Ограничение по ошибке   N_err "))
        self.cor_lan_3.setText(_translate("MainWindow", "Ограничение по скорости N "))
        self.cor_lon_4.setText(_translate("MainWindow", "Ограничение по ошибке  H_err  "))
        self.cor_lan_4.setText(_translate("MainWindow", "Ограничение по скорости H"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Помощь"))
        self.action.setText(_translate("MainWindow", "Открыть"))
        self.action_2.setText(_translate("MainWindow", "Экспорт"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())