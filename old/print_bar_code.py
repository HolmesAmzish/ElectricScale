# -*- coding: utf-8 -*-

# Form implementation generated from reading view file 'print_bar_code.view'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_print(object):
    def setupUi(self, MainWindow_print):
        MainWindow_print.setObjectName("MainWindow_print")
        MainWindow_print.resize(434, 529)
        self.centralwidget = QtWidgets.QWidget(MainWindow_print)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_print_ok = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_print_ok.setGeometry(QtCore.QRect(130, 440, 161, 61))
        self.pushButton_print_ok.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_print_ok.setObjectName("pushButton_print_ok")
        self.label_showbarcode = QtWidgets.QLabel(self.centralwidget)
        self.label_showbarcode.setGeometry(QtCore.QRect(60, 340, 311, 81))
        self.label_showbarcode.setText("")
        self.label_showbarcode.setObjectName("label_showbarcode")
        self.tableWidget_view = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_view.setGeometry(QtCore.QRect(90, 30, 261, 271))
        self.tableWidget_view.setObjectName("tableWidget_view")
        self.tableWidget_view.setColumnCount(1)
        self.tableWidget_view.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_view.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_view.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_view.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_view.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_view.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_view.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        item.setBackground(QtGui.QColor(208, 255, 253))
        self.tableWidget_view.setHorizontalHeaderItem(0, item)
        self.tableWidget_view.horizontalHeader().setDefaultSectionSize(160)
        MainWindow_print.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_print)
        self.statusbar.setObjectName("statusbar")
        MainWindow_print.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_print)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_print)

    def retranslateUi(self, MainWindow_print):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_print.setWindowTitle(_translate("MainWindow_print", "打印条形码"))
        self.pushButton_print_ok.setText(_translate("MainWindow_print", "打印完成"))
        item = self.tableWidget_view.verticalHeaderItem(0)
        item.setText(_translate("MainWindow_print", "类别"))
        item = self.tableWidget_view.verticalHeaderItem(1)
        item.setText(_translate("MainWindow_print", "名称"))
        item = self.tableWidget_view.verticalHeaderItem(2)
        item.setText(_translate("MainWindow_print", "重量(g)"))
        item = self.tableWidget_view.verticalHeaderItem(3)
        item.setText(_translate("MainWindow_print", "单价(元/kg)"))
        item = self.tableWidget_view.verticalHeaderItem(4)
        item.setText(_translate("MainWindow_print", "总价(元)"))
        item = self.tableWidget_view.verticalHeaderItem(5)
        item.setText(_translate("MainWindow_print", "包装日期"))

