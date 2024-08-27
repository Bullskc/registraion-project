from PySide6.QtWidgets import QMainWindow, QMenu, QTableWidgetItem, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QFileDialog
from PySide6.QtGui import QAction, QIcon
from ui_index import Ui_MainWindow  # ui_index.py에서 생성된 UI 클래스 임포트

import mysql.connector
from UpdateStudentDialog import UpdateStudentDialog
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# import os
# import subprocess

# def system_call(args, cwd="."):
#     print("Running '{}' in '{}'".format(str(args), cwd))
#     subprocess.call(args, cwd=cwd)
#     pass

# def fix_image_files(root=os.curdir):
#     for path, dirs, files in os.walk(os.path.abspath(root)):
#         # sys.stdout.write('.')
#         for dir in dirs:
#             system_call("mogrify *.png", "{}".format(os.path.join(path, dir)))


# fix_image_files(os.curdir)


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

        # Connect to mySQL server and create a database if it doent exist
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

        # Excel Export
        self.excelExport_btn.clicked.connect(self.export_to_excel_studentsTable)

        # PDF Export
        self.pdfExport_btn.clicked.connect(self.export_to_pdf_studentsTable)

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
        database_name = "my_school"

        # Establish a connection to MySQL server
        self.mydb  = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=mypassword,
        )
        
        # Create a cursor to execute SQL queries
        cursor = self.mydb.cursor()

        # Create the database if it does not exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

        # Connect to the created database
        self.mydb = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = mypassword,
            database = database_name
        )

        return self.mydb
    
    # CREATE STUDENTS TABLES
    def create_students_table(self):

        # Create a cursor for executing SQL queries
        cursor = self.create_connection().cursor()

        # The query
        create_students_table_query = f"""
                    CREATE TABLE IF NOT EXISTS students_table(
                        names TEXT,
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

        from StudentDialog import Ui_StudentsDialog
        
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
                double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)

                # Set this custom widget with two buttons lineed up horizontally for the action column
                self.studentInfo_table.setCellWidget(row_index, 9, double_button_widget)
                self.studentInfo_table.setRowHeight(row_index, 50) 

    def get_data_from_table(self, class_filter, gender_filter):

        cursor = self.create_connection().cursor()

        # Construct the SQL query based on the selected filters
        query = f""" SELECT names, student_id, gender, class, birthday, age, address, phone_number, email FROM students_table WHERE 
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
        sql_query = f""" SELECT names, student_id, gender, class, birthday, age, address, phone_number, email FROM students_table WHERE
                names LIKE '%{search_query}%' """
        cursor.execute(sql_query)
        results = cursor.fetchall()

        # Populate the table with the filtered data
        for row_index, row_data in enumerate(results):
            self.studentInfo_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.studentInfo_table.setItem(row_index, col_index, item)

                # Create a custom widget with two buttons lineed up horizontally for the action column
                double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)

                # Set this custom widget with two buttons lineed up horizontally for the action column
                self.studentInfo_table.setCellWidget(row_index, 9, double_button_widget)
                self.studentInfo_table.setRowHeight(row_index, 50)

    # EXCEL EXPORT

    def export_to_excel_studentsTable(self):

        # Convert QTableWidget to pandas Dataframe
        data = []

        self.headers = [self.studentInfo_table.horizontalHeaderItem(col).text() for col in range(self.studentInfo_table.columnCount())]

        for row in range(self.studentInfo_table.rowCount()):
            # Check if the item is not None before accessing its text
            row_data = [self.studentInfo_table.item(row, col).text() if self.studentInfo_table.item(row, col) is not None else "" for col in range(self.studentInfo_table.columnCount())]
            data.append(row_data)

        # Create a pandas DataFrame with the collected data and the headers
        df = pd.DataFrame(data, columns=self.headers)

        # Save the DataFrame to excel file
        # Exclude the last column before exporting
        df_filtered = df.iloc[:, :-1]

        # Open QFileDialog to get the file path
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save Excel File", "", "Excel files (*.xlsx);;All files (*)")

        if file_path:
            # Save filtered DataFrame to excel file at the chosen path
            df_filtered.to_excel(file_path, index=False)
            print(f"Table exported to {file_path}")

    # PDF EXPORT

    def export_to_pdf_studentsTable(self):

        # Open QFileDialog to get the file path
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save PDF File", "", "PDF files (*.pdf);;All files (*)")

        if file_path:
            # Create a PDF document
            pdf_document = SimpleDocTemplate(file_path, pagesize=letter)

            # Assuming n is the total number of columns in your QTable Widget
            n = self.studentInfo_table.columnCount()

            # Extract the headers from the QTableWidget
            headers = [self.studentInfo_table.horizontalHeaderItem(col).text() for col in range(n-1)]

            # Extract data from the QTableWidget, excluding the last column
            data = [headers]

            for row in range(self.studentInfo_table.rowCount()):
                row_data = [self.studentInfo_table.item(row, col).text() if self.studentInfo_table.item(row, col) is not None else "" for col in range(n-1)]
                data.append(row_data)

            # Create a PDF table
            pdf_table = Table(data)

            # Apply styles to the table
            style = TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 8),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])

            pdf_table.setStyle(style)

            # Build the PDF document
            pdf_document.build([pdf_table])

            print(f"Table exported to {file_path}")


    # DOUBLE BUTTON CLASS

class DoubleButtonWidgetStudents(QWidget):
    def __init__(self, row_index, row_data, sideBar):
        super().__init__()

        # Store the row index and row data as an instance in variables
        self.row_index = row_index
        self.row_data = row_data
        self.sidebar = sideBar # Store a reference to MySideBar

        # Get student variables from the tuple
        self.student_name = self.row_data[0]
        self.student_id = self.row_data[1]

        layout = QHBoxLayout(self)

        # Create blue Edit button
        self.edit_button = QPushButton("", self)
        self.edit_button.setStyleSheet("background-color: blue")
        self.edit_button.setFixedSize(61, 31)
        self.edit_button.clicked.connect(self.edit_clicked)

        # Create red Delete button
        self.delete_button = QPushButton("", self)
        self.delete_button.setStyleSheet("background-color: red")
        self.delete_button.setFixedSize(61, 31)
        self.delete_button.clicked.connect(self.delete_clicked)

        # Set icons for the buttons
        icon = QIcon(r"C:\Workspace\registraion-project_git\School\Icons\edit.png")
        self.edit_button.setIcon(icon)

        icon2 = QIcon(r"C:\Workspace\registraion-project_git\School\Icons\delete.png")
        self.delete_button.setIcon(icon2)

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

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
    
    def edit_clicked(self):
        # Create an instance of UpdateStudent Dialog
        self.update_dialog = UpdateStudentDialog(self.row_index, self.row_data)

        # Connect the custom signal to reload_Studentstable_data slot in MySideBar
        self.update_dialog.data_updated.connect(self.sidebar.reload_Studentstable_data)

        # Execute the dialog
        self.update_dialog.exec()

    def delete_clicked(self):
        
        cursor = self.create_connection().cursor()

        # Create a confirmation dialog
        message = QMessageBox.question(
            self, 'Confirmation',
            "Are you sure you want to delete " + self.student_name + "?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if message == QMessageBox.StandardButton.Yes:
            # Delete the row from the students_table

            delete_query = "DELETE FROM students_table WHERE student_id = %s"
            cursor.execute(delete_query, (self.student_id,))
            self.mydb.commit()
            self.mydb.close()

            # Emit a signal to inform about the change
            self.sidebar.reload_Studentstable_data()



