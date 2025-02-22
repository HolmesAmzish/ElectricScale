import cv2
import sys
from PyQt6 import uic
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from controllers.select_dialog import SelectWindow
from controllers.pay_dialog import PayDialog
from models import detection
import class_dict
from cart import Item

"""
File: view/main_window.py
Date: 2025-02-20
Author: SHENG
"""

CAP_FREQ = 30   # Set camera to 30 FPS


class MainWindow(QMainWindow):
    item_list = []

    def __init__(self):
        super().__init__()
        uic.loadUi('view/main.ui', self)

        # Initialize the camera with cv
        self.capture = cv2.VideoCapture(1)
        self.text_browser.append("初始化摄像头...")
        if not self.capture.isOpened():
            print("Cannot open camera")
            sys.exit()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(int(1000 / CAP_FREQ))
        self.text_browser.append("欢迎使用智能果树识别电子秤！")

        # Set slot functions with widgets
        self.select_btn.clicked.connect(self.show_select_dialog)
        self.accept_btn.clicked.connect(self.accept_information)
        self.clear_btn.clicked.connect(self.remove_all_items_from_cart)
        self.pay_btn.clicked.connect(self.show_payment_dialog)

    # VIDEO MODULE
    def update_frame(self):
        """
        Return frame cv captured and send frames to model,
        update predicted label every frame.
        """
        ret, frame = self.capture.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Detect the class of object and mark
            class_idx = detection.classify_by_image(frame_rgb)
            predicted_label = class_dict.class_names[class_idx]
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(
                frame_rgb, f'Predicted: {predicted_label}',
                (10, 30), font, 1, (0, 255, 0), 2
            )

            self.update_information_table(class_idx, 5)
            # TODO: pi weighting module

            height, width, channels = frame_rgb.shape
            bytes_per_line = channels * width
            qimg = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
            self.video_label.setPixmap(QPixmap.fromImage(qimg))

    def closeEvent(self, event):
        self.capture.release()
        event.accept()

    # CART MODULE
    def insert_item_to_cart(self, item):
        """
        Insert item to cart table
        :param item: Item object
        :return:
        """
        # Insert a new row at the end of the table
        self.item_list.append(item)
        row_position = self.cart_table.rowCount()
        self.cart_table.insertRow(row_position)

        # Insert item data into the table
        self.cart_table.setItem(row_position, 0, QTableWidgetItem(item.label))
        self.cart_table.setItem(row_position, 1, QTableWidgetItem(str(item.unit_price)))
        self.cart_table.setItem(row_position, 2, QTableWidgetItem(str(item.weight)))
        self.cart_table.setItem(row_position, 3, QTableWidgetItem(str(item.price)))

        # update the total price
        self.update_total_price()

    def update_total_price(self):
        """Calculate total price in cart"""
        total_price = sum(item.price for item in self.item_list)
        self.total_price_label.setText(f"总金额：{total_price:.2f}￥")

    def update_information_table(self, class_index, weight):
        label = class_dict.class_names_cn[class_index]
        unit_price = class_dict.class_prices[class_index]
        self.information_table.setItem(0, 0, QTableWidgetItem(label))
        self.information_table.setItem(1, 0, QTableWidgetItem(str(unit_price)))
        self.information_table.setItem(2, 0, QTableWidgetItem(str(weight)))
        self.information_table.setItem(3, 0, QTableWidgetItem(str(weight * unit_price)))

    def accept_information(self):
        """Handle the accept button click event"""
        label = self.information_table.item(0, 0).text()
        unit_price = float(self.information_table.item(1, 0).text())
        weight = float(self.information_table.item(2, 0).text())
        price = float(self.information_table.item(3, 0).text())

        item = Item(label, unit_price, weight, price)
        self.insert_item_to_cart(item)

    def remove_item_from_cart(self, cart_index):
        if 0 <= cart_index < len(self.item_list):
            self.cart_table.removeRow(cart_index)
            self.item_list.pop(cart_index)
            self.update_total_price()

    def remove_all_items_from_cart(self):
        for i in range(len(self.item_list) - 1, -1, -1):
            self.remove_item_from_cart(i)
        self.text_browser.append("所有物品已从购物车清空。")

    def show_select_dialog(self):
        dialog = SelectWindow()
        dialog.item_added.connect(self.insert_item_to_cart)
        dialog.exec()

    def show_payment_dialog(self):
        price = sum(item.price for item in self.item_list)
        pay_dialog = PayDialog(cart_items=self.item_list, total_price=price)
        pay_dialog.payment_accepted.connect(self.remove_all_items_from_cart)
        pay_dialog.exec()