# Examples/LogIn.py

from PyQt5.QtWidgets import *
import os


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.PassWord = "PyQt5"
        self.initData()
        self.UI()

    def initData(self):
        with open('Data.txt', 'r') as f:
            if f.read() == '':
                file = open('Data.txt', 'a')
                file.write(f"|> {"UserName".ljust(15)} || {"passwords".ljust(10)}\n")


    def UI(self):
        # Main Window Configurations.
        self.setGeometry(500, 300, 300, 100)
        self.setWindowTitle("Passwords Saver!")
        self.setFixedSize(300, 100)

        MLayout = QVBoxLayout()
        container = QWidget()
        self.setCentralWidget(container)
        container.setLayout(MLayout)

        InputsGrid = QGridLayout()
        MLayout.addLayout(InputsGrid)

        self.UserInput = QLineEdit()
        self.UserInputlbl = QLabel('User Name: ')
        self.UserInput.setPlaceholderText('enter Name')
        InputsGrid.addWidget(self.UserInputlbl, 0, 0)
        InputsGrid.addWidget(self.UserInput, 0, 1)

        self.passInput = QLineEdit()
        self.passInput.setPlaceholderText('enter Password')
        self.passInput.setEchoMode(QLineEdit.Password)
        passInputlbl = QLabel('PassWord: ')
        InputsGrid.addWidget(passInputlbl, 1, 0)
        InputsGrid.addWidget(self.passInput, 1, 1)

        btnsLayout = QHBoxLayout()
        self.logBtn = QPushButton("Done")
        self.logBtn.clicked.connect(self.validate)
        MLayout.addWidget(self.logBtn)
        self.viewBtn = QPushButton('View')
        self.viewBtn.clicked.connect(self.view)

        btnsLayout.addWidget(self.viewBtn, 1)
        btnsLayout.addWidget(self.logBtn, 2)

        MLayout.addLayout(btnsLayout)

    def validate(self, event):

        if self.UserInput.text() != '' and self.passInput.text() != '':

            with open('Data.txt', 'a') as f:
                f.write(f"|> {self.UserInput.text().ljust(15)} || {self.passInput.text().ljust(10)}\n")

            self.passInput.clear()
            self.UserInput.clear()

    def view(self):
        with open('Data.txt', 'r') as f:
            data = f.read()

        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("password INFO")
        msg.setText(data)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()

if __name__ == '__main__':
    app = QApplication([])
    win = Main()
    win.show()
    app.exec()