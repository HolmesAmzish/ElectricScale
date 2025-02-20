import sys
import cv2
from PyQt6 import uic
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from cart import Item
import detection


CAP_FREQ = 30


class MainWindow(QMainWindow):
    item_list = []

    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)

        # Initialize the camera with cv
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            print("Cannot open camera")
            sys.exit()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(int(1000 / CAP_FREQ))

        # Test cart insert
        self.insert_items_to_cart()

    # VIDEO MODULE
    def update_frame(self):
        """
        video label
        Return frames cv2 camera captured
        """
        ret, frame = self.capture.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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

    def insert_items_to_cart(self):
        """
        TEST
        Insert all items from the list into the cart table.
        """
        items = [
            Item("苹果", 0.5, 3.0, 1.5),
            Item("香蕉", 0.3, 2.5, 0.75),
            Item("橙子", 0.6, 4.0, 2.4),
        ]
        for item in items:
            self.insert_item_to_cart(item)

    def update_total_price(self):
        total_price = sum(item.price for item in self.item_list)
        self.total_price_label.setText(f"总金额：{total_price:.2f}￥")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())