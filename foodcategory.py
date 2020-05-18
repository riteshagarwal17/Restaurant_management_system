from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import conections
import datetime
from utilities import *
import sys
import os

class AddFoodCategory(QWidget):
    def __init__(self):
        super(AddFoodCategory, self).__init__()
        self.prepareScreen()

    def prepareScreen(self):
        self.setWindowTitle(" Assign Categories To Different Types Of Food ")
        self.setGeometry(100, 100, 1050, 750)

        image = QImage(os.path.abspath("pic7.jpg"))
        sImage = image.scaled(QSize(2000, 1200))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        # Initialize the widgets
        #self.course_records = list()
        #self.student_records = list()
        newfont = QFont("Consolas", 24, QFont.Bold)
        lbl1 = QLabel('Enter Food Category ID : ')
        lbl2 = QLabel('Enter Food Category Name : ')

        self.labl1Edit = QLineEdit()
        self.labl2Edit = QLineEdit()

        self.btn = QPushButton("Assign Category To Food")
        #lblcourse.setFont(newfont)
        lbl1.setFont(newfont)
        lbl2.setFont(newfont)
        self.labl1Edit.setFont(newfont)
        self.labl2Edit.setFont(newfont)
        self.btn.setFont(newfont)

        #prepare the Layout
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(lbl1, 3, 0)
        grid.addWidget(self.labl1Edit, 3, 1, 1, 3)
        grid.addWidget(lbl2, 5, 0)
        grid.addWidget(self.labl2Edit, 5, 1, 1, 3)


        grid.addWidget(self.btn,7, 0, 1, 4)
        self.setLayout(grid)
        self.show()
        try:
            self.btn.clicked.connect(self.adddetails)
        except BaseException as ex:
            print(ex)

    def adddetails(self):
        try:
            id = self.labl1Edit.text()
            name=self.labl2Edit.text()

            result = ""
            allvalid=True
            if isEmpty(id):
                result += "Please Fill Some value in id Box\n\n"
                allvalid = False
            elif not isNumber(id):
                result += "Please Fill Number in id Box\n\n"
                allvalid = False

            if isEmpty(name):
                result += "Please Fill Number in name Box\n\n"
                allvalid = False
            print(11)
            if (allvalid == True) :
                table_name = "foodcategory"
                print(23)
                column_values = dict()
                column_values["CategoryID"] = id
                column_values["CategoryName"] = name
                con = conections.Connection()
                print(22)
                query = con.createInsertQuery(table_name, column_values)
                print(21)
                if con.insertQuery(query):
                    result = "Food  Information is Saved in Database"
                else:
                    result = "Insertion Failure  Due To : " + con.getErrorMessage()
            else:
                print(34)
            showMessageDialog(self, result)
        except BaseException as ex:
            print(ex)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddFoodCategory()
    sys.exit(app.exec_())
