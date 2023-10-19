from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget,               QGridLayout, QLineEdit
import sys

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__() #To call the init of the parent class, in this code QWidget
        grid = QGridLayout()

        name_label = QLabel('Name:') #name widget
        name_line_edit = QLineEdit()

        date_birth_label = QLabel('Date of birth MM/DD/YYYY') #date of birth widget
        date_birth_line_edit = QLineEdit()

        grid.addWidget(name_label, 0, 0) #placement of widget
        grid.addWidget(name_line_edit, 0, 1) #placement of widget
        grid.addWidget(date_birth_label, 1, 0) #placement of widget
        grid.addWidget(date_birth_line_edit, 1, 1) #placement of widget

        self.setLayout(grid) #Code to output the app

app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())

if __name__ == '__main__':
    AgeCalculator()