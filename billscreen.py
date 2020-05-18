from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import conections
from utilities import  *
import datetime
import sys
import os
class billcounter(QWidget):
    def __init__(self):
        super(billcounter, self).__init__()
        self.prepareScreen()

    def prepareScreen(self):
        self.setWindowTitle(" Window Counter ")
        self.setGeometry(30, 50, 1250, 950)
        newfont = QFont("Consolas", 18, QFont.Bold)
        lbl1 = QLabel('New Customer')
        lbl2 = QLabel('Old Customer ')
        lbl3 = QLabel("Customer Name:")
        lbl4 = QLabel("Email ID:")
        lbl5 = QLabel("Phone Number:")
        lbl6 = QLabel("Table Number:")
        lbl7 = QLabel("After Reedeeming Bonus Pts,Discount:")
        lbl8 = QLabel("Choose Category:")
        lbl9 = QLabel("Choose SubCategory:")
        lbl10 = QLabel("Choose Food Item:")
        lbl11 = QLabel("Quantity:")
        lbl13 = QLabel("Grand Total:")
        lbl14 = QLabel("Choose Customer Name:")
        lbl15 = QLabel("Choose Customer Email ID:")
        lbl16 = QLabel("Your Total Bonus Points Are:")
        lbl17 = QLabel("After Discount::")
        lbl18 = QLabel("Grand Total:")

        self.rd1=QRadioButton()
        self.rd2=QRadioButton()

        btn1=QPushButton("Add To Bill")
        btn2=QPushButton("Generate Bill")
        btn3=QPushButton("Reedeem Bonus Points Here To Get Discount")
        self.table1=QTableWidget()
        self.table1.setColumnCount(4)
        self.table1.setRowCount(0)
        column_headers = ("Food Name", "Quantity", "Price", "Total Price")
        self.table1.setHorizontalHeaderLabels(column_headers)
        row=0
        self.table1.setContextMenuPolicy(Qt.ActionsContextMenu)
        deleteAction = QAction("Delete This Record", self.table1)
        editAction = QAction("Edit This Record", self.table1)
        self.table1.addAction(deleteAction)
        self.table1.addAction(editAction)
        deleteAction.triggered.connect(self.deleteOperation)
        editAction.triggered.connect(self.editOperation)

        self.combo1=QComboBox()
        self.combo2=QComboBox()
        self.combo3=QComboBox()
        self.combo4=QComboBox()
        self.combo5=QComboBox()
        self.edit1=QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3=QLineEdit()
        self.edit4=QLineEdit()
        self.edit5=QLineEdit()
        self.edit6=QLineEdit()
        self.edit7=QLineEdit()
        self.edit8=QLineEdit()
        self.edit9=QLineEdit()

        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)
        self.combo3.setFont(newfont)
        self.combo4.setFont(newfont)
        self.combo5.setFont(newfont)

        self.combo1.addItem("Choose Customer Name")
        btn1.setFont(newfont)
        btn2.setFont(newfont)
        btn3.setFont(newfont)

        lbl1.setFont(newfont)
        lbl2.setFont(newfont)
        lbl3.setFont(newfont)
        lbl4.setFont(newfont)
        lbl5.setFont(newfont)
        lbl6.setFont(newfont)
        lbl7.setFont(newfont)
        lbl8.setFont(newfont)
        lbl9.setFont(newfont)
        lbl10.setFont(newfont)
        lbl11.setFont(newfont)
        lbl13.setFont(newfont)
        lbl14.setFont(newfont)
        lbl15.setFont(newfont)
        lbl16.setFont(newfont)
        lbl17.setFont(newfont)
        lbl18.setFont(newfont)
        self.edit1.setFont(newfont)
        self.edit2.setFont(newfont)
        self.edit3.setFont(newfont)
        self.edit4.setFont(newfont)
        self.edit5.setFont(newfont)
        self.edit6.setFont(newfont)
        self.edit7.setFont(newfont)
        self.edit8.setFont(newfont)
        self.edit9.setFont(newfont)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(lbl1, 3, 0)
        grid.addWidget(lbl2, 3, 3,1,1)
        grid.addWidget(lbl3, 4, 0)
        grid.addWidget(lbl4, 5, 0)
        grid.addWidget(lbl5, 6, 0,1,1)
        grid.addWidget(lbl16, 8, 3)
        grid.addWidget(lbl6, 8, 0)
        grid.addWidget(lbl7, 12, 3)
        grid.addWidget(lbl8, 9, 0)
        grid.addWidget(lbl9, 9, 3)
        grid.addWidget(lbl10, 10, 0)
        grid.addWidget(lbl11, 10, 3)
        grid.addWidget(btn1, 11, 1,1,3)
        grid.addWidget(btn2, 21, 3)
        grid.addWidget(btn3, 12, 0,1,2)

        grid.addWidget(lbl13, 14, 0)
        grid.addWidget(lbl14, 5, 3)
        grid.addWidget(lbl15, 6, 3,1,1)
        grid.addWidget(lbl17, 19, 0,1,3)
        grid.addWidget(lbl18, 20, 0,1,1)
        grid.addWidget(self.rd1,3,1,1,1)
        grid.addWidget(self.rd2,3,4,1,1)

        grid.addWidget(self.combo1,5,4,1,2)
        grid.addWidget(self.combo2,9,1,1,2)
        grid.addWidget(self.combo3,9,4,1,2)
        grid.addWidget(self.combo4,10,1,1,2)
        grid.addWidget(self.combo5,6,4,1,2)
        grid.addWidget(self.table1,13,0,1,5)

        grid.addWidget(self.edit1, 4, 1,1,1)
        grid.addWidget(self.edit2, 5, 1,1,1)
        grid.addWidget(self.edit3, 6, 1,1,1)
        grid.addWidget(self.edit4, 8, 1,1,1)
        grid.addWidget(self.edit5, 12, 4,1,1)
        grid.addWidget(self.edit6, 10, 4,1,1)
        grid.addWidget(self.edit7, 14,1,1,1)
        grid.addWidget(self.edit8, 8,4)
        grid.addWidget(self.edit9, 20,1,1,1)
        self.preparecombo1data()
        self.combo5.addItem("Chose Any Email ID")
        self.combo1.currentTextChanged.connect(self.changecombo5)
        self.preparecombo2data()
        self.combo2.currentTextChanged.connect(self.changecombo3)
        self.combo5.currentTextChanged.connect(self.setedit8)
        self.combo3.addItem("First Chose Food Category")
        self.combo4.addItem("First Chose Food Sub Category")
        btn1.clicked.connect(self.addbill)
        btn2.clicked.connect(self.generatebill)
        btn3.clicked.connect(self.bonuspts)

        image = QImage(os.path.abspath("pic8.jpg"))
        sImage = image.scaled(QSize(2000, 1200))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        btn1.setIcon(QIcon(QPixmap("pic1.jpg")))

        self.setLayout(grid)
        self.table1.show()
        self.show()

    def generatebill(self):
        result=" "
        try:
            if(self.rd1.isChecked()):
                self.addcustinfo()
                self.addbillinfo()
                self.custbonuspt()
            elif(self.rd2.isChecked()):
                #pass
                value=self.edit5.text()
                if isEmpty(value):
                    self.addbillinfo2()
                    self.custbonuspt2()
                else:
                    self.clearbonus()
                    self.addbillinfo2()
                    self.custbonuspt2()
            else:
                result+="Plz Select Either New Customer Or New Customer"
                showMessageDialog(self, result)

        except BaseException as ex:
            print(ex)

    def addbill(self):
        self.addtotable()

    def addtotable(self):
        try:
            row=0
            self.table1.setColumnWidth(0, 460)
            value0 = self.combo4.currentText()
            value1 = self.edit6.text()
            con = conections.Connection()
            query = "select Price from foodinfo where Name= '"+value0+"'"
            self.food_price = con.executeQuery(query)
            if len(self.food_price) > 0:
                for record in self.food_price:
                    value2 = record[0]
            else:
                value2="not mentioned"
            value3=float(value2)*int(value1)
            row=0
            row = self.table1.rowCount()
            self.table1.insertRow(row)
            self.table1.setItem(row, 0, QTableWidgetItem(value0))
            self.table1.setItem(row, 1, QTableWidgetItem(value1))
            self.table1.setItem(row, 2, QTableWidgetItem(str(value2)))
            self.table1.setItem(row, 3, QTableWidgetItem(str(value3)))
            self.table1.show()
            self.grandtotal()
        except BaseException as ex:
            print(ex)

    def grandtotal(self):
        try:
            row = self.table1.rowCount()
            gtotal=0
            for rows in range(row):
                prices=self.table1.item(rows,3)
                gtotal += (float(prices.text()))
                self.edit7.setText(str(gtotal))
            total=self.edit7.text()
            discount=self.edit5.text()
            if isEmpty(discount):
                self.edit9.setText(total)
            elif "Sorry" in discount:
                self.edit9.setText(total)
            else:
                disc2=float(discount)/100
                total2=float(total)*float(disc2)
                total1=float(total)-float(total2)
                self.edit9.setText(str(total1))

        except BaseException as ex:
            print(ex)

    def deleteOperation(self):
        try:
            gtotal=self.edit7.text()
            gtotal3=self.edit9.text()
            srow = self.table1.currentRow()
            rollno = self.table1.item(srow,0).text()
            result = QMessageBox.question(self, 'Message From IMS System', "Are You Sure To Remove This Record?", QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
            if result == QMessageBox.Yes:
                prices=self.table1.item(srow,3)
                gtotal1 = (float(prices.text()))
                self.table1.removeRow(srow)
                gtotal2=float(gtotal)-float(gtotal1)
                self.edit7.setText(str(gtotal2))
                total = self.edit7.text()
                discount = self.edit5.text()
                result = "Your Entry Of Food Is Deleted"
                if isEmpty(discount):
                    self.edit9.setText(total)
                elif "Sorry" in discount:
                    self.edit9.setText(total)
                else:
                    disc2 = float(discount) / 100
                    print(11)
                    total2 = float(total) * float(disc2)
                    print(12)
                    total1 = float(total) - float(total2)
                    self.edit9.setText(str(total1))
                showMessageDialog(self, result)
            else:
                pass
        except BaseException as ex:
            print(ex)

    def editOperation(self):
        result = QMessageBox.question(self, 'Message From IMS System', "Are You Sure To Remove This Record?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.deleteOperation()
            result="Your Entry Of Food Is Deleted"
            showMessageDialog(self, result)
            print("Delete Action is Called")

    def addcustinfo(self):
        try:
            name = self.edit1.text()
            email = self.edit2.text()
            phone = self.edit3.text()
            result=""
            allvalid = True
            if isEmpty(name):
                result += "Please Fill Some value in name Box\n\n"
                allvalid = False
            elif isNumber(name):
                result += "Please Fill name in name Box\n\n"
                allvalid = False

            if isEmpty(email):
                result += "Please Fill id in email id Box\n\n"
                allvalid = False
            if isEmpty(phone):
                result += "Please Fill Number in phone Box\n\n"
                allvalid = False
            elif not isNumber(phone):
                result += "Please Fill number in phone Box\n\n"
                allvalid = False
            if (allvalid == True):
                table_name = "customerinfo"
                column_values = dict()
                column_values["CustomerName"] = name
                column_values["EmailID"] = email
                column_values["MobileNo"] = phone
                con = conections.Connection()
                query = con.createInsertQuery(table_name, column_values)
                if con.insertQuery(query):
                    result = "Customer Information is Saved in Database"
                else:
                    result = "Insertion Failure  Due To : " + con.getErrorMessage()
            else:
                print("")
            showMessageDialog(self, result)
        except BaseException as ex:
            print(ex)

    def addbillinfo(self):
        try:
            con = conections.Connection()
            query = "SELECT CustomerID FROM customerinfo WHERE CustomerID = LAST_INSERT_ID();"
            self.customer_records = con.executeQuery(query)
            if len(self.customer_records) > 0:
                for record in self.customer_records:
                    value = record[0]
            table = self.edit4.text()
            discount = self.edit5.text()
            customerid = str(value)
            result = ""
            allvalid = True
            if isEmpty(table):
                result += "Please Fill Some value in table Box\n\n"
                allvalid = False
            elif not isNumber(table):
                result += "Please Fill name in table Box\n\n"
                allvalid = False
            if isEmpty(discount):
                result += "Please Fill Number in discount id Box\n\n"
                allvalid = False
            if isEmpty(customerid):
                result += "Please Fill customer details Box\n\n"
                allvalid = False
            if (allvalid == True):
                value2=datetime.datetime.now()
                table_name = "billinfo"
                column_values = dict()
                column_values["BillDate"] = value2.strftime("%Y/%m/%d")
                column_values["BillTime"] = value2.strftime("%H:%M:%S")
                column_values["TableNo"] = table
                column_values["Discount"] = discount
                column_values["CustomerID"] = customerid
                con = conections.Connection()
                query = con.createInsertQuery(table_name, column_values)
                if con.insertQuery(query):
                    result = "Bill Information is Saved in Database"
                else:
                    result = "Insertion Failure  Due To : " + con.getErrorMessage()
            else:
                print("")
            showMessageDialog(self, result)

        except BaseException as ex:
            print(ex)

    def custbonuspt(self):
        try:
            con = conections.Connection()
            query = "SELECT CustomerID FROM customerinfo WHERE CustomerID = LAST_INSERT_ID();"
            self.customer_records = con.executeQuery(query)
            if len(self.customer_records) > 0:
                for record in self.customer_records:
                    value = record[0]
            row = self.table1.rowCount()
            bonuspts = 0
            for rows in range(row):
                foodname = self.table1.item(rows, 0)
                quantity = self.table1.item(rows, 1)
                quantity1=float(quantity.text())
                foodname1=foodname.text()
                con = conections.Connection()
                query2="select BonusPoint from foodinfo where Name='"+foodname1+"'"
                value3=con.executeQuery(query2)
                for record in value3:
                    value4 = record[0]
                value5=quantity1*value4
                bonuspts += value5
            value2 = datetime.datetime.now()
            table_name = "customerbonuspoints"
            column_values = dict()
            column_values["CustomerID"] = value
            column_values["BonusPoint"] =bonuspts
            column_values["EarnedDate"] = value2.strftime("%Y/%m/%d")
            con = conections.Connection()
            query = con.createInsertQuery(table_name, column_values)
            if con.insertQuery(query):
                result = "Customer Bonus Information is Saved in Database"
            else:
                result = "Insertion Failure  Due To : " + con.getErrorMessage()
            showMessageDialog(self, result)
        except BaseException as ex:
            print(ex)

    def preparecombo1data(self):
        con = conections.Connection()
        query = "select * from customerinfo"
        self.customer_records = con.executeQuery(query)
        if len(self.customer_records) > 0:
            for record in self.customer_records:
                value = record[1]
                self.combo1.addItem(str(value))

    def changecombo5(self):
        try:
            value= self.combo1.currentText()
            self.combo5.clear()
            self.combo5.addItem("Chose Any Email ID")
            if "Choose" in value:
                self.combo5.addItem("Chose Any Email ID")
            else:
                con = conections.Connection()
                query = "select EmailID from customerinfo where CustomerName= '"+value+"'"
                records = con.executeQuery(query)
                if records is not None:
                    for record in records:
                        self.combo5.addItem((record[0]))
                else:
                    self.combo5.addItem("No Record")
        except BaseException as ex:
            print(ex)

    def preparecombo2data(self):
        con = conections.Connection()
        self.combo2.addItem("Chose Any Food Category")
        query = "select * from foodcategory"
        self.food_records = con.executeQuery(query)
        if len(self.food_records) > 0:
            for record in self.food_records:
                value = record[1]
                self.combo2.addItem(str(value))
        else:
            self.combo2.addItem("Sorry,No Records")

    def changecombo3(self):
        try:
            value=self.combo2.currentText()
            self.combo3.clear()
            self.combo3.addItem("Chose Any Food Sub Category")
            if "chose" in value:
                self.combo3.addItem("Please Select Any Food Category")
            else:
                con = conections.Connection()
                query2="select CategoryID from foodcategory where CategoryName= '"+value+"'"
                record=con.executeQuery(query2)
                for record1 in record:
                    record2=record1[0]
                query = "select SubCategoryname from foodsubcategory where CategoryID=" + record2
                records = con.executeQuery(query)
                if records is not None:
                    for record in records:
                        self.combo3.addItem((record[0]))
                else:
                    self.combo3.addItem("No Record")
                self.combo3.currentTextChanged.connect(self.changecombo4)

        except BaseException as ex:
            print(ex)

    def changecombo4(self):
        try:
            value=self.combo3.currentText()
            self.combo4.clear()
            self.combo4.addItem("Chose any Food Item")
            con = conections.Connection()
            query="select FSCID from foodsubcategory where SubCategoryname='"+value+"'"
            records1 = con.executeQuery(query)
            if len(records1) > 0:
                for record in records1:
                    fscid = record[0]
            query1 = "select Name from foodinfo where FSCID="+str(fscid)
            records = con.executeQuery(query1)
            if len(records) > 0:
                for record in records:
                    self.combo4.addItem(record[0])
            else:
                self.combo4.addItem("Sorry,No Records")
        except BaseException as ex:
            print(ex)

    def setedit8(self):
        try:
            value1=self.combo1.currentText()
            value2=self.combo5.currentText()
            if "Choose" in value1:
                self.edit8.setText("")
            else:
                con = conections.Connection()
                query1="select CustomerID from customerinfo where CustomerName='"+value1+"' and EmailID='"+value2+"'"
                records1 = con.executeQuery(query1)
                if records1 is not None:
                    for record1 in records1:
                        value3=record1[0]
                else:
                    pass

                query = "select sum(BonusPoint) from customerbonuspoints where CustomerID=" +str(value3)
                records = con.executeQuery(query)
                if records is not None:
                    for record in records:
                        self.edit8.setText(str(record[0]))
                else:
                    self.edit8.setText("")
        except BaseException as ex:
            print(ex)

    def bonuspts(self):
        try:
            value1=self.edit8.text()
            self.edit5.clear()
            if value1=="None":
                self.edit5.setText("Sorry,No Bonus Points")
            elif 100<int(value1)<300:
                self.edit5.setText("2.5")
            elif 300 <int(value1) < 500:
                self.edit5.setText("5")
            elif 500<int(value1)<700:
                self.edit5.setText("7.5")
            elif 700<int(value1)<1000:
                self.edit5.setText("10")
            elif 1000<int(value1)<2000:
                self.edit5.setText("12.5")
            elif 2000 < int(value1) < 5000:
                self.edit5.setText("15")
            else:
                self.edit5.setText("20")

        except BaseException as ex:
            print(ex)

    def addbillinfo2(self):
        try:
            value1=self.combo1.currentText()
            value2=self.combo5.currentText()
            result = ""
            if "Choose" in value1:
                result+="Please Select Any Customer ID"
                showMessageDialog(self, result)
            else:
                con = conections.Connection()
                query1="select CustomerID from customerinfo where CustomerName='"+value1+"' and EmailID='"+value2+"'"
                records1 = con.executeQuery(query1)
                if records1 is not None:
                    for record1 in records1:
                        value3=record1[0]
                else:
                    pass
            table = self.edit4.text()
            value = self.edit5.text()
            if "Sorry" in value:
                discount=0
            elif isEmpty(value):
                discount=0
            else:
                discount=value
            customerid = str(value3)
            result = ""
            allvalid = True
            if isEmpty(table):
                result += "Please Fill Some value in table Box\n\n"
                allvalid = False
            elif not isNumber(table):
                result += "Please Fill name in table Box\n\n"
                allvalid = False
            if isEmpty(str(discount)):
                result += "Please Fill Number in discount id Box\n\n"
                allvalid = False
            if isEmpty(customerid):
                result += "Please Fill customer details Box\n\n"
                allvalid = False
            if (allvalid == True):
                value2=datetime.datetime.now()
                table_name = "billinfo"
                column_values = dict()
                column_values["BillDate"] = value2.strftime("%Y/%m/%d")
                column_values["BillTime"] = value2.strftime("%H:%M:%S")
                column_values["TableNo"] = table
                column_values["Discount"] = discount
                column_values["CustomerID"] = customerid
                con = conections.Connection()
                query = con.createInsertQuery(table_name, column_values)
                if con.insertQuery(query):
                    result = "Bill Information is Saved in Database"
                else:
                    result = "Insertion Failure  Due To : " + con.getErrorMessage()
            else:
                print("")
            showMessageDialog(self, result)

        except BaseException as ex:
            print(ex)

    def custbonuspt2(self):
        try:
            value1 = self.combo1.currentText()
            value2 = self.combo5.currentText()
            result = ""
            if "Choose" in value1:
                result += "Please Select Any Customer ID"
                showMessageDialog(self, result)
            else:
                con = conections.Connection()
                query1 = "select CustomerID from customerinfo where CustomerName='" + value1 + "' and EmailID='" + value2 + "'"
                records1 = con.executeQuery(query1)
                if records1 is not None:
                    for record1 in records1:
                        value = record1[0]
                else:
                    pass
            row = self.table1.rowCount()
            bonuspts = 0
            for rows in range(row):
                foodname = self.table1.item(rows, 0)
                quantity = self.table1.item(rows, 1)
                quantity1=float(quantity.text())
                foodname1=foodname.text()
                con = conections.Connection()
                query2="select BonusPoint from foodinfo where Name='"+foodname1+"'"
                value3=con.executeQuery(query2)
                for record in value3:
                    value4 = record[0]
                value5=quantity1*value4
                bonuspts += value5
            value2 = datetime.datetime.now()
            table_name = "customerbonuspoints"
            column_values = dict()
            column_values["CustomerID"] = value
            column_values["BonusPoint"] =bonuspts
            column_values["EarnedDate"] = value2.strftime("%Y/%m/%d")
            con = conections.Connection()
            query = con.createInsertQuery(table_name, column_values)
            if con.insertQuery(query):
                result = "Customer Bonus Information is Saved in Database"
            else:
                result = "Insertion Failure  Due To : " + con.getErrorMessage()
            showMessageDialog(self, result)
        except BaseException as ex:
            print(ex)

    def clearbonus(self):
        value1 = self.edit8.text()
        value1 = self.combo1.currentText()
        value2 = self.combo5.currentText()
        result = ""
        if "Choose" in value1:
            result += "Please Select Any Customer ID"
            showMessageDialog(self, result)
        else:
            con = conections.Connection()
            query1 = "select CustomerID from customerinfo where CustomerName='" + value1 + "' and EmailID='" + value2 + "'"
            records1 = con.executeQuery(query1)
            if records1 is not None:
                for record1 in records1:
                    value = record1[0]
            else:
                pass
        con = conections.Connection()
        table_name = 'customerbonuspoints'
        column_values = dict()
        column_values['BonusPoint'] = 0
        primary_values = dict()
        primary_values["CustomerID"] = value
        query = con.createUpdateQuery(table_name, column_values, primary_values)
        if con.insertQuery(query):
            message = "Course Information is Updated in Database"
        else:
            message = "Updation Failure  Due To : " + con.getErrorMessage()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = billcounter()
    sys.exit(app.exec_())


