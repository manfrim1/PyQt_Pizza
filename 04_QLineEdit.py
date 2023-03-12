from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont,QPixmap,QPicture,QIcon,QMovie
import sys


class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,600)
        self.setWindowTitle('04 - Lineedit')#define o texto da window
        self.setMinimumHeight(80)#define o minimo de largura da tela.
        self.create_line_edit()#cria o componente

    def create_line_edit(self):
        line_edit = QLineEdit(self)
        line_edit.setFont(QFont('sanserif',15))#define a fonte da letra
        line_edit.setPlaceholderText("Digite sua senha: ")# é uma legenda que fica no campo:
        #line_edit.setText('Olá tudo bem?')# vem escrito como padrão no line_edit
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)# define a mascara de senha para o que for digitado dentro do line_edit


        



app = QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec())