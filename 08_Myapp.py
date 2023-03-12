# Form implementation generated from reading ui file 'Myapp.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(403, 281)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 381, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        #botão
        self.btn_alterar = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_alterar.setFont(font)
        self.btn_alterar.setFlat(False)
        self.btn_alterar.setObjectName("btn_alterar")
        self.horizontalLayout.addWidget(self.btn_alterar)
        self.btn_alterar.clicked.connect(self.alterar_texto)

        #linedit
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        #label
        self.label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    #função alterar texto
    def alterar_texto(self):
        texto = self.lineEdit.text()
        self.label.setText(texto)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tela de Introdução"))
        self.btn_alterar.setText(_translate("Form", "Alterar Texto"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Digite o seu texto aqui..."))
        self.label.setText(_translate("Form", "Seu texto irá aparecer aqui."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
