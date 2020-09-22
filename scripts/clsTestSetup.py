#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import datetime

from clsOneOfFour import *
from clsClearTranslator import *

class Ui_FormTestSetup(object):
    def setupUi(self, FormTestSetup):
        FormTestSetup.setObjectName("FormTestSetup")
        FormTestSetup.resize(400, 433)
        self.spinBoxCount = QtWidgets.QSpinBox(FormTestSetup)
        self.spinBoxCount.setGeometry(QtCore.QRect(20, 238, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.spinBoxCount.setFont(font)
        self.spinBoxCount.setMinimum(3)
        self.spinBoxCount.setSingleStep(1)
        self.spinBoxCount.setObjectName("spinBoxCount")
        self.rbtnForward = QtWidgets.QRadioButton(FormTestSetup)
        self.rbtnForward.setGeometry(QtCore.QRect(50, 110, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.rbtnForward.setFont(font)
        self.rbtnForward.setObjectName("rbtnForward")
        self.rbtnReverse = QtWidgets.QRadioButton(FormTestSetup)
        self.rbtnReverse.setGeometry(QtCore.QRect(50, 150, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.rbtnReverse.setFont(font)
        self.rbtnReverse.setObjectName("rbtnReverse")
        self.btnBack = QtWidgets.QPushButton(FormTestSetup)
        self.btnBack.setGeometry(QtCore.QRect(320, 390, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.btnOK = QtWidgets.QPushButton(FormTestSetup)
        self.btnOK.setGeometry(QtCore.QRect(220, 390, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.btnOK.setFont(font)
        self.btnOK.setObjectName("btnOK")
        self.label = QtWidgets.QLabel(FormTestSetup)
        self.label.setGeometry(QtCore.QRect(130, 10, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(FormTestSetup)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.spinBoxTime = QtWidgets.QSpinBox(FormTestSetup)
        self.spinBoxTime.setGeometry(QtCore.QRect(20, 330, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.spinBoxTime.setFont(font)
        self.spinBoxTime.setMinimum(1)
        self.spinBoxTime.setMaximum(60)
        self.spinBoxTime.setSingleStep(2)
        self.spinBoxTime.setProperty("value", 10)
        self.spinBoxTime.setObjectName("spinBoxTime")
        self.checkBox = QtWidgets.QCheckBox(FormTestSetup)
        self.checkBox.setGeometry(QtCore.QRect(20, 296, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.label_4 = QtWidgets.QLabel(FormTestSetup)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(FormTestSetup)
        QtCore.QMetaObject.connectSlotsByName(FormTestSetup)

    def retranslateUi(self, FormTestSetup):
        _translate = QtCore.QCoreApplication.translate
        FormTestSetup.setWindowTitle(_translate("FormTestSetup", "Form"))
        self.rbtnForward.setText(_translate("FormTestSetup", "Forward"))
        self.rbtnReverse.setText(_translate("FormTestSetup", "Reverse"))
        self.btnBack.setText(_translate("FormTestSetup", "Back"))
        self.btnOK.setText(_translate("FormTestSetup", "OK"))
        self.label.setText(_translate("FormTestSetup", "Test setup"))
        self.label_3.setText(_translate("FormTestSetup", "Number of questions in the test:"))
        self.checkBox.setText(_translate("FormTestSetup", "Set response time"))
        self.label_4.setText(_translate("FormTestSetup", "Translation direction:"))


        
class TestSetup(QtWidgets.QWidget):
    def __init__(self, root, test_type='oof', parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_FormTestSetup()
        self.ui.setupUi(self)
        self.main = root
        self.df = root.df
        self.test_type = test_type
        self.directForward = True
        self.initUI() 
        
    def initUI(self):
        self.rbtn_group = QtWidgets.QButtonGroup()
        self.rbtn_group.addButton(self.ui.rbtnForward)
        self.rbtn_group.addButton(self.ui.rbtnReverse)
        self.rbtn_group.buttonClicked.connect(self.rbtn_checked)
        
        self.ui.rbtnForward.setChecked(True)
        self.ui.spinBoxCount.setMaximum(len(self.df)-4)
        self.ui.btnOK.clicked.connect(self.go_ok)
        self.ui.btnBack.clicked.connect(self.close)
        self.show()
        
    def rbtn_checked(self, btn):
        if btn == self.ui.rbtnForward:
            self.directForward = True
        else:
            self.directForward = False        

    def go_ok(self):
        if self.ui.checkBox.isChecked():
            self.time_is_set = True
            self.timer_val = self.ui.spinBoxTime.value()
        else:
            self.time_is_set = False
            self.timer_val = 0
        self.count = int(self.ui.spinBoxCount.value())
        if self.test_type == 'oof':
            self.tester = OneOfFour(self)
        elif self.test_type == 'ct':
            self.tester = ClearTranslator(self)
        else:
            raise ValueError(f'Invalid test cipher: {self.test_type}')
        self.close()
            