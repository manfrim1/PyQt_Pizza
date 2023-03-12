from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont,QIcon,QMovie
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('06 - GridLayout')
        

    def criar_widgets(self):
        btn = QPushButton('Mudar texto ')
        btn.clicked.connect(self.clicked_btn)

        btn_voltar = QPushButton('Voltar texto Original')
        btn_voltar.clicked.connect(self.clicked_voltar)

        self.texto_original = "Eai galera esse é nosso texto original"
        self.lb = QLabel(self.texto_original)

        grid = QGridLayout()
        grid.addWidget(btn,0,0)
        grid.addWidget(btn_voltar,0,1)     
        grid.addWidget(self.lb,0,1)
        self.setLayout(grid)

    def clicked_btn(self):
        self.lb.selectedText("O texto mudou")

    def clicked_voltar(self):
        self.lb.selectedText(self.texto_original)

    
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())