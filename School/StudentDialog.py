# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentDialogQYggaH.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget, QMessageBox)

import mysql.connector
from random import randint
from datetime import datetime


class Ui_StudentsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(548, 584)
        font = QFont()
        font.setBold(True)
        self.setFont(font)
        self.setStyleSheet(u"QDialog{\n"
"	background-color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border:1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"	height:35px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"	border:1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"	height:31px;\n"
"}\n"
"\n"
"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius: 8px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color : white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(7, 50, 541, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 5, 261, 41))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Heavy"])
        font1.setPointSize(20)
        font1.setBold(False)
        self.label.setFont(font1)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 80, 521, 411))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_2.setFont(font2)

        self.verticalLayout.addWidget(self.label_2)

        self.name_lineEdit = QLineEdit(self.layoutWidget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 35))
        self.name_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.name_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.layoutWidget)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")

        self.verticalLayout_5.addWidget(self.gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_7)

        self.class_comboBox = QComboBox(self.layoutWidget)
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.setObjectName(u"class_comboBox")

        self.verticalLayout_6.addWidget(self.class_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_8)

        self.dob_dateEdit = QDateEdit(self.layoutWidget)
        self.dob_dateEdit.setObjectName(u"dob_dateEdit")
        self.dob_dateEdit.setFont(font)

        self.verticalLayout_7.addWidget(self.dob_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3)

        self.address_lineEdit = QLineEdit(self.layoutWidget)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.address_lineEdit.setMinimumSize(QSize(0, 35))
        self.address_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.address_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_4)

        self.phone_lineEdit = QLineEdit(self.layoutWidget)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.phone_lineEdit.setMinimumSize(QSize(0, 35))
        self.phone_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.phone_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_5)

        self.email_lineEdit = QLineEdit(self.layoutWidget)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 35))
        self.email_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.email_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(300, 510, 241, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saveStudent_btn = QPushButton(self.layoutWidget1)
        self.saveStudent_btn.setObjectName(u"saveStudent_btn")
        self.saveStudent_btn.setMinimumSize(QSize(0, 41))
        self.saveStudent_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:#34D481;\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.saveStudent_btn)

        self.cancel_btn = QPushButton(self.layoutWidget1)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(0, 41))
        self.cancel_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:#585858;\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.cancel_btn)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, StudentsDialog):
        StudentsDialog.setWindowTitle(QCoreApplication.translate("StudentsDialog", u"Students Dialog", None))
        self.label.setText(QCoreApplication.translate("StudentsDialog", u"Add New Student", None))
        self.label_2.setText(QCoreApplication.translate("StudentsDialog", u"Full Name", None))
        self.label_6.setText(QCoreApplication.translate("StudentsDialog", u"Select Gender", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("StudentsDialog", u"Select Class", None))
        self.class_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Grade 1", None))
        self.class_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Grade 2", None))
        self.class_comboBox.setItemText(2, QCoreApplication.translate("StudentsDialog", u"Grade 3", None))
        self.class_comboBox.setItemText(3, QCoreApplication.translate("StudentsDialog", u"Grade 4", None))
        self.class_comboBox.setItemText(4, QCoreApplication.translate("StudentsDialog", u"Grade 5", None))
        self.class_comboBox.setItemText(5, QCoreApplication.translate("StudentsDialog", u"Grade 6", None))
        self.class_comboBox.setItemText(6, QCoreApplication.translate("StudentsDialog", u"Grade 7", None))
        self.class_comboBox.setItemText(7, QCoreApplication.translate("StudentsDialog", u"Grade 8", None))
        self.class_comboBox.setItemText(8, QCoreApplication.translate("StudentsDialog", u"Grade 9", None))
        self.class_comboBox.setItemText(9, QCoreApplication.translate("StudentsDialog", u"Grade 10", None))
        self.class_comboBox.setItemText(10, QCoreApplication.translate("StudentsDialog", u"Grade 11", None))
        self.class_comboBox.setItemText(11, QCoreApplication.translate("StudentsDialog", u"Grade 12", None))

        self.label_8.setText(QCoreApplication.translate("StudentsDialog", u"Date Of Birth", None))
        self.label_3.setText(QCoreApplication.translate("StudentsDialog", u"Address", None))
        self.label_4.setText(QCoreApplication.translate("StudentsDialog", u"Phone Number", None))
        self.label_5.setText(QCoreApplication.translate("StudentsDialog", u"Email", None))
        self.saveStudent_btn.setText(QCoreApplication.translate("StudentsDialog", u"Add Student", None))
        self.cancel_btn.setText(QCoreApplication.translate("StudentsDialog", u"Cancel", None))
    # retranslateUi

    # Add new pupil when you press a button
        self.saveStudent_btn.clicked.connect(self.add_student)
        self.cancel_btn.clicked.connect(self.close)

    # CREATE DATABASE CONNECTION

    def create_connection(self):

        # Replace these with your actual MySQL server details
        host_name = "localhost"
        user_name = "root"
        mypassword = "shin5082@12"
        datebase_name = "my_school"

        # Establish a connection to MySQL server
        self.mydb  = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=mypassword,
        )
        
        # Create a cursor to execute SQL queries
        cursor = self.mydb.cursor()

        # Create the database if it does not exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {datebase_name}")

        # Connect to the created database
        self.mydb = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=mypassword,
            database=datebase_name
        )

        return self.mydb
    
    # INSERT NEW STUDENT

    def insert_new_student(self):

        try:
            connection = self.create_connection()
            if connection is not None:
                return
            
            cursor = connection().cursor()

            gender = self.gender_comboBox.currentText()
            student_id = self.generate_studentId(gender)

            birthday = self.handleDateChange()

            # Assuming birthday is a QDate object
            birth_date = self.dob_dateEdit.date()
            age = self.calculate_age(birth_date)

            # Create list of student information
            self.new_stdent = [
                self.name_lineEdit.text(),
                student_id,
                self.gender_comboBox.currentText(),
                self.class_comboBox.currentText(),
                birthday,
                age,
                self.address_lineEdit.text(),
                self.phone_lineEdit.text(),
                self.email_lineEdit.text()
            ]

            # to insert multiple rows in the database
            insert_student_query = f""" INSERT INTO students_table (names, student_id, gender, class, birthday, age, address, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            cursor.execute(insert_student_query, self.new_stdent)
            self.show_inserted_message()
            connection.commit()
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            # Handle MySQL errors
            print(f"Error: {err}")

    def generate_studentId(self, gender):

        cursor = self.create_connection().cursor()

        while True:
            if gender == "Male":
                id_start_value = "24" + '/U/M'

            else:
                id_start_value = "24" + '/U/F'

            random_value = self.generate_ramdomNumber()
            student_id = id_start_value + random_value

            # Check if the generated student id is already in the table
            cursor.execute(f"SELECT student_id FROM students_table WHERE student_id = %s", (student_id,))
            existing_id = cursor.fetchone()

            if not existing_id:
                return student_id

    def generate_ramdomNumber(self):

        number = randint(1, 9999)
        random_number = f"{number:04d}"
        return random_number
    
    def handleDateChange(self):

        # Convert QDate to a string in the format 'YYYY-MM-DD'
        selected_date = self.dob_dateEdit.date()
        self.date_string = selected_date.toString(Qt.ISODate)

        return self.date_string
    
    def calculate_age(self, birth_date):

        # Get the current date
        current_date = datetime.now().date()

        # Create a date object for the birthdate
        birth_datetime = datetime(birth_date.year(), birth_date.month(), birth_date.day()).date()

        # Calculate the difference in years
        age = current_date.year - birth_datetime.year

        # Check if the birthday has occurred this year
        if (current_date.month, current_date.day) < (birth_datetime.month, birth_datetime.day):
            age -= 1

        return age
    
    def show_inserted_message(self):

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Success")
        msg_box.setText(self.name_lineEdit.text() + " inserted into the database")
        msg_box.exec()

    def add_student(self):
        self.insert_new_student()
        self.accept()

        

