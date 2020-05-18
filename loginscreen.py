import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import conections
import mainscreen
import billscreen
from utilities import *
import datetime
import os


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        self.setGeometry(100,100,800,800)
        newfont = QFont("Consolas", 22, QFont.Bold)
        self.setWindowTitle(" Login Screen ")
        self.layout = QGridLayout()
        lbl1 = QLabel(" Enter User Name : ")
        lbl2 = QLabel(" Enter User Password : ")
        self.et_username = QLineEdit()
        self.et_password = QLineEdit()
        self.et_password.setEchoMode(QLineEdit.Password)
        self.btn = QPushButton(" Click To Login ")
        lbl1.setFont(newfont)
        lbl2.setFont(newfont)
        self.et_username.setFont(newfont)
        self.et_password.setFont(newfont)
        self.btn.setFont(newfont)
        self.layout.addWidget(lbl1,0,0)
        self.layout.addWidget(self.et_username, 0, 1)
        self.layout.addWidget(lbl2, 1, 0)
        self.layout.addWidget(self.et_password, 1, 1)
        self.layout.addWidget(self.btn,2,0,1,2)
        image = QImage(os.path.abspath("pic10.jpg"))
        sImage = image.scaled(QSize(800, 800))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.setLayout(self.layout)
        self.show()
        self.btn.clicked.connect(self.checkLogin)

    def checkLogin(self):
        try:
            allvalid = True
            message = ""
            user_name = self.et_username.text()
            password = self.et_password.text()
            if len(user_name) == 0:
                message += "Please Enter Some Value in User Name Box\n\n"
                allvalid = False
            if len(password) == 0:
                message += "Please Enter Some Value in User Password Box\n\n"
                allvalid = False
            if allvalid:
                conn = conections.Connection()
                query = "select UserName,Password,RoleName "
                query += " from signupinfo where UserName='" + user_name + "'"
                cursor = conn.executeQuery(query)
                if len(cursor)==0:
                    allvalid = False
                    message = "Wrong UserName"
                    showMessageDialog(self, message)
                elif cursor is not None:
                    for record in cursor:
                        value3=record[0]
                else:
                    allvalid = False
                    message = "Sorry,No Record"
                    showMessageDialog(self, message)

                if record is not None:
                    if record[1] == password:
                        if record[2] == "admin":
                            self.window = mainscreen.main()
                            self.window.show()
                            message = "Valid User Name and Password "
                        if record[2] == "manager":
                            self.window = billscreen.billcounter()
                            self.window.show()
                            message = "Valid User Name and Password "
                        else:
                            allvalid = False
                            message = "Unauthorized Access"
                    else:
                        allvalid = False
                        message = "User Name and password does not match"
                else:
                    allvalid = False
                    message = "Invalid User Name Given"
                table_name = "logininfo"
                column_values = dict()
                value2 = datetime.datetime.now()
                column_values["UserName"] = user_name
                column_values["Password"] = password
                column_values["RoleName"] = record[2]
                column_values["LastLogin"] = str(value2)

                con = conections.Connection()
                query = con.createInsertQuery(table_name, column_values)
                if con.insertQuery(query):
                    message = "Login Information is Saved in Database"
                else:
                    message = "Insertion Failure  Due To : " + con.getErrorMessage()

            showMessageDialog(self, message)
        except BaseException as ex:
            print("Unexpected error:", ex)
        if allvalid:
            self.close()
            #self.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginScreen()
    sys.exit(app.exec_())
