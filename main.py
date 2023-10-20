from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget,  QGridLayout, QLineEdit, QPushButton
import sys
import datetime

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__() #To call the init of the parent class, in this code QWidget
        self.setWindowTitle('Wala sa idad yan!!!!') #App Title
        grid = QGridLayout()

        name_label = QLabel('Name:') #name widget
        self.name_line_edit = QLineEdit() #adding self to make the variable accessible to the other functions, we also have to add the self to the addWidget placement

        calculate_button = QPushButton('Calculate Age') #creating a button
        calculate_button.clicked.connect(self.calculate_age) #linking the button to the calculate_age function
        self.output_age_label = QLabel('Dito malalaman and edad mong animal ka') #adding self to make the variable accessible to the other functions,
        # we also have to add the self to
        # the addWidget placement

        date_birth_label = QLabel('Date of birth MM/DD/YYYY') #date of birth widget
        self.date_birth_line_edit = QLineEdit() #adding self to make the variable accessible to the other functions, we also have to add the self
        # to the addWidget placement

        grid.addWidget(name_label, 0, 0) #placement of widget
        grid.addWidget(self.name_line_edit, 0, 1) #placement of widget
        grid.addWidget(date_birth_label, 1, 0) #placement of widget
        grid.addWidget(self.date_birth_line_edit, 1, 1) #placement of widget
        grid.addWidget(calculate_button, 2, 0, 1, 2) #row2, column0, span of 1 row and 2 columns
        grid.addWidget(self.output_age_label, 3,0,1,2) #row3, column0, span of 1 row and 2 columns

        self.setLayout(grid) #Code to output the app

    def calculate_age(self):
        current_year = datetime.datetime.now().year #retrieving the current year
        year_of_birth = self.date_birth_line_edit.text() #added the text method so we can extract the actual value
        birth_year = datetime.datetime.strptime(year_of_birth, "%m/%d/%Y").date().year
        age = current_year - birth_year
        self.output_age_label.setText(f"{self.name_line_edit.text()}'s age is {age} years")

# the codes below are for the app to launch
app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())


if __name__ == '__main__':
    AgeCalculator()