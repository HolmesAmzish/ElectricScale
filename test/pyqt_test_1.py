import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit

app = QApplication(sys.argv)

window = QMainWindow()
window.resize(800, 600)
window.move(300, 310)
window.setWindowTitle('PyQt Test')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("Input table of salary")
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton("done", window)
button.move(380, 80)

window.show()

app.exec()
