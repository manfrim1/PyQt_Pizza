from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont,QPixmap,QPicture,QIcon,QMovie
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Grill Gourmets')
        self.setGeometry(500,500,600,500)
        self.setWindowIcon(QIcon('cozinhar.png'))
        '''
        label = QLabel(self)
        label.setText("Leonardo Manfrim")
        label.setFont(QFont("Sanserif",20))
        label.setStyleSheet('Color:Green')

        
        
        
        '''
        '''
        label = QLabel(self)        
        background = QPixmap('wp8513047-gourmet-wallpapers.jpg')
        label.setPixmap(background)
        
        '''
        
        label = QLabel(self)
        backgroundgif = QMovie('lamen.gif')
        label.setMovie(backgroundgif)        
        backgroundgif.start()

        
        
        



app = QApplication(sys.argv) 
window = MyWindow()
window.show()
sys.exit(app.exec())
