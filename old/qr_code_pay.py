# -*- coding: utf-8 -*-

# Form implementation generated from reading view file 'qr_code_pay.view'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_pay(object):
    def setupUi(self, MainWindow_pay):
        MainWindow_pay.setObjectName("MainWindow_pay")
        MainWindow_pay.resize(430, 522)
        self.centralwidget = QtWidgets.QWidget(MainWindow_pay)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_pay_ok = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pay_ok.setGeometry(QtCore.QRect(110, 420, 211, 71))
        self.pushButton_pay_ok.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_pay_ok.setObjectName("pushButton_pay_ok")
        self.label_showqrcode = QtWidgets.QLabel(self.centralwidget)
        self.label_showqrcode.setGeometry(QtCore.QRect(160, 300, 111, 101))
        self.label_showqrcode.setText("")
        self.label_showqrcode.setObjectName("label_showqrcode")
        self.tableWidget_view_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_view_2.setGeometry(QtCore.QRect(90, 10, 271, 271))
        self.tableWidget_view_2.setObjectName("tableWidget_view_2")
        self.tableWidget_view_2.setColumnCount(1)
        self.tableWidget_view_2.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_view_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_view_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_view_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_view_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_view_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_view_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_view_2.setHorizontalHeaderItem(0, item)
        self.tableWidget_view_2.horizontalHeader().setDefaultSectionSize(160)
        MainWindow_pay.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_pay)
        self.statusbar.setObjectName("statusbar")
        MainWindow_pay.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_pay)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_pay)

    def retranslateUi(self, MainWindow_pay):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_pay.setWindowTitle(_translate("MainWindow_pay", "二维码付款"))
        self.pushButton_pay_ok.setText(_translate("MainWindow_pay", "付款成功"))
        item = self.tableWidget_view_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow_pay", "类别"))
        item = self.tableWidget_view_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow_pay", "名称"))
        item = self.tableWidget_view_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow_pay", "重量(g)"))
        item = self.tableWidget_view_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow_pay", "单价(元/kg)"))
        item = self.tableWidget_view_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow_pay", "总价(元)"))
        item = self.tableWidget_view_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow_pay", "包装日期"))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        item.setFont(font)
        item.setBackground(QtGui.QColor(208, 255, 253))

