from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget,  QGridLayout, QLineEdit, QPushButton, QMainWindow
import sys
import datetime

class MainWindow(QMainWindow): #QMainWindow has a menu bar, toolbar, status bar
    def __init__(self):
        super().__init__() #To call the init of the parent class, in this code QMainWindow
        self.setWindowTitle('Estudyante Blues Management System') #setting the title of the app

        # Adding items on the menu bar
        file_menu_item = self.menuBar().addMenu('&File') #Adding the ampersand sign in the beginning of the word will underscore the first letter
        help_menu_item = self.menuBar().addMenu('&Help')

# the codes below are for the app to launch
app = QApplication(sys.argv)
estudyante_blues = MainWindow()
estudyante_blues.show()
sys.exit(app.exec())

if __name__ == '__main__':
    MainWindow()