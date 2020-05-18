from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import conections
from utilities import *
import sys

class custinfo(QWidget):
    def __init__(self):
        super(custinfo, self).__init__()
        self.prepareScreen()

    def prepareScreen(self):
        self.setWindowTitle(" View Customer Details ")
        self.layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        column_headers = ("CustomerID", "CustomerName","EmailID","MobileNo")
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.prepareTableData()
        self.layout.addWidget(self.tableWidget)
        self.setGeometry(100,100,800,400)
        self.setLayout(self.layout)
        self.show()

    def prepareTableData(self):
        con = conections.Connection()
        query = "select CustomerID, CustomerName, EmailID, MobileNo from customerinfo"
        records = con.executeQuery(query)
        row = 0
        if records is not None:
            self.tableWidget.setRowCount(len(records))
            print(type(records))
            for record in records:
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(record[3])))
                row += 1
        else:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("No Records"))
            self.tableWidget.setItem(row, 1, QTableWidgetItem("No Records"))
            self.tableWidget.setItem(row, 2, QTableWidgetItem("No Records"))
            self.tableWidget.setItem(row, 3, QTableWidgetItem("No Records"))

        #print(records)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = custinfo()
    sys.exit(app.exec_())
