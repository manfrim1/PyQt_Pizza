from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont,QIcon,QMovie
from PyQt6.QtCore import QSize
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,600)
        self.setWindowTitle('09_ChecBox')
        self.create_widgets()


    def create_widgets(self):
        self.check1 = QCheckBox('whatsapp')
        self.check1.setIcon(QIcon('whatsapp.png'))
        self.check1.setFont(QFont('sanserif',15))
        self.check1.toggled.connect(self.item_selected)
        

        self.check2 = QCheckBox('instagram')
        self.check2.setIcon(QIcon('instagram.png'))
        self.check1.setFont(QFont('sanserif',15))
        self.check2.toggled.connect(self.item_selected)

        self.check3 = QCheckBox('facebook')
        self.check3.setIcon(QIcon('facebook.png'))
        self.check1.setFont(QFont('sanserif',15))
        self.check3.toggled.connect(self.item_selected)

        self.label = QLabel('Escolha suas redes sociais favoritas')
        self.label.setFont(QFont())

        vbox = QVBoxLayout()
        vbox.addWidget(self.check1)
        vbox.addWidget(self.check2)
        vbox.addWidget(self.check3)
        vbox.addWidget(self.label)

        self.setLayout(vbox)


    def item_selected(self):
        texto1 = ''
        texto2 = ''
        texto3 = ''
        if self.check1.isChecked():
            texto1 = self.check1.text()
        if self.check2.isChecked():
            texto2 = self.check2.text()
        if self.check3.isChecked():
            texto3 = self.check3.text()

        text = texto1 + ' ' + texto2 + ' ' + texto3

        self.label.setText("Redes sociais escolhidas: " + text)


        


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())

