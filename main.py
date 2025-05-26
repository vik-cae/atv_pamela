import sys
import shutil
shutil.rmtree('__pycache__', ignore_errors=True)
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap
from login import Ui_MainWindow as Ui_Login  # Interface da janela de login
from ui_finalizado import Ui_Form as Ui_Finalizado

class JanelaFinalizada(QMainWindow):
    """ Segunda janela (tela final) """
    def __init__(self, peso, altura):
        super().__init__()
        self.ui = Ui_Finalizado()
        self.ui.setupUi(self)

        # Exibir peso e altura capturados na tela anterior
        self.ui.label_peso_tela_inicial.setText(f"{peso} kg")
        self.ui.label_altura_tela_iicial.setText(f"{altura} m")

        # Calcular IMC
        imc = peso / (altura ** 2)
        self.ui.label_imc_tela_inicial_meio.setText(f"IMC: {imc:.2f}")  # Exibir IMC com duas casas decimais

        # Definir imagens nos QLabel
        self.carregar_imagens()

    def carregar_imagens(self):
        """ Define as imagens nos QLabel da interface """
        imagens = {
            self.ui.label_card: "./imagens/card-suco.png",
            self.ui.label_card_2: "./imagens/card-salda.png",
            self.ui.label_vector_circulo: "./imagens/circulo-verde.png",
            self.ui.label_vector_2: "./imagens/direita-vector.png",
            self.ui.label_vector: "./imagens/esquerda-vector.png",
            self.ui.label_cabecalho: "./imagens/onda-cima.png",
            self.ui.label_2: "./imagens/nutrir-se-bem.png",
            self.ui.label_foto: "./imagens/imagem-lembrete.png",
            self.ui.label_onda: "./imagens/onda-meio.png",
            self.ui.label_vector_linhas: "./imagens/Group 20.png",
            self.ui.label_vector_linhas_2: "./imagens/Group 20.png",
            self.ui.label: "./imagens/Group 18.png",

        }
        for label, img_path in imagens.items():
            label.setPixmap(QPixmap(img_path))


class JanelaLogin(QMainWindow):
    """ Janela de login """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # Definir imagem de fundo no QLabel login
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

        # Abrir a segunda janela e passar os valores para cálculo do IMC
        self.janela_finalizada = JanelaFinalizada(peso, altura)
        self.janela_finalizada.show()

        # Fechar a tela de login
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JanelaLogin()
    window.show()
    sys.exit(app.exec_())
