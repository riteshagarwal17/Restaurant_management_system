from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import conections
import datetime
from utilities import *
import sys

class AddFoodInfo(QWidget):
    def __init__(self):
        super(AddFoodInfo, self).__init__()
        self.prepareScreen()

    def prepareScreen(self):
        self.setWindowTitle(" Assign Information To Different Types Of Food ")

        # Initialize the widgets
        #self.course_records = list()
        #self.student_records = list()
        newfont = QFont("Consolas", 18, QFont.Bold)
        lbl1 = QLabel('Enter Food Name : ')
        lbl2 = QLabel('Enter Food Price: ')
        lbl3 = QLabel('Enter Food Desc: ')
        lbl4 = QLabel('Enter Bonus Points: ')
        lbl5=QLabel("Food Sub Category:")
        self.combo1=QComboBox()
        self.labl1Edit = QLineEdit()
        self.labl2Edit = QLineEdit()
        self.labl3Edit = QLineEdit()
        self.labl4Edit = QLineEdit()

        self.btn = QPushButton("Assign Information To Food")
        #lblcourse.setFont(newfont)
        lbl1.setFont(newfont)
        lbl2.setFont(newfont)
        lbl2.setFont(newfont)
        lbl3.setFont(newfont)
        lbl4.setFont(newfont)
        lbl5.setFont(newfont)
        self.combo1.setFont(newfont)
        self.labl1Edit.setFont(newfont)
        self.labl2Edit.setFont(newfont)
        self.labl3Edit.setFont(newfont)
        self.labl4Edit.setFont(newfont)
        self.btn.setFont(newfont)

        #prepare the Layout
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.combo1,1,1,1,2)
        grid.addWidget(lbl1, 3, 0)
        grid.addWidget(lbl2, 4, 0)
        grid.addWidget(lbl3, 5, 0)
        grid.addWidget(lbl4, 6, 0)
        grid.addWidget(lbl5,1,0)

        grid.addWidget(self.labl1Edit, 3, 1, 1, 3)
        grid.addWidget(self.labl2Edit, 4, 1, 1, 3)
        grid.addWidget(self.labl3Edit, 5, 1, 1, 3)
        grid.addWidget(self.labl4Edit, 6, 1, 1, 3)

        grid.addWidget(self.btn,7, 0, 1, 4)
        self.btn.clicked.connect(self.adddetails)
        self.preparecombodata()
        self.setLayout(grid)
        self.show()

    def adddetails(self):
        try:
            subcatname=self.combo1.currentText()
            name = self.labl1Edit.text()
            price=self.labl2Edit.text()
            desc=self.labl3Edit.text()
            bonus=self.labl4Edit.text()
            result = ""
            allvalid = True
            if "chose" in subcatname:
                result+="Please Select Sub Category ID"
                allvalid = False
            if isEmpty(desc):
                result += "Please Fill Some value in desc Box\n\n"
                allvalid = False
            elif isNumber(desc):
                result += "Please Fill Any Desc in desc Box\n\n"
                allvalid = False
            if isEmpty(name):
                result += "Please Fill Some value in name Box\n\n"
                allvalid = False
            elif isNumber(name):
                result += "Please Fill Some Name in name Box\n\n"
                allvalid = False
            if isEmpty(price):
                result += "Please Fill Some value in price Box\n\n"
                allvalid = False
            elif not isNumber(price):
                result += "Please Fill Number in price Box\n\n"
                allvalid = False
            if isEmpty(bonus):
                result += "Please Fill Some value in bonus Box\n\n"
                allvalid = False
            elif not isNumber(bonus):
                result += "Please Fill Number in bonus Box\n\n"
                allvalid = False
            print(11)
            con=conections.Connection()
            query="select FSCID from foodsubcategory where SubCategoryname='"+subcatname+"'"
            self.records=con.executeQuery(query)
            if len(self.records) > 0:
                for record in self.records:
                    fscid = record[0]

            if (allvalid == True) :
                table_name = "foodinfo"
                print(23)
                column_values = dict()
                column_values["Name"] = name
                column_values["Price"] = price
                column_values["Description"] = desc
                column_values["BonusPoint"] = bonus
                column_values["FSCID"] = fscid
                con = conections.Connection()
                print(22)
                query = con.createInsertQuery(table_name, column_values)
                print(21)
                if con.insertQuery(query):
                    result = "Food info Information is Saved in Database"
                else:
                    result = "Insertion Failure  Due To : " + con.getErrorMessage()
            else:
                print(34)
            showMessageDialog(self, result)
        except BaseException as ex:
            print(ex)

    def preparecombodata(self):
        con=conections.Connection()
        query="select subcategoryname from foodsubcategory"
        self.values=con.executeQuery(query)
        self.combo1.addItem("Chose Any Sub Category")
        if len(self.values) > 0:
            for record in self.values:
                value = record[0]
                self.combo1.addItem(str(value))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddFoodInfo()
    sys.exit(app.exec_())
