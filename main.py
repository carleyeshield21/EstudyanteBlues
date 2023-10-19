from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget,               QGridLayout, QLineEdit

class AgeCalculator(QWidget):
    def __init__(self):
        grid = QGridLayout()

        name_label = QLabel('Name:')
        name_line_edit = QLineEdit()

        name_label = QLabel('Date of birth MM/DD/YYYY')
        date_birth_line_edit = QLineEdit()




if __name__ == '__main__':
    AgeCalculator()