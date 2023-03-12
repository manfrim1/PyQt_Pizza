from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('05 - Box Layout')
        self.setGeometry(100,100,500,600)
        self.criar_widgets()#Funcão que irá criar os widgets

    def criar_widgets(self):
         # criar o layout vertical onde os componentes irão ficar em formato de layout
        VerticalBox = QVBoxLayout()

        # Declarou os componentes
        button = QPushButton('Entrar')
        line_edit = QLineEdit()
        line_edit2 = QLineEdit()
        line_edit.setPlaceholderText('Digite seu e-mail')
        line_edit2.setPlaceholderText('Digite sua senha')
        line_edit2.setEchoMode(QLineEdit.EchoMode.Password)
        
        #Adicionando o componente no layout OBS: os componentes ficam na ordem que for declarado.
        
        VerticalBox.addWidget(line_edit) 
        VerticalBox.addWidget(line_edit2)
        VerticalBox.addWidget(button)

        #passando o vertical box de parametro para aparecer na tela.
        self.setLayout(VerticalBox)










app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
