from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import conections
from utilities import *
import sys

class delandupdfoodsubcat(QWidget):
    def __init__(self):
        super(delandupdfoodsubcat, self).__init__()
        self.prepareScreen()

    def prepareScreen(self):
        self.setWindowTitle(" Delete / Update Food Sub Category ")
        # Initialize the widgets
        newfont = QFont("Consolas", 18, QFont.Bold)
        lbl1 = QLabel('Choose Food Category ID :')
        lbl2 = QLabel("Enter Food Sub Category ID: ")
        lbl3 = QLabel("Enter Food Sub Category Name: ")
        self.combo1 = QComboBox()
        self.combo2 = QComboBox()
        self.edit1 = QLineEdit()
        self.btnUpdate = QPushButton("Update Food Category Name")
        self.btnDelete = QPushButton("Delete Food Category")
        lbl1.setFont(newfont)
        lbl2.setFont(newfont)
        lbl3.setFont(newfont)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)
        self.edit1.setFont(newfont)
        self.btnUpdate.setFont(newfont)
        self.btnDelete.setFont(newfont)

        #prepare the Layout
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(lbl1, 1, 0)
        grid.addWidget(self.combo1, 1, 1, 1, 2)

        grid.addWidget(lbl2, 2, 0)
        grid.addWidget(self.combo2, 2, 1, 1, 2)

        grid.addWidget(lbl3, 3, 0)
        grid.addWidget(self.edit1, 3, 1, 1, 2)

        grid.addWidget(self.btnUpdate, 4, 0)
        grid.addWidget(self.btnDelete, 4, 1)
        self.setLayout(grid)
        self.show()
        self.prepareCombo1Items()
        self.btnUpdate.clicked.connect(self.updatedetails)
        self.btnDelete.clicked.connect(self.deletedetails)
        self.combo1.currentTextChanged.connect(self.changecombo2)
        self.combo2.currentTextChanged.connect(self.changecombo3)


    def prepareCombo1Items(self):
        self.combo1.clear()
        con = conections.Connection()
        query = "select CategoryID from foodcategory"
        records = con.executeQuery(query)
        if records is not None:
            items = ['Choose Any Category']
            for record in records:
                items.append(record[0])
            self.combo1.addItems(tuple(items))

    def prepareCombo2Items(self):
        try:
            self.combo2.clear()
            fscid=self.combo1.currentText()
            con = conections.Connection()
            query = "select FSCID from foodsubcategory where CategoryID="+fscid
            records = con.executeQuery(query)
            if records is not None:
                items = ['Choose Any Sub Category']
                for record in records:
                    items.append(str(record[0]))
                self.combo2.addItems(tuple(items))
        except BaseException as ex:
            print(ex)

    def changecombo2(self):
        try:
            self.prepareCombo2Items()
        except BaseException as ex:
            print(ex)

    def changecombo3(self):
        try:
            value = self.combo2.currentText()
            if "Choose" in value:
                self.edit1.setText("")
            else:
                con = conections.Connection()
                query = "select SubCategoryname from foodsubcategory where FSCID=" + value
                records = con.executeQuery(query)
                if records is not None:
                    for record in records:
                        self.edit1.setText((record[0]))
                else:
                    self.edit1.setText("")
        except BaseException as ex:
            print(ex)

    def deletedetails(self):
        try:
            cid = self.combo1.currentText()
            scid = self.combo2.currentText()
            message = ""
            if "Choose" in cid:
                message = "Please Choose Any Category"
            elif "Choose" in scid:
                message = "Please Choose Any Sub Category"
            else:
                result = QMessageBox.question(self, 'Message From IMS System', "Are You Sure To Remove This Record?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if result == QMessageBox.Yes:
                    con = conections.Connection()
                    table_name = " foodsubcategory"
                    primary_values = dict()
                    primary_values['CategoryID'] = cid
                    primary_values['FSCID'] = scid
                    query = con.createDeleteQuery(table_name,primary_values)
                    if con.insertQuery(query):
                        message = "Course Information is Deleted in Database"
                        self.prepareCombo1Items()
                        self.prepareCombo2Items()
                    else:
                        message = "Deletion Failure  Due To : " + con.getErrorMessage()
                else:
                    message = "Now System is Not Going To Delete The Record"
            showMessageDialog(self, message)
        except BaseException as ex:
            print(ex)

    def updatedetails(self):
        try:
            cid = self.combo1.currentText()
            scid = self.combo2.currentText()
            fscname = self.edit1.text()
            message = ""
            if isEmpty(cid) or isEmpty(fscname) or isEmpty(scid):
                message = "Please Fill All Boxes"
            elif "Choose" in cid:
                message = "Please Choose Any CategoryID"
            elif "Choose" in scid:
                message = "Please Choose Any SubCategoryID"
            elif not isNumber(fscname):
                name = (fscname)
                con = conections.Connection()
                table_name = 'foodsubcategory'
                column_values = dict()
                column_values['SubCategoryname'] = name
                primary_values = dict()
                primary_values["FSCID"] = scid
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
    ex = delandupdfoodsubcat()
    sys.exit(app.exec_())
