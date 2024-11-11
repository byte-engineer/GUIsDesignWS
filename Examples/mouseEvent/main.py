from PyQt5.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QApplication, QWidget



class main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.UI()

    def UI(self):
        self.setGeometry(300, 200, 300 ,50)

        container = QWidget()
        self.setCentralWidget(container)

        disclbl = QLabel('Click and drag to change the values')

        layout = QVBoxLayout()
        container.setLayout(layout)

        self.lblMouse = QLabel('Mouse position: (??, ??)')
        layout.addWidget(disclbl)
        layout.addWidget(self.lblMouse)

    def mouseMoveEvent(self, event):
        
        self.lblMouse.setText(f'Mouse position: ({event.x()}, {event.y()})')    


        return super().mouseMoveEvent(event)
    
if __name__ == '__main__':
    app = QApplication([])

    win = main()
    win.show()

    app.exec()