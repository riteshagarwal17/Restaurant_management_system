from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import conections
import datetime
from utilities import *
import sys

class signup(QWidget):
    def __init__(self):
        super(signup, self).__init__()
        self.prepareScreen()

    def prepareScreen(self):
        self.setWindowTitle(" Please Sign Up")

        newfont = QFont("Consolas", 18, QFont.Bold)
        lbl1 = QLabel('Enter UserName : ')
        lbl2 = QLabel('Enter Password : ')
        lbl3 = QLabel("Role Name:")

        self.labl1Edit = QLineEdit()
        self.labl2Edit = QLineEdit()
        self.labl3Edit = QLineEdit()

        self.btn = QPushButton("Sign Up")
        #lblcourse.setFont(newfont)
        lbl1.setFont(newfont)
        lbl2.setFont(newfont)
        lbl3.setFont(newfont)
        self.labl1Edit.setFont(newfont)
        self.labl2Edit.setFont(newfont)
        self.labl2Edit.setEchoMode(QLineEdit.Password)
        self.labl3Edit.setFont(newfont)
        self.btn.setFont(newfont)

        #prepare the Layout
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(lbl1, 3, 0)
        grid.addWidget(self.labl1Edit, 3, 1, 1, 3)
        grid.addWidget(lbl2, 5, 0)
        grid.addWidget(self.labl2Edit, 5, 1, 1, 3)
        grid.addWidget(lbl3, 7, 0)
        grid.addWidget(self.labl3Edit, 7, 1, 1, 3)


        grid.addWidget(self.btn,9, 0, 1, 4)
        self.setLayout(grid)
        self.show()
        try:
            self.btn.clicked.connect(self.adddetails)
        except BaseException as ex:
            print(ex)

    def adddetails(self):
        try:
            id = self.labl1Edit.text()
            pswd=self.labl2Edit.text()
            role=self.labl3Edit.text()
            result = ""
            allvalid=True
            if isEmpty(id):
                result += "Please Fill Some value in id Box\n\n"
                allvalid = False
            elif isNumber(id):
                result += "Please Fill Number in id Box\n\n"
                allvalid = False

            if isEmpty(pswd):
                result += "Please Fill Number in password Box\n\n"
                allvalid = False
            if isEmpty(role):
                result += "Please Fill Number in password Box\n\n"
                allvalid = False
            if (allvalid == True) :
                table_name = "signupinfo"
                column_values = dict()
                value2=datetime.datetime.now()
                column_values["UserName"] = id
                column_values["Password"] = pswd
                column_values["RoleName"] = role
                column_values["signupdatetime"] = str(value2)

                con = conections.Connection()
                print(22)
                query = con.createInsertQuery(table_name, column_values)
                print(21)
                if con.insertQuery(query):
                    result = "SignUp Information is Saved in Database"
                else:
                    result = "Insertion Failure  Due To : " + con.getErrorMessage()
            else:
                pass
            showMessageDialog(self, result)
        except BaseException as ex:
            print(ex)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = signup()
    sys.exit(app.exec_())
