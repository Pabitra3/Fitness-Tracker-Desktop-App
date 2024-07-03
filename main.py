#Imports
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox, QLineEdit, QDateEdit
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
#
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#
import numpy as np  
from sys import exit


# Main Class
class FitTrack(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
    
    # Settings
    def settings(self):
        self.setWindowTitle("FitTrack")
        self.resize(800,600)
    
    # Init UI
    def initUI(self):
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())

        self.kal_box = QLineEdit()
        self.kal_box.setPlaceholderText("Number of Burned Calories")
        self.distance_box = QLineEdit()
        self.distance_box.setPlaceholderText("Enter distane run")
        self.description = QLineEdit()
        self.description.setPlaceholderText("Enter a description")

        self.submit_btn = QPushButton("Submit")
        self.add_btn = QPushButton("Add")
        self.delete_btn = QPushButton("Delete")
        self.clear_btn = QPushButton("Clear")
        self.dark_mode = QPushButton("Dark Mode")

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Id","Date","Calories","Distance","Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        # Design Our Layout
        self.master_layout = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()

        self.sub_row1 = QHBoxLayout()
        self.sub_row2 = QHBoxLayout()
        self.sub_row3 = QHBoxLayout()
        self.sub_row4 = QHBoxLayout()

        self.sub_row1.addWidget(QLabel("Date:"))
        self.sub_row1.addWidget(self.date_box)
        self.sub_row2.addWidget(QLabel("Calories:"))
        self.sub_row2.addWidget(self.kal_box)
        self.sub_row3.addWidget(QLabel("KM:"))
        self.sub_row3.addWidget(self.distance_box)
        self.sub_row4.addWidget(QLabel("Description:"))
        self.sub_row4.addWidget(self.description)
        
        self.col1.addLayout(self.sub_row1)
        self.col1.addLayout(self.sub_row2)
        self.col1.addLayout(self.sub_row3)
        self.col1.addLayout(self.sub_row4)
        self.col1.addWidget(self.dark_mode)


        btn_row1 = QHBoxLayout()
        btn_row2 = QHBoxLayout()

        btn_row1.addWidget(self.add_btn)
        btn_row1.addWidget(self.delete_btn)
        btn_row2.addWidget(self.submit_btn)
        btn_row2.addWidget(self.clear_btn)

        self.col1.addLayout(btn_row1)
        self.col1.addLayout(btn_row2)


        self.col2.addWidget(self.canvas)
        self.col2.addWidget(self.table)

        

        self.master_layout.addLayout(self.col1, 30)
        self.master_layout.addLayout(self.col2, 70)
        self.setLayout(self.master_layout)
    
    # Load Tables

    # Add Tables

    # Delete Tables

    # Calculate Calories

    # Click

    # Dark Mode

    # Reset


# Initialize my DB
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("fitness.db")

if not db.open():
    QMessageBox.critical(None,"ERROR","Can not open the Database")
    exit(2)

query = QSqlQuery()
query.exec_("""
           CREATE TABLE IF NOT EXISTS fitness {
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                calories REAL,
                distance REAL,
                description TEXT
            }
            """)


if __name__ == "__main__":
    app = QApplication([])
    main = FitTrack()
    main.show()
    app.exec_()
