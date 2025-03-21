import sys

import shutil
shutil.rmtree('__pycache__', ignore_errors=True)
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel,QMessageBox
from PyQt5.QtGui import QPixmap
from login import Ui_MainWindow as Ui_Login  # Interface da janela de login
from ui_finalizado import Ui_Form as Ui_Finalizado



class JanelaFinalizada(QMainWindow):
    """ Segunda janela (tela final) """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Finalizado()
        self.ui.setupUi(self)

class JanelaLogin(QMainWindow):
    """ Janela de login """
    def __init__(self):
        super().__init__()

        # Carregar a interface do designer
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # Definir imagem de fundo no QLabel
        pixmap = QPixmap("./imagens/fundo-login.png")
        self.ui.label.setPixmap(pixmap)

        # Conectar botão "Entrar" à função que salva e abre nova janela
        self.ui.pushButton_entrar.clicked.connect(self.salvar_dados)

    def salvar_dados(self):
        """ Captura os dados e abre a nova janela """
        nome = self.ui.lineEdit_nome.text().strip()
        idade = self.ui.lineEdit_idade.text().strip()
        peso = self.ui.lineEdit_peso.text().strip()
        altura = self.ui.lineEdit_altura.text().strip()

        # Verificar se os campos estão preenchidos
        if not (nome and idade and peso and altura):
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")
            return

        try:
            peso = float(peso)
            altura = float(altura)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Peso e altura devem ser números válidos!")
            return

        # Salvar os dados no arquivo
        with open("dados_salvos.txt", "a") as file:
            file.write(f"Nome: {nome}, Idade: {idade}, Peso: {peso}, Altura: {altura}\n")

        # Abrir a segunda janela
        self.janela_finalizada = JanelaFinalizada()
        self.janela_finalizada.show()

        # Fechar a tela de login
        self.close()

        


    #def __init__(self):
        ####super().__init__()
        
        # Carregar a interface do designer (arquivo .ui)
        # Se você estiver usando o arquivo .ui diretamente:
        #####self.ui = uic.loadUi("login.ui", self)
        
        # Ou se converteu para Python:
        # from seu_arquivo_ui import Ui_MainWindow
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        
        # Definir a imagem para um QLabel (assumindo que você tem um QLabel chamado 'label_imagem')
        ####pixmap = QPixmap("./imagens/fundo-login.png")
        #####self.ui.label.setPixmap(pixmap)
        # Você pode redimensionar a imagem se necessário
        # self.ui.label_imagem.setScaledContents(True)
        
        ####self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JanelaLogin()
    window.show()
    sys.exit(app.exec_())


