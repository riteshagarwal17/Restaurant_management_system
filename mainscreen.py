from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
import viewcustinfo,viewcustbonus,viewlogininfo,signup,loginscreen,foodcategory,foodsubcategory,FoodInfo,viewfoodinfo,viewfoodsubcat,viewfoodcat,dufoodcat,dufcs,dufoodinfo
class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("   Restaurant     Management      Screen   ")
        self.setGeometry(5,40,1950,980)
        newfont = QFont("Times",18,QFont.Bold)
        mainMenu = self.menuBar()
        operationsMenu1 = mainMenu.addMenu("Add Data")
        operationsMenu2 = mainMenu.addMenu("View Data")
        operationsMenu3 = mainMenu.addMenu("Edit Data")
        operationsMenu4 = mainMenu.addMenu("Login And Signup")
        action1 = QAction("Add Food Category", self)
        action1.setShortcut("Ctrl+N")
        action2 = QAction("Add Food  Sub Category", self)
        action2.setShortcut("Ctrl+O")
        action3 = QAction("Add Food Info", self)
        action3.setShortcut("Ctrl+P")
        action4 = QAction("View Food Info", self)
        action4.setShortcut("Ctrl+q")
        action5 = QAction("View Food Sub Category Info", self)
        action5.setShortcut("Ctrl+r")
        action6 = QAction("View Food Category Info", self)
        action6.setShortcut("Ctrl+s")
        action7 = QAction("Update And Delete Food Category", self)
        action7.setShortcut("Ctrl+t")
        action8 = QAction("Update And Delete Food Sub Category", self)
        action8.setShortcut("Ctrl+u")
        action9 = QAction("Update And Delete Food Info", self)
        action9.setShortcut("Ctrl+v")
        action10 = QAction("Sign Up", self)
        action10.setShortcut("Ctrl+w")
        action11 = QAction("LogIN", self)
        action11.setShortcut("Ctrl+x")
        action12 = QAction("View Login Info", self)
        action12.setShortcut("Ctrl+y")
        action13 = QAction("View Customer Bonus Points", self)
        action13.setShortcut("Ctrl+z")
        action14 = QAction("View Customer Info", self)
        action14.setShortcut("Ctrl+a")

        image = QImage(os.path.abspath("pic5.jpg"))
        sImage = image.scaled(QSize(1950, 1000))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        operationsMenu1.addAction(action1)
        operationsMenu1.addAction(action2)
        operationsMenu1.addAction(action3)
        operationsMenu2.addAction(action4)
        operationsMenu2.addAction(action6)
        operationsMenu2.addAction(action5)
        operationsMenu3.addAction(action7)
        operationsMenu3.addAction(action8)
        operationsMenu3.addAction(action9)
        operationsMenu2.addAction(action12)
        operationsMenu2.addAction(action13)
        operationsMenu2.addAction(action14)
        operationsMenu4.addAction(action10)
        operationsMenu4.addAction(action11)

        action1.triggered.connect(self.foodcategory)
        action2.triggered.connect(self.foodsubcategory)
        action3.triggered.connect(self.foodinfo)
        action4.triggered.connect(self.viewfoodinfo)
        action5.triggered.connect(self.viewfoodsubcatinfo)
        action6.triggered.connect(self.viewfoodcatinfo)
        action7.triggered.connect(self.editfoodcategory)
        action8.triggered.connect(self.editfoodsubcategory)
        action9.triggered.connect(self.editfoodinfo)
        action10.triggered.connect(self.signup)
        action11.triggered.connect(self.login)
        action12.triggered.connect(self.logininfo)
        action13.triggered.connect(self.custbonus)
        action14.triggered.connect(self.custinfo)

        self.show()

    def foodcategory(self):
        try:
            self.obj = foodcategory.AddFoodCategory()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def foodsubcategory(self):
        try:
            self.obj = foodsubcategory.AddFoodSubCategory()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def foodinfo(self):
        try:
            self.obj =FoodInfo.AddFoodInfo()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def viewfoodinfo(self):
        try:
            self.obj = viewfoodinfo.ViewFoodDetails()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def viewfoodsubcatinfo(self):
        try:
            self.obj = viewfoodsubcat.ViewFSCDetails()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def viewfoodcatinfo(self):
        try:
            self.obj = viewfoodcat.ViewFCDetails()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def editfoodcategory(self):
        try:
            self.obj = dufoodcat.DelAndUpdFoodCat()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def editfoodsubcategory(self):
            try:
                self.obj = dufcs.delandupdfoodsubcat()
                self.obj.show()
            except BaseException as ex:
                print(ex)

    def editfoodinfo(self):
            try:
                self.obj = dufoodinfo.DelAndUpdFoodInfo()
                self.obj.show()
            except BaseException as ex:
                print(ex)

    def signup(self):
        try:
            self.obj = signup.signup()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def login(self):
        try:
            self.obj = loginscreen.LoginScreen()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def logininfo(self):
        try:
            self.obj = viewlogininfo.viewlogin()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def custbonus(self):
        try:
            self.obj = viewcustbonus.custbonus()
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def custinfo(self):
        try:
            self.obj = viewcustinfo.custinfo()
            self.obj.show()
        except BaseException as ex:
            print(ex)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())

