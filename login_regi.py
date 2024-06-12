# import sys
# from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# import json
# import os

# class LoginWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Login")
#         self.setGeometry(100, 100, 300, 200)

#         layout = QVBoxLayout()

#         self.label_id = QLabel("ID:")
#         layout.addWidget(self.label_id)

#         self.input_id = QLineEdit()
#         layout.addWidget(self.input_id)

#         self.label_password = QLabel("Password:")
#         layout.addWidget(self.label_password)

#         self.input_password = QLineEdit()
#         self.input_password.setEchoMode(QLineEdit.Password)
#         layout.addWidget(self.input_password)

#         self.login_button = QPushButton("Login")
#         self.login_button.clicked.connect(self.login)
#         layout.addWidget(self.login_button)

#         self.setLayout(layout)

#         self.load_credentials()

#     def login(self):
#         user_id = self.input_id.text()
#         password = self.input_password.text()

#         if user_id and password:
#             self.save_credentials(user_id, password)
#             QMessageBox.information(self, "Login", "Login Successful")
#         else:
#             QMessageBox.warning(self, "Login", "Please enter both ID and Password")

#     def save_credentials(self, user_id, password):
#         credentials = {"id": user_id, "password": password}
#         with open("credentials.json", "w") as file:
#             json.dump(credentials, file)

#     def load_credentials(self):
#         if os.path.exists("credentials.json"):
#             with open("credentials.json", "r") as file:
#                 credentials = json.load(file)
#                 self.input_id.setText(credentials["id"])
#                 self.input_password.setText(credentials["password"])

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = LoginWindow()
#     window.show()
#     sys.exit(app.exec())



import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from login_regi_ui import Ui_MainWindow

class Login_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Login_Window,self).__init__()
        self.setupUi(self)

        self.setWindowTitle("인터넷등기소")

    def slot_loginid(self):
        pass

    def slot_loginpw(self):
        pass

    def slot_autologin(self):
        pass

    def slot_login(self):
        pass

    def slot_membership(self):
        pass

    def slot_idpw_find(self):
        pass
    


app = QApplication(sys.argv)

window = Login_Window()
window.show()

app.exec()