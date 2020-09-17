#!/usr/bin/env python
# coding: utf-8
# -*- codecs: utf-8 -*-
import codecs
# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets, Qt

from clsTestSetup import *
from clsCoupleFinder import *

import os
import sys

class Ui_FormTestChoice(object):
    def setupUi(self, FormTestChoice):
        FormTestChoice.setObjectName("FormTestChoice")
        FormTestChoice.resize(428, 589)
        self.btnOOF = QtWidgets.QPushButton(FormTestChoice)
        self.btnOOF.setGeometry(QtCore.QRect(70, 10, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnOOF.setFont(font)
        self.btnOOF.setObjectName("btnOOF")
        self.btnBack = QtWidgets.QPushButton(FormTestChoice)
        self.btnBack.setGeometry(QtCore.QRect(310, 520, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.btnCF = QtWidgets.QPushButton(FormTestChoice)
        self.btnCF.setGeometry(QtCore.QRect(70, 130, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnCF.setFont(font)
        self.btnCF.setObjectName("btnCF")
        self.btnCT = QtWidgets.QPushButton(FormTestChoice)
        self.btnCT.setGeometry(QtCore.QRect(70, 250, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnCT.setFont(font)
        self.btnCT.setObjectName("btnCT")
        self.btnWhyDisabled = QtWidgets.QPushButton(FormTestChoice)
        self.btnWhyDisabled.setGeometry(QtCore.QRect(10, 520, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnWhyDisabled.setFont(font)
        self.btnWhyDisabled.setObjectName("btnWhyDisabled")
        self.btnGallows = QtWidgets.QPushButton(FormTestChoice)
        self.btnGallows.setGeometry(QtCore.QRect(70, 370, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnGallows.setFont(font)
        self.btnGallows.setObjectName("btnGallows")

        self.retranslateUi(FormTestChoice)
        QtCore.QMetaObject.connectSlotsByName(FormTestChoice)

    def retranslateUi(self, FormTestChoice):
        _translate = QtCore.QCoreApplication.translate
        FormTestChoice.setWindowTitle(_translate("FormTestChoice", "Form"))
        self.btnOOF.setText(_translate("FormTestChoice", "One of four"))
        self.btnBack.setText(_translate("FormTestChoice", "Back"))
        self.btnCF.setText(_translate("FormTestChoice", "Couple Finder"))
        self.btnCT.setText(_translate("FormTestChoice", "Clear Translator"))
        self.btnWhyDisabled.setText(_translate("FormTestChoice", "Why test is disabled?"))
        self.btnGallows.setText(_translate("FormTestChoice", "Gallows"))
        

class TestChoice(QtWidgets.QWidget):
    def __init__(self, root, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_FormTestChoice()
        self.ui.setupUi(self)
        self.main = root
        self.df = root.df_dict
        self.initUI() 
        
    def initUI(self):
        self.well_learned = self.df.loc[self.df['Knowledge'] > 0.6]
        if self.well_learned.shape[0] >= 10:
            self.ui.btnCF.setEnabled(True)
        else:
            self.ui.btnCF.setDisabled(True)
        
        self.ui.btnOOF.clicked.connect(self.go_oof)
        self.ui.btnCF.clicked.connect(self.go_cf)
        self.ui.btnWhyDisabled.clicked.connect(self.why_tests_disabled)
        self.ui.btnBack.clicked.connect(self.close)
        self.show()
        
    def why_tests_disabled(self):
        file = self.main.txt_dir + '/' + 'why_test_is_disabled.txt'
        txt = codecs.open(file, 'r', 'utf-8')
        info = QtWidgets.QMessageBox.information(self, 'Почему?',
                                                    str(txt.read()),
                                                    buttons=QtWidgets.QMessageBox.Close,
                                                    defaultButton=QtWidgets.QMessageBox.Close)
    
    def go_oof(self):
        self.setup_oof = TestSetup(self)
        self.close()
    
    def go_cf(self):
        self.couple_finder = CoupleFinder(self)
        self.close()
        
    def go_ct(self):
        pass
        
    def go_gallows(self):
        pass
        