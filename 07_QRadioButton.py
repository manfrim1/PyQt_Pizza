from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont,QIcon,QMovie
import sys



class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('07 - Radio Button')
        self.create_widgets()



    def create_widgets(self):
        rad1 = QRadioButton("WhatsApp")
        rad1.setIcon(QIcon('whatsapp.png'))

        rad2 = QRadioButton("Instagram")
        rad2.setIcon(QIcon('instagram.png'))

        rad3 = QRadioButton("Facebook")
        rad3.setIcon(QIcon('facebook.png'))
        self.label = QLabel("Escolha sua rede social favorita")

        rad1.toggled.connect(self.radio_button_selected)#conectando os radios button
        rad2.toggled.connect(self.radio_button_selected)
        rad3.toggled.connect(self.radio_button_selected)


        


        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(rad1)
        vbox.addWidget(rad2)
        vbox.addWidget(rad3)
        self.setLayout(vbox)

    def radio_button_selected(self):
        radio_selected = self.sender()
        if radio_selected.isChecked():
            self.label.setText(f"sua rede social favorita é: {radio_selected.text()}")




app = QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec())