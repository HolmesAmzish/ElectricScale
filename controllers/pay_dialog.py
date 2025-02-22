from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import pyqtSignal
from cart import Item
import models.payment_generator as payment_generator

"""
File: controllers/pay_dialog.py
Date: 2025-02-22
"""


class PayDialog(QDialog):
    payment_accepted = pyqtSignal()

    def __init__(self, cart_items, total_price):
        super().__init__()
        uic.loadUi('view/pay_dialog.ui', self)

        self.accept_btn.clicked.connect(self.accept_pay)
        self.cancel_btn.clicked.connect(self.cancel_pay)

        # Get cart items and total price

        self.cart_items = cart_items
        self.total_price = total_price

        qr_pixmap = payment_generator.generate_qrcode(self.cart_items, self.total_price)
        order_id = payment_generator.generate_order_id()
        bar_pixmap = payment_generator.generate_barcode(order_id)

        self.qrcode_label.setPixmap(qr_pixmap)
        self.barcode_label.setPixmap(bar_pixmap)
        # self.price_label.setText(f"总金额：{total_price:.2f}￥")

    def cancel_pay(self):
        self.reject()

    def accept_pay(self):
        self.payment_accepted.emit()
        self.accept()
