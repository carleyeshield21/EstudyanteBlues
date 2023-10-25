from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QLabel, QWidget,  QGridLayout, QLineEdit, QPushButton, QMainWindow, QTableWidget,
                             QTableWidgetItem, QDialog, QComboBox, QToolBar, QStatusBar)
import sys
import sqlite3
def on_combobox_selection(index):
    selected_text = my_combo_box.itemText(index)
    print(f"Selected item: {selected_text}")

# course_name = main_window.teybol.item(index,2).text()
app = QApplication(sys.argv)
window = QMainWindow()
window.setGeometry(100, 100, 400, 200)

my_combo_box = QComboBox(window)
my_combo_box.addItem("Option 1")
my_combo_box.addItem("Option 2")
my_combo_box.addItem("Option 3")
my_combo_box.currentIndexChanged.connect(on_combobox_selection)

window.show()
sys.exit(app.exec())