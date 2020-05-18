from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import conections
import datetime
from utilities import *
import sys

class AddFoodSubCategory(QWidget):
    def __init__(self):
        super(AddFoodSubCategory, self).__init__()
        self.prepareScreen()

    def prepareScreen(self):
        self.setWindowTitle(" Assign Sub Categories To Different Types Of Categories Of Food ")

        # Initialize the widgets
        #self.course_records = list()
        #self.student_records = list()
        newfont = QFont("Consolas", 18, QFont.Bold)
        lbl1 = QLabel('Enter Food Sub Category Name : ')
        lbl2 = QLabel('Choose Food Category ID : ')
        self.combocategoryid = QComboBox()
        self.combocategoryid.addItem("Choose Food Category")
        self.labl1Edit = QLineEdit()

        self.btn = QPushButton("Assign Sub Category To Food")
        #lblcourse.setFont(newfont)
        lbl1.setFont(newfont)
        lbl2.setFont(newfont)
        self.combocategoryid.setFont(newfont)
        self.labl1Edit.setFont(newfont)
        self.btn.setFont(newfont)

        #prepare the Layout
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(lbl1, 3, 0)
        grid.addWidget(self.labl1Edit, 3, 1, 1, 3)
        grid.addWidget(lbl2, 5, 0)
        grid.addWidget(self.combocategoryid, 5, 1, 1, 3)


        grid.addWidget(self.btn,7, 0, 1, 4)
        self.setLayout(grid)
        self.show()
        self.btn.clicked.connect(self.adddetails)
        self.prepareComboData()
    def prepareComboData(self):
        con = conections.Connection()
        query = "select * from foodcategory"
        self.food_records = con.executeQuery(query)
        #print(self.food_records)
        if len(self.food_records) > 0:
            for record in self.food_records:
                value = record[0]
                self.combocategoryid.addItem(value)

    def adddetails(self):
        try:
            name = self.labl1Edit.text()
            categoryid = ""
            if "Choose" not in self.combocategoryid.currentText():
                index = self.combocategoryid.currentIndex()
                record = self.food_records[index - 1]
                categoryid = record[0]
            result = ""
            allvalid=True
            if isEmpty(name):
                result += "Please Fill Some value in Name Box\n\n"
                allvalid = False
            elif isNumber(name):
                result += "Please Fill Name in Name Box\n\n"
                allvalid = False

            if isEmpty(categoryid):
                result += "Please Choose Any FoodCategory\n\n"
                allvalid = False
            print(11)
            if (allvalid == True) :
                table_name = "foodsubcategory"
                print(23)
                column_values = dict()
                column_values["SubCategoryname"] = name
                column_values["CategoryID"] = categoryid
                con = conections.Connection()
                print(22)
                query = con.createInsertQuery(table_name, column_values)
                print(21)
                if con.insertQuery(query):
                    result = "Food Subcategory Information is Saved in Database"
                else:
                    result = "Insertion Failure  Due To : " + con.getErrorMessage()
            else:
                print(34)
            showMessageDialog(self, result)
        except BaseException as ex:
            print(ex)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddFoodSubCategory()
    sys.exit(app.exec_())
