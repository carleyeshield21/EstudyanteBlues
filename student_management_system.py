from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget,  QGridLayout, QLineEdit, QPushButton, QMainWindow, QTableWidget
from PyQt6.QtGui import QAction
import sys
import datetime

class MainWindow(QMainWindow): #QMainWindow has a menu bar, toolbar, status bar
    def __init__(self):
        super().__init__() #To call the init of the parent class, in this code QMainWindow
        self.setWindowTitle('Estudyante Blues Management System') #setting the title of the app

        # Adding items on the menu bar
        file_menu_item = self.menuBar().addMenu('&File') #Adding the ampersand sign in the beginning of the word will underscore the first letter
        help_menu_item = self.menuBar().addMenu('&Help')

        # adding the sub menus or the action to the items in the main menu
        add_student_action = QAction('Add Stoodent',self) #must from PyQt6.QtGui import QAction, must also add the argument self to show from the
        # drop down menu
        file_menu_item.addAction(add_student_action)

        about_action = QAction('About',self)
        help_menu_item.addAction(about_action)
        # about_action.setMenuRole(QAction.MenuRole.NoRole) => only include this code if help menu does not show up, (Mac users)

        # adding a table to the app, QTableWidget should be imported
        self.teybol = QTableWidget() #this variable will be accessed from another function to load the the table so we need to add the self keyword
        self.teybol.setColumnCount(20) #setting the column count of our table
        self.teybol.setHorizontalHeaderLabels(('ID', 'Name', 'Course', 'MobileNumber')) #setting the label names of each column

    #creating another function for the table
    def load_data(self):
        self.teybol

# the codes below are for the app to launch
app = QApplication(sys.argv)
estudyante_blues = MainWindow()
estudyante_blues.show()
sys.exit(app.exec())

if __name__ == '__main__':
    MainWindow()