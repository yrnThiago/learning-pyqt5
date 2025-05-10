import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Learning PyQt5")
        self.setGeometry(300, 200, 1280, 720)
        self.setWindowIcon(QIcon("icon.png"))

        # label = QLabel("Hello", self)
        # label.setFont(QFont("Arial", 40))
        # label.setGeometry(0, 0, 1280, 100)
        # label.setStyleSheet("color: blue; background-color: yellow; font-weight: bold;")

        # label.setAlignment(Qt.AlignCenter)

        self.InitUi()

    def InitUi(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("Hello #1", self)
        label1.setStyleSheet("background-color: yellow;")

        label2 = QLabel("Hello #2", self)
        label2.setStyleSheet("background-color: green;")

        label3 = QLabel("Hello #3", self)
        label3.setStyleSheet("background-color: red;")

        label4 = QLabel("Hello #4", self)
        label4.setStyleSheet("background-color: purple;")
        
        label5 = QLabel("Hello #5", self)
        label5.setStyleSheet("background-color: orange;")

        grid = QGridLayout()
                            # ROW COL
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 0, 2)
        grid.addWidget(label4, 1, 0)
        grid.addWidget(label5, 2, 0)

        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()