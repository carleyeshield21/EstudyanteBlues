from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget,  QGridLayout, QLineEdit, QPushButton, QMainWindow
import sys
import datetime

class MainWindow(QMainWindow): #QMainWindow has a menu bar, toolbar, status bar
    def __init__(self):
        super().__init__() #To call the init of the parent class, in this code QMainWindow
        self.setWindowTitle('Estudyante Blues Management System')

app = QApplication(sys.argv)
estudyante_blues = MainWindow()
estudyante_blues.show()
sys.exit(app.exec())

if __name__ == '__main__':
    MainWindow()