from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QLabel, QWidget,  QGridLayout, QLineEdit, QPushButton, QMainWindow, QTableWidget,
                             QTableWidgetItem, QDialog, QComboBox)
from PyQt6.QtGui import QAction
import sys
import sqlite3
import pandas

table = pandas.read_csv('Family Income and Expenditure.csv')
kunyare_courses = list(table.columns.values) #list for column titles

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
        add_student_action.triggered.connect(self.insert) #the function insert should be created
        file_menu_item.addAction(add_student_action)

        about_action = QAction('About',self)
        help_menu_item.addAction(about_action)
        # about_action.setMenuRole(QAction.MenuRole.NoRole) => only include this code if help menu does not show up, (Mac users)

        # adding a table to the app, QTableWidget should be imported
        self.teybol = QTableWidget() #this variable will be accessed from another function to load the the table so we need to add the self keyword
        self.teybol.setColumnCount(4) #setting the column count of our table
        self.teybol.setHorizontalHeaderLabels(('ID', 'Name', 'Course', 'MobileNumber')) #setting the label names of each column
        self.teybol.verticalHeader().setVisible(False) #this code will disable the first default column(optional)
        self.setCentralWidget(self.teybol) #this line of code will execute the layout of the table we have created

    #creating another function for the table
    def load_data(self):
        kuneksyon = sqlite3.connect('database.db') #creating a connection to the database file
        resulta_ng_database_teybol = kuneksyon.execute('SELECT * FROM students') #executing the connection from the database and making a database
        # query
        print(type(resulta_ng_database_teybol))
        self.teybol.setRowCount(0) #prevents duplicate data
        for index_row_number, row_data in enumerate(resulta_ng_database_teybol): #this nested for loop will set the items in the table cells
            self.teybol.insertRow(index_row_number)
            for index_column_number, data in enumerate(row_data):
                self.teybol.setItem(index_row_number, index_column_number, QTableWidgetItem(str(data)))
        kuneksyon.close()

    def insert(self): #this function created from line18
        dayalog = InsertDialog() #this class should be created in line50
        dayalog.exec()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__() #calling the parent class
        self.setWindowTitle('Insert stoodent tata')  # setting the title of the app
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout() #we can use QGridLayout() (depends on desired layout)

        # creating the widgets
        stoodent_name = QLineEdit()
        stoodent_name.setPlaceholderText('Type student name here') #setting a placeholder for student name

        course_drop_down = QComboBox()
        course_drop_down.addItems(kunyare_courses)

        layout.addWidget(stoodent_name) #adding the widget, no need to add the rows and columns because we chose the QVBoxLayout(),
        # which is stacked vertically

        self.setLayout(layout) #output of the widget layout



# the codes below are for the app to launch
app = QApplication(sys.argv)
estudyante_blues = MainWindow()
estudyante_blues.show()
estudyante_blues.load_data() #this function should be called so we can execute the table on the app, without this line of code the table from the
# database will not populate the table
sys.exit(app.exec())

if __name__ == '__main__':
    MainWindow()