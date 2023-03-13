from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont,QIcon,QMovie
from PyQt6.QtCore import QSize
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('11 - spinbox')
        self.setGeometry(50,50,400,500)
        self.create_widgets()

    def create_widgets(self):
        self.spin = QSpinBox(self,
        value = 2,#valor começa em 2
        #prefix = '*',
        #suffix = 'pizza',
        maximum = 100)


        self.label_mussarela = QLabel('Pizza de Mussarela. R$50,00')
        self.label_total = QLabel("Total = R$00,00")

        self.spin.valueChanged.connect(self.spin_value)

        grid = QGridLayout()
        grid.addWidget(self.spin,0,1)
        grid.addWidget(self.label_mussarela,0,0)
        grid.addWidget(self.label_total,0,2)
        self.setLayout(grid)

    def spin_value(self):
        self.label_total.setText(f'Total = R$ {50 * int(self.spin.text()),00}')

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())