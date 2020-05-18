from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import conections
from utilities import *
import sys

class ViewFoodDetails(QWidget):
    def __init__(self):
        super(ViewFoodDetails, self).__init__()
        self.prepareScreen()

    def prepareScreen(self):
        self.setWindowTitle(" View Food Details ")
        self.layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(6)
        column_headers = ("FoodID", "Name","Price","Description","Bonus Points","Food Sub Cat ID")
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.prepareTableData()
        self.layout.addWidget(self.tableWidget)
        self.setGeometry(100,100,800,400)
        self.setLayout(self.layout)
        self.show()

    def prepareTableData(self):
        con = conections.Connection()
        query = "select FoodID,Name,Price,Description,BonusPoint,FSCID from foodinfo"
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
                self.tableWidget.setItem(row, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(str(record[5])))

                row += 1
        else:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("No Records"))
            self.tableWidget.setItem(row, 1, QTableWidgetItem("No Records"))
            self.tableWidget.setItem(row, 2, QTableWidgetItem("No Records"))
            self.tableWidget.setItem(row, 3, QTableWidgetItem("No Records"))
            self.tableWidget.setItem(row, 4, QTableWidgetItem("No Records"))
            self.tableWidget.setItem(row, 5, QTableWidgetItem("No Records"))

        #print(records)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ViewFoodDetails()
    sys.exit(app.exec_())
