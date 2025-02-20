import cv2
import sys
from PyQt6 import uic
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from view.select_window import SelectWindow
from cart import Item
import detection
import class_dict

"""
File: view/main_window.py
Date: 2025-02-20
Author: SHENG
"""

CAP_FREQ = 30


class MainWindow(QMainWindow):
    item_list = []

    def __init__(self):
        super().__init__()
        uic.loadUi('view/main.ui', self)

        # Initialize the camera with cv
        self.capture = cv2.VideoCapture(1)
        if not self.capture.isOpened():
            print("Cannot open camera")
            sys.exit()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(int(1000 / CAP_FREQ))

        # Set slot functions with widgets
        self.select_btn.clicked.connect(self.show_select_dialog)

    # VIDEO MODULE
    def update_frame(self):
        """
        video label
        Return frames cv2 camera captured
        """
        ret, frame = self.capture.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Detect the class of object and mark
            class_idx = detection.classify_by_image(frame_rgb)
            predicted_label = class_dict.class_names[class_idx]
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame_rgb, f'Predicted: {predicted_label}', (10, 30), font, 1, (0,255, 0), 2)

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
        total_price = sum(item.price for item in self.item_list)
        self.total_price_label.setText(f"总金额：{total_price:.2f}￥")

    def show_select_dialog(self):
        dialog = SelectWindow()
        dialog.item_added.connect(self.insert_item_to_cart)
        dialog.exec()