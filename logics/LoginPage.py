import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from Pyqt5.uic import loadUi
import sqlite3

conn = sqlite3.connect("../database/users.sqlite")
cursor = conn.cursor()

#TODO decorate connection and closing function



def check_password(username, password):
    cursor.execute(f"SELECT user,password FROM Users WHERE user={username} AND password={password}")
    flag = cursor.fetchone()
    if len(flag) == 0:
        return False
    return True


def switch_to_main_window(username):
    pass
    # TODO write switching function


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("../design/LoginPage.ui", self)
        self.setWindowTitle("Login Form")
        self.Login_button.clicked.connect(self.login)
        self.username_label.setAlignment(Qt.AlignCenter)
        self.pwd_label.setAlignment(Qt.AlignCenter)
        self.username = self.username_field.text()
        self.password = self.password_field.text()
    def add_new_user(self,username, password):
        cursor.execute("INSERT INTO Users (user, password) VALUES (?, ?)", (username, password))
    def login(self):
        cursor.execute("SELECT * FROM Users WHERE user=?", (self.username,))
        user = cursor.fetchone()
        if user is not None:
            if not check_password(self.username, self.password):
                self.setWindowTitle("incorrect password")
            else:
                switch_to_main_window(self.username)
        else:
            self.add_new_user(self.username, self.password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec_())
