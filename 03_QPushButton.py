from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont,QCursor,QIcon
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,800,450)
        self.create_button()


    def create_button(self):
        btn = QPushButton('Inserir',self)
        btn.setGeometry(50,50,300,90)
        btn.setFont(QFont('times',25,QFont.Weight.ExtraLight))
        btn.setIcon(QIcon("lamen.png"))
        


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())