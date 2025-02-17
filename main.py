"""
main.py
Date: 2025-02-15
"""

import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('home.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme='light_blue.xml')
    window.show()
    sys.exit(app.exec())