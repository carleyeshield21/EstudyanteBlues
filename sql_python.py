from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QLabel, QWidget,  QGridLayout, QLineEdit, QPushButton, QMainWindow, QTableWidget,
                             QTableWidgetItem, QDialog, QComboBox, QToolBar, QStatusBar, QMessageBox)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt #used in line152
import sys #used in line158, window will not run without this
import sqlite3
import pandas
import mysql.connector

table = pandas.read_csv('Family Income and Expenditure.csv')
kunyare_courses = list(table.columns.values) #list for column titles

class DatabaseConnection():
    def __init__(self, host='localhost', user='root', password='pythonsql',database='iskul_bukol'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        return connection

# class DatabaseConnection():
#     def __init__(self, database_file = 'database.db'):
#         self.database_file = database_file
#
#     def connect(self):
#         connection = sqlite3.connect(self.database_file)
#         return connection

class MainWindow(QMainWindow): #QMainWindow has a menu bar, toolbar, status bar
    def __init__(self):
        super().__init__() #To call the init of the parent class, in this code QMainWindow
        self.setWindowTitle('Estudyante Blues Management System') #setting the title of the app
        self.setMinimumSize(800,600) #setting the size of the output window

        # Adding items on the menu bar
        file_menu_item = self.menuBar().addMenu('&File') #Adding the ampersand sign in the beginning of the word will underscore the first letter
        help_menu_item = self.menuBar().addMenu('&Help')

        edit_menu_item = self.menuBar().addMenu('&Edit') #adding the Edit to the menu bar,can be clicked but no action is added yet, to add the action, we need the codes on line39,40

        # adding the sub menus or the action to the items in the main menu, and adding the icon for add student
        add_student_action = QAction(QIcon('icons/add.png'),'&Add Stoodent',self) #the new code to add icon from line27, you can right click on the
        # file from the folder where the icon is located then choose Copy Path/Reference then Path from Content Root
        # add_student_action = QAction('&Add Stoodent',self) #must from PyQt6.QtGui import QAction, must also add the argument self to show from the
        # drop down menu

        add_student_action.triggered.connect(self.insert) #the method insert should be created, line69
        file_menu_item.addAction(add_student_action)

        about_action = QAction('&About',self)
        help_menu_item.addAction(about_action)
        # about_action.setMenuRole(QAction.MenuRole.NoRole) => only include this code if help menu does not show up, (Mac users)
        about_action.triggered.connect(self.about)

        # adding the icon for search
        search_action = QAction(QIcon('icons/search.png'),'&Search',self)  # this code is needed first before we can add the option when we click the Edit on the menu bar, previous code from line39
        # search_action = QAction('&Search', self) #this code is needed first before we can add the option when we click the Edit on the menu bar

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
        toolbar.addAction(search_action)

        #Creating Status bar and status bar elements
        self.istatus_bar = QStatusBar() #creating a status bar instance, will be accessed in a_cell_is_clicked method
        self.setStatusBar(self.istatus_bar) #will show a gray status bar created below the window

        #Detecting a click
        self.teybol.cellClicked.connect(self.a_cell_is_clicked) #created method on line66

    def a_cell_is_clicked(self):
        edit_button = QPushButton('Edit record')
        edit_button.clicked.connect(self.edit) #create method
        print('Clicked')

        delete_button = QPushButton('Delete record')
        delete_button.clicked.connect(self.delete) #method will be created

        #clearing duplicate buttons, without this code, the buttons will be duplicated on every cell click
        tseldren = self.findChildren(QPushButton)
        if tseldren:
            for tsayld in tseldren:
                self.istatus_bar.removeWidget(tsayld)

        #adding widgets to the status bar
        self.istatus_bar.addWidget(edit_button)
        self.istatus_bar.addWidget(delete_button)


    #creating another function for the table
    def load_data(self):
        kuneksyon = DatabaseConnection().connect()
        # kuneksyon = sqlite3.connect('database.db') #creating a connection to the database file
        resulta_ng_database_teybol = kuneksyon.execute('SELECT * FROM students') #executing the connection from the database
        # and making a
        # database
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

    def edit(self):
        dialog = EditDialog() #another class should be created outside the MainWindow class
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog() #another class should be created outside the MainWindow class
        dialog.exec()

    def about(self):
        dialog = AboutDialog() #this class will be created outside the mainWindow class
        dialog.exec()

class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('About Face!')
        content = """
        Ang app na ito ay hindi ko pa napapagana ng maayos, merong AttributeError: 'NoneType' object has no attribute 'text'
        """
        self.setText(content)


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()  # calling the parent class
        self.setWindowTitle('Update stoodent tata')  # setting the title of the app
        self.setFixedWidth(300)  # distance between widgets (depends on the design)
        self.setFixedHeight(300)  # distance between widgets (depends on the design)

        layout = QVBoxLayout()  # we can use QGridLayout() (depends on desired layout, this is stacked vertically)
        index = main_window.teybol.currentRow()
        student_name = main_window.teybol.item(index,0).text()
        print(student_name)
        self.student_id = main_window.teybol.item(index,0).text()


        #get student name from selected row
        index = main_window.teybol.currentRow()
        print(index)
        print(type(index))
        student_name = main_window.teybol.item(index,1).text() #1 is the Name column in the teybol, then apply the text() method to extract the text
        print(type(student_name))

        # mobile number edit
        mobile_number = main_window.teybol.item(index,2).text()
        print(mobile_number)

        # creating the widgets
        self.stoodent_name = QLineEdit(student_name)
        self.stoodent_name.setPlaceholderText('Type student name here')  # setting a placeholder for student name

        course_name = main_window.teybol.item(index,2).text() #setting a default course name
        self.course_drop_down = QComboBox()  # drop down list widget
        self.course_drop_down.addItems(kunyare_courses)  # adding items from any list
        self.course_drop_down.setCurrentText(course_name)

        self.mobile_num = QLineEdit()  # mobile number widget
        self.mobile_num.setPlaceholderText('Anong cell number mo?')


        submit_mo_na_boton = QPushButton('Register your information')
        submit_mo_na_boton.clicked.connect(self.update_student)  # method is changed to update and will be created in line 150

        # placement of widgets to the layout of app
        layout.addWidget(self.stoodent_name)  # adding the widget, no need to add the rows and columns because we chose the QVBoxLayout(),
        # which is stacked vertically
        layout.addWidget(self.course_drop_down)
        layout.addWidget(self.mobile_num)
        layout.addWidget(submit_mo_na_boton)


        self.setLayout(layout)  # output of the widget layout

    def update_student(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = %s, course = %s, mobile_num = %s WHERE id = %s",
                       self.student_name.text(),
                       self.course_name
                       )


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()  # calling the parent class
        self.setWindowTitle('Delete Record')  # setting the title of the app

        layout = QGridLayout()
        confirmation = QLabel('Are you shure??')
        yes = QPushButton('Yes')
        no = QPushButton('No')

        layout.addWidget(confirmation, 0, 0, 2,2)
        layout.addWidget(yes, 2, 1)
        layout.addWidget(no, 2, 2)

        self.setLayout(layout)

        yes.clicked.connect(self.delete_student)

    def delete_student(self):
        #get selected row index and student id
        index = main_window.teybol.currentRow()
        student_id = main_window.teybol.item(index,0).text()

        connection = DatabaseConnection().connect()
        # connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('DELETE from students WHERE id = ?', (student_id, )) #should include a comma for it to be recognized as the local student_id
        # variable
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()

        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle('Success')
        confirmation_widget.setText('Da rikord was deleted saksespuli')
        confirmation_widget.exec()

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
        database_connection = DatabaseConnection().connect()
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
        button.clicked.connect(self.search) #the search method will be created in line149
        layout.addWidget(button)

        self.setLayout(layout) #to output of the dialog box

    def search(self):
        name = self.student_name.text() #this will get the user input on the search box
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM students WHERE name = ?",(name,))
        rows = list(result)
        print(rows)
        items = main_window.teybol.findItems(name, Qt.MatchFlag.MatchFixedString) #main_window created, MainWindow instance line171, teybol object
        # from line44

        for item in items:
            # print(item)
            # main_window.teybol.item(item.row(),1).setSelected(True)
            print(main_window.teybol.item(item.row(),1).setSelected(True))

        cursor.close()
        connection.close()



# the codes below are for the app to launch
app = QApplication(sys.argv)
main_window = MainWindow()
estudyante_blues = MainWindow()
estudyante_blues.show()
estudyante_blues.load_data() #this method should be called so we can execute the table on the app, without this line of code the table from the
# database will not populate the table
sys.exit(app.exec())

if __name__ == '__main__':
    MainWindow()