from PySide6.QtWidgets import QMainWindow, QMenu, QTableWidgetItem, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtGui import QAction, QIcon
from ui_index import Ui_MainWindow  # ui_index.py에서 생성된 UI 클래스 임포트

import mysql.connector

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")  

        # Hide Widget Menu
        self.icon_only_widget.setHidden(True)
    
        # Hide Dropdowns
        self.students_dropdown.setHidden(True)
        self.teachers_dropdown.setHidden(True)
        self.finances_dropdown.setHidden(True)
    
        # Connect Buttons to switch to different pages
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)

        self.institution_1.clicked.connect(self.switch_to_institution_page)
        self.institution_2.clicked.connect(self.switch_to_institution_page)

        self.student_info.clicked.connect(self.switch_to_studentInfo_page)
        self.student_payments.clicked.connect(self.switch_to_studentPayments_page)
        self.student_transactions.clicked.connect(self.switch_to_studentTransactions_page)

        self.teacher_info.clicked.connect(self.switch_to_teacherInfo_page)
        self.teacher_salaries.clicked.connect(self.switch_to_teacherSalaries_page)
        self.teacher_transactions.clicked.connect(self.switch_to_teacherTransactions_page)

        self.budgets.clicked.connect(self.switch_to_budgetsInfo_page)
        self.expenses.clicked.connect(self.switch_to_expensesInfo_page)
        self.business_overview.clicked.connect(self.switch_to_businessOverview_page)

        self.settings_1.clicked.connect(self.switch_to_settings_page)
        self.settings_2.clicked.connect(self.switch_to_settings_page)

        # Connect Buttons to respective context menus
        self.students_1.clicked.connect(self.students_context_menu)
        self.teachers_1.clicked.connect(self.teachers_context_menu)
        self.finances_1.clicked.connect(self.finances_context_menu)

        # Connect to mySQL server and create a database if it does not exist
        self.create_connection()

        # Create students table
        self.create_students_table()

        # Load students information to QTable
        self.load_students_info()
        self.select_class.currentIndexChanged.connect(self.reload_Studentstable_data)
        self.select_gender.currentIndexChanged.connect(self.reload_Studentstable_data)
        self.search_student.textChanged.connect(self.search_students)

        # Control column widths
        self.studentInfo_table.setColumnWidth(0, 120)
        self.studentInfo_table.setColumnWidth(1, 80)
        self.studentInfo_table.setColumnWidth(2, 60)
        self.studentInfo_table.setColumnWidth(3, 70)
        self.studentInfo_table.setColumnWidth(4, 70)
        self.studentInfo_table.setColumnWidth(5, 50)
        self.studentInfo_table.setColumnWidth(6, 70)
        self.studentInfo_table.setColumnWidth(7, 80)
        self.studentInfo_table.setColumnWidth(8, 120)
        self.studentInfo_table.setColumnWidth(9, 150)

        # Open add student dialog
        self.addStudent_btn.clicked.connect(self.open_addstudent_dialog)

    # Methods for switch to different pages
    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def switch_to_institution_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_studentInfo_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_studentPayments_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_studentTransactions_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_teacherInfo_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_teacherSalaries_page(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_teacherTransactions_page(self):
        self.stackedWidget.setCurrentIndex(7)

    def switch_to_budgetsInfo_page(self):
        self.stackedWidget.setCurrentIndex(8)

    def switch_to_expensesInfo_page(self):
        self.stackedWidget.setCurrentIndex(9)

    def switch_to_businessOverview_page(self):
        self.stackedWidget.setCurrentIndex(10)

    def switch_to_settings_page(self):
        self.stackedWidget.setCurrentIndex(11)

    # Methods to show context menus
    def students_context_menu(self):
        self.show_custom_context_menu(self.students_1, ["Student Information", "Student Payments", "Student Transactions"])

    def teachers_context_menu(self):
        self.show_custom_context_menu(self.teachers_1, ["Teacher Information", "Teacher Salaries", "Teacher Transactions"])

    def finances_context_menu(self):
        self.show_custom_context_menu(self.finances_1, ["Budgets", "Expenses", "Business Overview"])

    def show_custom_context_menu(self, button, menu_items):

        menu = QMenu()

        # Set style for the menu
        menu.setStyleSheet("""
                           QMenu {
                           background-color: black; 
                           color: white;
                           }
                           
                           QMenu:selected {
                           background-color: white;
                           color: #128298;
                           }
                           """)

        # Add actions to the menu
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        # Show the menu
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):
        
        text = self.sender().text()

        if text == "Student Information":
            self.switch_to_studentInfo_page()
        elif text == "Student Payments":
            self.switch_to_studentPayments_page()
        elif text == "Student Transactions":
            self.switch_to_studentTransactions_page()
        elif text == "Teacher Information":
            self.switch_to_teacherInfo_page()
        elif text == "Teacher Salaries":
            self.switch_to_teacherSalaries_page()
        elif text == "Teacher Transactions":
            self.switch_to_teacherTransactions_page()
        elif text == "Budgets":
            self.switch_to_budgetsInfo_page()
        elif text == "Expenses":
            self.switch_to_expensesInfo_page()
        elif text == "Business Overview":
            self.switch_to_businessOverview_page()

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
    
    # CREATE STUDENTS TABLES
    def create_students_table(self):

        # Create a cursor for executing SQL queries
        cursor = self.create_connection().cursor()

        # The query
        create_students_table_query = f"""
                    CREATE TABLE IF NOT EXISTS students_table(
                        name TEXT,
                        student_id VARCHAR(15) PRIMARY KEY,
                        gender TEXT,
                        class TEXT,
                        birthday TEXT,
                        age INT,
                        address TEXT,
                        phone_number VARCHAR(15),
                        email VARCHAR(15)
                    )"""
        
        cursor.execute(create_students_table_query)

        # Commit the changes and close the connection
        self.mydb.commit()
        self.mydb.close()

    # OPEN DIALOGS FOR INSERTING NEW STUDENT

    def open_addstudent_dialog(self):

        from ui_studentDialog import Ui_StudentsDialog
        
        # Instantiate and show the dialog
        addStudent_Dialog = Ui_StudentsDialog(self)
        result = addStudent_Dialog.exec() # This will block until the dialog is closed

        if result == Ui_StudentsDialog.Accepted:
            # If the dialog was accepted (User clicked add student button)
            self.reload_Studentstable_data()

    def reload_Studentstable_data(self):
        # This method is called to reload the table data
        self.load_students_info()

    # LOAD STUDENTS INFORMATION TO QTABLE

    def load_students_info(self):

        # Clear existing data in the table
        self.studentInfo_table.setRowCount(0)

        # fetch data based on the selected class and gender in the comboboxes
        selected_class = self.select_class.currentText()
        selected_gender = self.select_gender.currentText()
        data = self.get_data_from_table(selected_class, selected_gender)

        # Populate the table with the filtered data
        for row_index, row_data in enumerate(data):
            self.studentInfo_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.studentInfo_table.setItem(row_index, col_index, item)

                # Create a custom widget with two buttons lineed up horizontally for the action column
                double_button_widget = DoubleButtonWidgetStudents(row_index, row_data)

                # Set this custom widget with two buttons lineed up horizontally for the action column
                self.studentInfo_table.setCellWidget(row_index, 9, double_button_widget)
                self.studentInfo_table.setRowHeight(row_index, 50) 

    def get_data_from_table(self, class_filter, gender_filter):

        cursor = self.create_connection().cursor()

        # Construct the SQL query based on the selected filters
        query = f""" SELECT name, student_id, gender, class, birthday, age, address, phone_number, email FROM students_table WHERE 
                ('{class_filter}' = 'SELECT CLASS' OR class = '{class_filter}') AND
                ('{gender_filter}' = 'SELECT GENDER' OR gender = '{gender_filter}') """
        
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def search_students(self):
        
        # Clear previous table results
        self.studentInfo_table.setRowCount(0)

        # Get the search query from the Qlineedit
        search_query = self.search_student.text()

        # Execute the SQL query
        cursor = self.create_connection().cursor()
        sql_query = f""" SELECT name, student_id, gender, class, birthday, age, address, phone_number, email FROM students_table WHERE name LIKE '%{search_query}%' """
        cursor.execute(sql_query)
        results = cursor.fetchall()

        # Populate the table with the filtered data
        for row_index, row_data in enumerate(results):
            self.studentInfo_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.studentInfo_table.setItem(row_index, col_index, item)

                # Create a custom widget with two buttons lineed up horizontally for the action column
                double_button_widget = DoubleButtonWidgetStudents(row_index, row_data)

                # Set this custom widget with two buttons lineed up horizontally for the action column
                self.studentInfo_table.setCellWidget(row_index, 9, double_button_widget)
                self.studentInfo_table.setRowHeight(row_index, 50)


    # DOUBLE BUTTON CLASS

class DoubleButtonWidgetStudents(QWidget):
    def __init__(self, row_index, row_data):
        super().__init__()

        # Store the row index and row data as an instance in variables
        self.row_index = row_index
        self.row_data = row_data

        # Get student variables from the tuple
        self.student_name = self.row_data[0]
        self.student_id = self.row_data[1]

        layout = QHBoxLayout(self)

        # Create blue Edit button
        self.edit_button = QPushButton("", self)
        self.edit_button.setStyleSheet("background-color: blue")
        self.edit_button.setFixedSize(61, 31)

        # Create red Delete button
        self.delete_button = QPushButton("", self)
        self.delete_button.setStyleSheet("background-color: red")
        self.delete_button.setFixedSize(61, 31)

        # Set icons for the buttons
        icon = QIcon("C:\Workspace\School\Icons\edit.png")
        self.edit_button.setIcon(icon)

        icon2 = QIcon("C:\Workspace\School\Icons\delete.png")
        self.delete_button.setIcon(icon2)

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)




