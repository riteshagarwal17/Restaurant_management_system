from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import conections
from utilities import *
import sys
import os

class DelAndUpdFoodInfo(QWidget):
    def __init__(self):
        super(DelAndUpdFoodInfo, self).__init__()
        self.prepareScreen()

    def prepareScreen(self):
        self.setWindowTitle(" Delete / Update Food Info ")
        # Initialize the widgets
        newfont = QFont("Consolas", 18, QFont.Bold)
        lbl1 = QLabel('Choose Food ID :')
        lbl2 = QLabel("Enter Name: ")
        lbl3 = QLabel("Enter Price:")
        lbl4 = QLabel("Enter Description:")
        lbl5 = QLabel("Enter Bonus Points:")

        self.combo1 = QComboBox()
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit4 = QLineEdit()

        self.btnUpdate = QPushButton("Update Food Category Name")
        self.btnDelete = QPushButton("Delete Food Category")
        lbl1.setFont(newfont)
        lbl2.setFont(newfont)
        lbl3.setFont(newfont)
        lbl4.setFont(newfont)
        lbl5.setFont(newfont)

        self.combo1.setFont(newfont)
        self.edit1.setFont(newfont)
        self.edit2.setFont(newfont)
        self.edit3.setFont(newfont)
        self.edit4.setFont(newfont)
        self.btnUpdate.setFont(newfont)
        self.btnDelete.setFont(newfont)

        #prepare the Layout
        grid = QGridLayout()
        grid.setSpacing(50)
        image = QImage(os.path.abspath("pic9.jpg"))
        sImage = image.scaled(QSize(2000, 1200))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        grid.addWidget(lbl1, 1, 0)
        grid.addWidget(lbl2, 2, 0)
        grid.addWidget(lbl3, 3, 0)
        grid.addWidget(lbl4, 4, 0)
        grid.addWidget(lbl5, 5, 0)

        grid.addWidget(self.combo1, 1, 1, 1, 6)
        grid.addWidget(self.edit1, 2, 1, 1, 6)
        grid.addWidget(self.edit2, 3, 1, 1, 6)
        grid.addWidget(self.edit3, 4, 1, 1, 6)
        grid.addWidget(self.edit4, 5, 1, 1, 6)


        grid.addWidget(self.btnUpdate, 6, 0)
        grid.addWidget(self.btnDelete, 6, 1,1,4)
        self.setLayout(grid)
        self.show()
        self.prepareComboItems()
        self.btnUpdate.clicked.connect(self.updatedetails)
        self.btnDelete.clicked.connect(self.deletedetails)
        self.combo1.currentTextChanged.connect(self.changecombo)

    def prepareComboItems(self):
        self.combo1.clear()
        con = conections.Connection()
        query = "select FoodID from foodinfo"
        records = con.executeQuery(query)
        if records is not None:
            items = ['Choose Any Food']
            for record in records:
                items.append(str(record[0]))
            self.combo1.addItems(tuple(items))

    def changecombo(self):
        value=self.combo1.currentText()
        if "Choose" in value:
            self.edit1.setText("")
        else:
            con = conections.Connection()
            query = "select Name,Price,Description,BonusPoint from foodinfo where FoodID=" + value
            records = con.executeQuery(query)
            if records is not None:
                for record in records:
                    self.edit1.setText((record[0]))
                    self.edit2.setText(str(record[1]))
                    self.edit3.setText((record[2]))
                    self.edit4.setText(str(record[3]))
            else:
                self.edit1.setText("")

    def deletedetails(self):
        fid = self.combo1.currentText()
        message = ""
        if "Choose" in fid:
            message = "Please Choose Any Food"
        else:
            result = QMessageBox.question(self, 'Message From IMS System', "Are You Sure To Remove This Record?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                con = conections.Connection()
                table_name = " foodinfo"
                primary_values = dict()
                primary_values['FoodID'] = fid
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
            fid = self.combo1.currentText()
            fname = self.edit1.text()
            fprice = self.edit2.text()
            fdesc = self.edit3.text()
            fbonus = self.edit4.text()

            message = ""
            if isEmpty(fid) or isEmpty(fname) or isEmpty(fprice) or isEmpty(fdesc) or isEmpty(fbonus):
                message = "Please Fill All Boxes"
            elif "Choose" in fid:
                message = "Please Choose Any FoodID"
            elif not isNumber(fname):
                name = (fname)
                con = conections.Connection()
                table_name = 'foodinfo'
                column_values = dict()
                column_values['Name'] = fname
                column_values['Price'] = fprice
                column_values['Description'] = fdesc
                column_values['BonusPoint'] = fbonus

                primary_values = dict()
                primary_values["FoodID"] = fid
                query = con.createUpdateQuery(table_name,column_values,primary_values)
                if con.insertQuery(query):
                    message = "Course Information is Updated in Database"
                else:
                    message = "Updation Failure  Due To : " + con.getErrorMessage()
            else:
                message = "Food Name must be a Name"
            showMessageDialog(self,message)
        except BaseException as ex:
            print(ex)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DelAndUpdFoodInfo()
    sys.exit(app.exec_())
