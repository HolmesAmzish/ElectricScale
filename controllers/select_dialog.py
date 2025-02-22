from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QComboBox
from PyQt6.QtCore import pyqtSignal
import class_dict
from cart import Item

"""
File: view/select_dialog.py
Date: 2025-02-20
Author: SHENG
"""


class SelectWindow(QDialog):
    """
    Create a window to select label manually
    """

    # Define signal between windows for Item object
    item_added = pyqtSignal(Item)

    def __init__(self):
        super().__init__()
        uic.loadUi('view/select.ui', self)

        # Load all labels from local file: class_dict.py
        for label in class_dict.class_names_cn:
            self.label_list_box.addItem(label)

        # Set default price when initializing
        self.price_per_unit_label.setText(f"价格：{class_dict.class_prices[0]:.2f}￥")

        # Set slot functions
        self.label_list_box.currentIndexChanged.connect(self.update_price_label)
        self.weight_edit.textChanged.connect(self.update_total_price)
        self.accept_btn.clicked.connect(self.add_item_to_cart)

    def update_price_label(self):
        """Update the price label if label_list index changed"""
        index = self.label_list_box.currentIndex()
        price = class_dict.class_prices[index]
        self.price_per_unit_label.setText(f"价格：{price:.2f}￥")  # 设置价格，保留两位小数
        self.update_total_price()

    def update_total_price(self):
        """
        Update the total price when weight is edited
        It will get unit price from local file
        :return:
        """
        try:
            weight = float(self.weight_edit.text())
            index = self.label_list_box.currentIndex()
            price = class_dict.class_prices[index]
            total_price = price * weight
            self.price_label.setText(f"总价格：{total_price:.2f}￥")
        except ValueError:
            self.price_label.setText("总价格：请输入有效重量")

    def add_item_to_cart(self):
        """
        Create an Item object and send it to MainWindow's item_list.
        """
        label = self.label_list_box.currentText()   # Get label
        try:
            weight = float(self.weight_edit.text()) # Get weight
        except ValueError:
            weight = 0
        index = self.label_list_box.currentIndex()
        unit_price = class_dict.class_prices[index] # Get unit price
        price = unit_price * weight                 # Get total price
        item = Item(label, weight, unit_price, price)

        # Add the signal and close the dialog
        self.item_added.emit(item)
        self.accept()