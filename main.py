import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from nutricionista import Ui_MainWindow

class nutricionista(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_entrar.connect(self.resultado)

    def resultado(self):
        nome = str(self.ui.lineEdit_nome.text()).upper()  # Convertendo a entrada para maiúsculas
        peso = float(self.ui.lineEdit_peso.text())
        idade = int(self.ui.lineEdit_idade.text())
        altura = float(self.ui.lineEdit_altura.text())
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = nutricionista()
    window.show()
    sys.exit(app.exec_())