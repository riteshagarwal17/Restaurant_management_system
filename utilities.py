from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def showMessageDialog(self,message):
    QMessageBox.question(self, 'Message From IMS System', message, QMessageBox.Ok)

def isEmpty(value):
    return len(value) == 0

def isNumber(value):
    try:
        val = int(value)
        return True
    except:
        return False

def isFloat(value):
    try:
        val = float(value)
        return True
    except:
        return False

def validContact(value):
    if len(value) == 10:
        for ch in value:
            if not isNumber(ch):
                return False
        return True
    return False