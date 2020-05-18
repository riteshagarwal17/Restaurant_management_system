from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import conections
from utilities import *
import sys

class DelAndUpdFoodCat(QWidget):
    def __init__(self):
        super(DelAndUpdFoodCat, self).__init__()
        self.prepareScreen()

    def prepareScreen(self):
        self.setWindowTitle(" Delete / Update Food Category ")
        # Initialize the widgets
        newfont = QFont("Consolas", 18, QFont.Bold)
        lbl1 = QLabel('Choose Food Category ID :')
        lbl2 = QLabel("Enter Food Category Name: ")
        self.combo1 = QComboBox()
        self.edit1 = QLineEdit()
        self.btnUpdate = QPushButton("Update Food Category Name")
        self.btnDelete = QPushButton("Delete Food Category")
        lbl1.setFont(newfont)
        lbl2.setFont(newfont)
        self.combo1.setFont(newfont)
        self.edit1.setFont(newfont)
        self.btnUpdate.setFont(newfont)
        self.btnDelete.setFont(newfont)

        #prepare the Layout
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(lbl1, 1, 0)
        grid.addWidget(self.combo1, 1, 1, 1, 2)

        grid.addWidget(lbl2, 2, 0)
        grid.addWidget(self.edit1, 2, 1, 1, 2)

        grid.addWidget(self.btnUpdate, 4, 0)
        grid.addWidget(self.btnDelete, 4, 1)
        self.setLayout(grid)
        self.show()
        self.prepareComboItems()
        self.btnUpdate.clicked.connect(self.updatedetails)
        self.btnDelete.clicked.connect(self.deletedetails)
        self.combo1.currentTextChanged.connect(self.changecombo)

    def prepareComboItems(self):
        self.combo1.clear()
        con = conections.Connection()
        query = "select CategoryID from foodcategory"
        records = con.executeQuery(query)
        if records is not None:
            items = ['Choose Any Category']
            for record in records:
                items.append(record[0])
            self.combo1.addItems(tuple(items))

    def changecombo(self,value):
        if "Choose" in value:
            self.edit1.setText("")
        else:
            con = conections.Connection()
            query = "select CategoryName from foodcategory where CategoryID='" + value + "'"
            records = con.executeQuery(query)
            if records is not None:
                for record in records:
                    self.edit1.setText(str(record[0]))
            else:
                self.edit1.setText("")

    def deletedetails(self):
        cid = self.combo1.currentText()
        message = ""
        if "Choose" in cid:
            message = "Please Choose Any Category"
        else:
            result = QMessageBox.question(self, 'Message From IMS System', "Are You Sure To Remove This Record?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                con = conections.Connection()
                table_name = " foodcategory"
                primary_values = dict()
                primary_values['CategoryID'] = cid
                query = con.createDeleteQuery(table_name,primary_values)
                if con.insertQuery(query):
                    message = "Course Information is Deleted in Database"
                    self.prepareComboItems()
                else:
                    message = "Deletion Failure  Due To : " + con.getErrorMessage()
            else:
                message = "Now System is Not Going To Delete The Record"
        showMessageDialog(self, message)

    def updatedetails(self):
        try:
            cid = self.combo1.currentText()
            cname = self.edit1.text()
            message = ""
            if isEmpty(cid) or isEmpty(cname):
                message = "Please Fill All Boxes"
            elif "Choose" in cid:
                message = "Please Choose Any CategoryID"
            elif not isNumber(cname):
                name = (cname)
                con = conections.Connection()
                table_name = 'foodcategory'
                column_values = dict()
                column_values['CategoryName'] = cname
                primary_values = dict()
                primary_values["CategoryID"] = cid
                query = con.createUpdateQuery(table_name,column_values,primary_values)
                if con.insertQuery(query):
                    message = "Course Information is Updated in Database"
                else:
                    message = "Updation Failure  Due To : " + con.getErrorMessage()
            else:
                message = "Category Name must be a Name"
            showMessageDialog(self,message)
        except BaseException as ex:
            print(ex)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DelAndUpdFoodCat()
    sys.exit(app.exec_())
