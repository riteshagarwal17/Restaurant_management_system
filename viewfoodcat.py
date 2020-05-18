from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import conections
from utilities import *
import sys
import os

class ViewFCDetails(QWidget):
    def __init__(self):
        super(ViewFCDetails, self).__init__()
        self.prepareScreen()

    def prepareScreen(self):
        self.setWindowTitle(" View Food Category Details ")
        self.layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(2)
        column_headers = ("Category ID", "Category Name")
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.prepareTableData()
        self.layout.addWidget(self.tableWidget)
        self.setGeometry(100,100,500,400)
        image = QImage(os.path.abspath("pic6.jpg"))
        sImage = image.scaled(QSize(450, 400))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.setLayout(self.layout)
        self.show()

    def prepareTableData(self):
        con = conections.Connection()
        query = "select CategoryID,CategoryName from foodcategory"
        records = con.executeQuery(query)
        row = 0
        if records is not None:
            self.tableWidget.setRowCount(len(records))
            for record in records:
                self.tableWidget.setItem(row, 0, QTableWidgetItem(record[0]))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(record[1])))
                row += 1
        else:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(row, 0, QTableWidgetItem("No Records"))
            self.tableWidget.setItem(row, 1, QTableWidgetItem("No Records"))
        #print(records)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ViewFCDetails()
    sys.exit(app.exec_())
