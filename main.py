import sys
from PyQt6.QtWidgets import QApplication
from view.main_window import MainWindow

"""
File: main.py
Date: 2025-02-20
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
