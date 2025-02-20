import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush

import get_labels
from home import *

from sys import argv, exit

import cv2
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from print_bar_code import *
from qr_code_pay import *
import barcode
from barcode.writer import ImageWriter
import time
import datetime
import qrcode
import weight


isCreate=False
isInput=False


class MyWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        desktop = QApplication.desktop()
        rect = desktop.frameSize()
        self.resize(QSize(rect.width(), rect.height()))
        self.timer_camera = None  # 定时器
        # self.timer_camera = QtCore.QTimer()  # 定时器
        self.cap = cv2.VideoCapture()  # 准备获取图像
        self.CAM_NUM = 0
        self.fruit_label=""
        self.setStyle(QStyleFactory.create("GTK+"))
        self.setStyleSheet('#centralwidget{border-image:url("./background1.jpg")}')
        self.tableWidget_kind.setStyleSheet('background-color: rgb(202, 235, 216);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.tableWidget.setStyleSheet('background-color: rgb(202, 235, 216);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.pushButton_reok.setStyleSheet('background-color: rgb(255, 99, 71);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.pushButton_pay.setStyleSheet('background-color: rgb(3, 168, 158);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.pushButton_print.setStyleSheet('background-color: rgb(210, 180, 140);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        # palette = QPalette()
        # palette.setBrush(QPalette.Background, QBrush(QPixmap("./background1.jpg")))
        # self.setPalette(palette)
        # self.setAutoFillBackground(True)
        self.slot_init()  # 设置槽函数
        # self.button_open_camera_click()
        # global mywin_t
        # t=weight.Hx711(mywindow=self.__class__)
        # t.start()
        # while True:
        #     n=send.startWeight()
        #     if (n is not None) and n > 2:
        #         self.camera_capture()
        #     else:
        #         pass


    def initTimer(self):
        self.timer_camera = QtCore.QTimer()
        self.timer_camera.timeout.connect(self.show_camera)

    def slot_init(self):
        # 设置槽函数
        # self.timer_camera = QtCore.QTimer()
        # self.timer_camera.timeout.connect(self.show_camera)
        # self.pushButton_open.clicked.connect(self.button_open_camera_click)

        # self.pushButton_close.clicked.connect(self.closeEvent)
        # self.pushButton_ok.clicked.connect(self.getDataInformation)
        self.pushButton_reok.clicked.connect(self.pushDataInformation)
        # self.pushButton_capture.clicked.connect(self.camera_capture)
        self.pushButton_print.clicked.connect(self.printBarCode)
        self.pushButton_pay.clicked.connect(self.QRcodePay)


    def getDataInformation(self):
        name_2=self.fruit_label
        sql="select * from info where (sort regexp '%s') or (name regexp '%s')"
        name_2="'"+name_2+"'"
        sql=sql.replace("'%s'",name_2)
        print(sql)
        try:
            cursor.execute(sql)
            data=cursor.fetchall()
            print(data)
            x=0
            for i in data:
                y=0
                for j in i:
                    self.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(data[x][y])))
                    y=y+1
                x=x+1
        except:
          print("Error:unable to fetch data")

    def init_t(self,t):
        self.t=t


    def pushDataInformation(self):
        weights = self.t.getWeight()
        while weights is None or weights<=0:
            weights = self.t.getWeight()

        print(weights)
        get_row=self.tableWidget.currentRow()
        name_1=self.tableWidget.item(get_row,1).text()
        sql="select * from info where name = '%s'"%(name_1)
        print(sql)
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            print(results)
            for row in results:
                sort=row[0]
                name_2=row[1]
                # weight=row[2]
                unit_price=row[2]
                # total_price=row[4]
                item1=QTableWidgetItem(sort)
                self.tableWidget_kind.setItem(0,0,item1)
                item2 = QTableWidgetItem(name_2)
                self.tableWidget_kind.setItem(1, 0, item2)
                item3 = QTableWidgetItem(str(weights))
                self.tableWidget_kind.setItem(2, 0, item3)
                item4 = QTableWidgetItem(str(unit_price))
                self.tableWidget_kind.setItem(3, 0, item4)
                item5 = QTableWidgetItem(str(unit_price/1000*weights))
                self.tableWidget_kind.setItem(4, 0, item5)
        except:
            print("Error:unable to fetch data")

    def createOrderId(self):
        global isCreate
        global num
        if isCreate is not True:
            millis = int(round(time.time() * 1000))
            num = str(millis)
            isCreate=True
            return num
        else:
            return num

    def printBarCode(self):
        self.ch=MyWindow_1()
        self.ch.OPEN()
        num=self.createOrderId()
        print(num)
        print(barcode.PROVIDED_BARCODES)
        EAN = barcode.get_barcode_class('code39')
        ean = EAN(num, writer=ImageWriter())
        fullname = ean.save('./barCodeImg/ean13_barcode')
        print(fullname)
        self.ch.label_showbarcode.setPixmap(QPixmap('./barCodeImg/ean13_barcode'))
        self.ch.label_showbarcode.setScaledContents(True)
        item1 = QTableWidgetItem(self.tableWidget_kind.item(0,0).text())
        self.ch.tableWidget_view.setItem(0, 0, item1)
        item2 = QTableWidgetItem(self.tableWidget_kind.item(1, 0).text())
        self.ch.tableWidget_view.setItem(1, 0, item2)
        item3 = QTableWidgetItem(str(self.tableWidget_kind.item(2, 0).text()))
        self.ch.tableWidget_view.setItem(2, 0, item3)
        item4 = QTableWidgetItem(str(self.tableWidget_kind.item(3, 0).text()))
        self.ch.tableWidget_view.setItem(3, 0, item4)
        item5 = QTableWidgetItem(str(self.tableWidget_kind.item(4, 0).text()))
        self.ch.tableWidget_view.setItem(4, 0, item5)
        now=datetime.datetime.now().strftime('%Y-%m-%d')
        item6 = QTableWidgetItem(now)
        self.ch.tableWidget_view.setItem(5, 0, item6)
        try:
            sql = "insert into orders(num, sort, name, weight, unit_price, total_price) values (%s, %s, %s, %s, %s, %s)"
            list_i=[num,item1.text(),item2.text(),float(item3.text()),float(item4.text()),float(item5.text())]
            cursor.execute(sql,list_i)
        except:
            print("Error:unable to insert data")

    def QRcodePay(self):
        self.ch1 = MyWindow_2()
        self.ch1.OPEN()
        num=self.createOrderId()
        qrcode.make(num).save('./barCodeImg/qrcode.png')
        self.ch1.label_showqrcode.setPixmap(QPixmap('./barCodeImg/qrcode.png'))
        self.ch1.label_showqrcode.setScaledContents(True)
        item1 = QTableWidgetItem(self.tableWidget_kind.item(0, 0).text())
        self.ch1.tableWidget_view_2.setItem(0, 0, item1)
        item2 = QTableWidgetItem(self.tableWidget_kind.item(1, 0).text())
        self.ch1.tableWidget_view_2.setItem(1, 0, item2)
        item3 = QTableWidgetItem(str(self.tableWidget_kind.item(2, 0).text()))
        self.ch1.tableWidget_view_2.setItem(2, 0, item3)
        item4 = QTableWidgetItem(str(self.tableWidget_kind.item(3, 0).text()))
        self.ch1.tableWidget_view_2.setItem(3, 0, item4)
        item5 = QTableWidgetItem(str(self.tableWidget_kind.item(4, 0).text()))
        self.ch1.tableWidget_view_2.setItem(4, 0, item5)
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        item6 = QTableWidgetItem(now)
        self.ch1.tableWidget_view_2.setItem(5, 0, item6)




    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(
                    self, u"Warning", u"请检测相机与电脑是否连接正确",
                    buttons=QtWidgets.QMessageBox.Ok,
                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)
                self.show_image()

    def show_image(self):
        flag, self.image = self.cap.read()  # 从视频流中读取图片
        image_show = cv2.resize(self.image, (1280, 720))  # 把读到的帧的大小重新设置为 600*360
        width, height = image_show.shape[:2]  # 行:宽，列:高
        image_show = cv2.cvtColor(image_show, cv2.COLOR_BGR2RGB)  # opencv读的通道是BGR,要转成RGB
        image_show = cv2.flip(image_show, 1)  # 水平翻转，因为摄像头拍的是镜像的。
        self.showImage = QtGui.QImage(image_show.data, height, width, QImage.Format_RGB888)





    def show_camera(self):
        flag, self.image = self.cap.read()

        self.image=cv2.flip(self.image, 1) # 左右翻转
        show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_face.setPixmap(QtGui.QPixmap.fromImage(showImage))
        self.label_face.setScaledContents(True)

    def camera_capture(self):
        if self.cap.isOpened():
            now_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
            fname ='images/pic_' + str(now_time) + '.png' #设置图片地址
            cv2.imwrite(fname, self.image) #保存图片
            cv2.putText(self.image, 'The picture have saved !',
                        (int(self.image.shape[1] / 2 - 130), int(self.image.shape[0] / 2)),
                        cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                        1.0, (255, 0, 0), 1)
            # self.timer_camera.stop()  # 停止计时
            print(fname)
            self.fruit_label=get_labels.getClass(fname) # 进行预测获取label
            #self.pushButton_name.setText(_translate("mainWindow", fruit_label))
            # self.timer_camera.start(30)
            self.show_image()
        else:
            QMessageBox.critical(self, '错误', '摄像头未打开！')
            return None



    def closeEvent(self):
        if self.timer_camera.isActive() != False:
            ok = QtWidgets.QPushButton()
            cacel = QtWidgets.QPushButton()

            msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")

            msg.addButton(ok,QtWidgets.QMessageBox.ActionRole)
            msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
            ok.setText(u'确定')
            cacel.setText(u'取消')

            if msg.exec_() != QtWidgets.QMessageBox.RejectRole:

                if self.cap.isOpened():
                    self.cap.release()
                if self.timer_camera.isActive():
                    self.timer_camera.stop()
                self.label_face.setText("<html><head/><body><p align=\"center\"><img src=\":/newPrefix/pic/Hint.png\"/><span style=\" font-size:28pt;\">点击打开摄像头</span><br/></p></body></html>")


class MyWindow_1(QMainWindow,Ui_MainWindow_print):
    def __init__(self, parent=None):
        super(MyWindow_1, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget_view.setStyleSheet('background-color: rgb(202, 235, 216);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.pushButton_print_ok.setStyleSheet('background-color: rgb(255, 99, 71);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.pushButton_print_ok.clicked.connect(self.close)
    def OPEN(self):
        self.show()




class MyWindow_2(QMainWindow,Ui_MainWindow_pay):
    def __init__(self, parent=None):
        super(MyWindow_2, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget_view_2.setStyleSheet('background-color: rgb(202, 235, 216);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.pushButton_pay_ok.setStyleSheet('background-color: rgb(255, 99, 71);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.pushButton_pay_ok.clicked.connect(self.close)
    def OPEN(self):
        self.show()



if __name__ == '__main__':
    # 打开数据库连接
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd=str(20230612),
        database='elec_scale',
        autocommit=True,
        charset="utf8")

    # 使用cursor()方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)

    # t=weight.Hx711()
    # t.start()
    app = QApplication(sys.argv)
    mywin= MyWindow()
    t = weight.Hx711(mywindow=mywin)
    mywin.init_t(t)
    t.start()
    #mywin.setStyleSheet("#mainWindow{border-image:url(./background.jpg)}")
    mywin.show()
    exit(app.exec_())
 # 关闭数据库连接
    db.close()

