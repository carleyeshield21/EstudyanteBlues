from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QLabel, QWidget,  QGridLayout, QLineEdit, QPushButton, QMainWindow, QTableWidget,
                             QTableWidgetItem, QDialog, QComboBox, QToolBar)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
import sys
import sqlite3
import pandas

table = pandas.read_csv('Family Income and Expenditure.csv')
kunyare_courses = list(table.columns.values) #list for column titles

class MainWindow(QMainWindow): #QMainWindow has a menu bar, toolbar, status bar
    def __init__(self):
        super().__init__() #To call the init of the parent class, in this code QMainWindow
        self.setWindowTitle('Estudyante Blues Management System') #setting the title of the app
        self.setMinimumSize(800,600) #setting the size of the output window

        # Adding items on the menu bar
        file_menu_item = self.menuBar().addMenu('&File') #Adding the ampersand sign in the beginning of the word will underscore the first letter
        help_menu_item = self.menuBar().addMenu('&Help')

        edit_menu_item = self.menuBar().addMenu('&Edit') #adding the Edit to the menu bar,can be clicked but no action is added yet, to add the action, we need the codes on line39,40

        # adding the sub menus or the action to the items in the main menu
        add_student_action = QAction(QIcon('icons/add.png'),'&Add Stoodent',self) #the new code to add icon from line24, you can right click on the
        # file from the folder where the icon is located then choose Copy Path/Reference then Path from Content Root

        # add_student_action = QAction('&Add Stoodent',self) #must from PyQt6.QtGui import QAction, must also add the argument self to show from the
        # drop down menu

        add_student_action.triggered.connect(self.insert) #the method insert should be created, line69
        file_menu_item.addAction(add_student_action)

        about_action = QAction('&About',self)
        help_menu_item.addAction(about_action)
        # about_action.setMenuRole(QAction.MenuRole.NoRole) => only include this code if help menu does not show up, (Mac users)

        search_action = QAction('&Search', self) #this code is needed first before we can add the option when we click the Edit on the menu bar
        edit_menu_item.addAction(search_action) #this code will show the option Search when we click the Edit on the menu bar
        search_action.triggered.connect(self.search) #the search method should be created, line74


        # adding a table to the app, QTableWidget should be imported
        self.teybol = QTableWidget() #this variable will be accessed from another function to load the the table so we need to add the self keyword
        self.teybol.setColumnCount(4) #setting the column count of our table
        self.teybol.setHorizontalHeaderLabels(('ID', 'Name', 'Course', 'MobileNumber')) #setting the label names of each column
        self.teybol.verticalHeader().setVisible(False) #this code will disable the first default column(optional)
        self.setCentralWidget(self.teybol) #this line of code will execute the layout of the table we have created

        #create toolbars and adding toolbar elements import QToolBar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar) #adds the toolbar to the window
        toolbar.addAction(add_student_action) #from line21


    #creating another function for the table
    def load_data(self):
        kuneksyon = sqlite3.connect('database.db') #creating a connection to the database file
        resulta_ng_database_teybol = kuneksyon.execute('SELECT * FROM students') #executing the connection from the database and making a database
        # query
        # print(type(resulta_ng_database_teybol))
        self.teybol.setRowCount(0) #prevents duplicate data
        for index_row_number, row_data in enumerate(resulta_ng_database_teybol): #this nested for loop will set the items in the table cells
            self.teybol.insertRow(index_row_number)
            for index_column_number, data in enumerate(row_data):
                self.teybol.setItem(index_row_number, index_column_number, QTableWidgetItem(str(data)))
        kuneksyon.close()

    def insert(self): #this function created from line18
        dayalog = InsertDialog() #this class should be created in line50
        dayalog.exec()

    def search(self):
        dialog = SearchDialog() #this class is created line124 outside the MainWindow class
        dialog.exec()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__() #calling the parent class
        self.setWindowTitle('Insert stoodent tata')  # setting the title of the app
        self.setFixedWidth(300) #distance between widgets (depends on the design)
        self.setFixedHeight(300) #distance between widgets (depends on the design)

        layout = QVBoxLayout() #we can use QGridLayout() (depends on desired layout, this is stacked vertically)

        # creating the widgets
        self.stoodent_name = QLineEdit()
        self.stoodent_name.setPlaceholderText('Type student name here') #setting a placeholder for student name

        self.course_drop_down = QComboBox() #drop down list widget
        self.course_drop_down.addItems(kunyare_courses) #adding items from any list

        self.mobile_num = QLineEdit() #mobile number widget
        self.mobile_num.setPlaceholderText('Anong cell number mo?')

        submit_mo_na_boton = QPushButton('Register your information')

        # placement of widgets to the layout of app
        layout.addWidget(self.stoodent_name) #adding the widget, no need to add the rows and columns because we chose the QVBoxLayout(),
        # which is stacked vertically
        layout.addWidget(self.course_drop_down)
        layout.addWidget(self.mobile_num)
        layout.addWidget(submit_mo_na_boton)
        submit_mo_na_boton.clicked.connect(self.add_student) #we will connect a method when this button si clicked, this function is created in line85

        self.setLayout(layout) #output of the widget layout

    def add_student(self): #will connect to a database, the variables required will have the word self. added to access those in this method
        name = self.stoodent_name.text() #extracting the text using text() method
        course = self.course_drop_down.itemText(self.course_drop_down.currentIndex()) #this should be the format for a combo box or drop down list
        # to extract the choice
        mobile = self.mobile_num.text() #extracting the text using text() method
        database_connection = sqlite3.connect('database.db')
        korsor = database_connection.cursor()
        korsor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)", (name, course, mobile))
        database_connection.commit() #to apply the changes in the database

        korsor.close()
        database_connection.close()

        estudyante_blues.load_data() #to automatically update the database without the need to close it and open again

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        # setting title and size
        self.setWindowTitle('Maghanap ka ng istudyante')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # creating layout and widget
        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('Sinong hinahanap mo?')
        layout.addWidget(self.student_name)

        # creating button
        button = QPushButton('&Search')
        button.clicked.connect(self.search) #the search method will be created in line145
        layout.addWidget(button)

        self.setLayout(layout) #to output of the dialog box

    def search(self):
        pass


# the codes below are for the app to launch
app = QApplication(sys.argv)
estudyante_blues = MainWindow()
estudyante_blues.show()
estudyante_blues.load_data() #this method should be called so we can execute the table on the app, without this line of code the table from the
# database will not populate the table
sys.exit(app.exec())

if __name__ == '__main__':
    MainWindow()