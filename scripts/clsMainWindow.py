#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import os
import pandas as pd
from clsWorkTable import *
from clsSaveChanges import *
from clsTestChoice import *
from clsOptions import *
from clsCredits import *
from clsCreateDict import *

class Ui_FormMainWindow(object):
    def setupUi(self, FormMainWindow):
        FormMainWindow.setObjectName("FormMainWindow")
        FormMainWindow.resize(496, 629)
        self.btnSelect = QtWidgets.QPushButton(FormMainWindow)
        self.btnSelect.setGeometry(QtCore.QRect(120, 100, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.btnSelect.setFont(font)
        self.btnSelect.setObjectName("btnSelect")
        self.btnWork = QtWidgets.QPushButton(FormMainWindow)
        self.btnWork.setGeometry(QtCore.QRect(120, 190, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.btnWork.setFont(font)
        self.btnWork.setObjectName("btnWork")
        self.btnTests = QtWidgets.QPushButton(FormMainWindow)
        self.btnTests.setGeometry(QtCore.QRect(120, 290, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.btnTests.setFont(font)
        self.btnTests.setObjectName("btnTests")
        self.labelState = QtWidgets.QLabel(FormMainWindow)
        self.labelState.setGeometry(QtCore.QRect(130, 350, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(11)
        self.labelState.setFont(font)
        self.labelState.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelState.setObjectName("labelState")
        self.btnStat = QtWidgets.QPushButton(FormMainWindow)
        self.btnStat.setGeometry(QtCore.QRect(120, 430, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.btnStat.setFont(font)
        self.btnStat.setObjectName("btnStat")
        self.btnOpt = QtWidgets.QPushButton(FormMainWindow)
        self.btnOpt.setGeometry(QtCore.QRect(120, 480, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.btnOpt.setFont(font)
        self.btnOpt.setObjectName("btnOpt")
        self.btnCred = QtWidgets.QPushButton(FormMainWindow)
        self.btnCred.setGeometry(QtCore.QRect(260, 480, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.btnCred.setFont(font)
        self.btnCred.setObjectName("btnCred")
        self.btnExit = QtWidgets.QPushButton(FormMainWindow)
        self.btnExit.setGeometry(QtCore.QRect(360, 580, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")
        self.label_2 = QtWidgets.QLabel(FormMainWindow)
        self.label_2.setGeometry(QtCore.QRect(120, 59, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnNewDict = QtWidgets.QPushButton(FormMainWindow)
        self.btnNewDict.setGeometry(QtCore.QRect(410, 100, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.btnNewDict.setFont(font)
        self.btnNewDict.setObjectName("btnNewDict")

        self.retranslateUi(FormMainWindow)
        QtCore.QMetaObject.connectSlotsByName(FormMainWindow)

    def retranslateUi(self, FormMainWindow):
        _translate = QtCore.QCoreApplication.translate
        FormMainWindow.setWindowTitle(_translate("FormMainWindow", "Form"))
        self.btnSelect.setText(_translate("FormMainWindow", "Selecting a dictionary"))
        self.btnWork.setText(_translate("FormMainWindow", "Working with a dictionary"))
        self.btnTests.setText(_translate("FormMainWindow", "Tests"))
        self.labelState.setText(_translate("FormMainWindow", "Dictionary is not selected"))
        self.btnStat.setText(_translate("FormMainWindow", "Statistics"))
        self.btnOpt.setText(_translate("FormMainWindow", "Options"))
        self.btnCred.setText(_translate("FormMainWindow", "Credits"))
        self.btnExit.setText(_translate("FormMainWindow", "Exit"))
        self.label_2.setText(_translate("FormMainWindow", "Begin work!"))
        self.btnNewDict.setText(_translate("FormMainWindow", "New"))

        
class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_FormMainWindow()
        self.frame = QtWidgets.QFrame()
        
        self.main_folder = os.path.dirname(os.getcwd())
        self.txt_dir = os.path.join(self.main_folder, 'txts')
        
        self.ui.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.ui.btnTests.setDisabled(True)
        self.ui.btnWork.setDisabled(True)
        self.ui.btnSelect.setToolTip('Переход в окно выбора словаря')
        self.ui.btnWork.setToolTip('Переход в окно работы со словарём')
        self.ui.btnTests.setToolTip('Переход к тестам')
        self.ui.btnExit.setToolTip('Выход из программы')
        
        self.ui.btnSelect.clicked.connect(self.go_select)
        self.df_dict = self.ui.btnWork.clicked.connect(self.go_work)
        self.ui.btnTests.clicked.connect(self.go_test)
        self.ui.btnExit.clicked.connect(self.go_exit)
        self.ui.btnNewDict.clicked.connect(self.go_new_dict)
        
    def go_select(self):
        try:
            self.file, ffilter = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                        caption='Выберите словарь', directory='F:',
                        filter='All (*)', initialFilter='Csv (*.csv)')
            self.df_dict = pd.read_csv(self.file)
            self.df_dict = self.df_dict.drop(columns=self.df_dict.columns[0], axis=1)
            self.ui.btnTests.setEnabled(True)
            self.ui.btnWork.setEnabled(True)
            self.ui.labelState.setText(f'Выбран словарь: {self.file}')
            
        except FileNotFoundError:
            self.ui.labelState.setText('Словарь не выбран')
            self.df_dict = pd.DataFrame()
            
    def go_new_dict(self):
        self.create_new = CreateDict(self)
        
    def go_work(self):
        self.work_window = WorkTable(self)
        
    def go_test(self):
        self.testChoiceWindow = TestChoice(self)
        
    def go_exit(self):
        exit = SaveChanges('Вы действительно хотите выйти?')
        result = exit.exec_()
        if result == QtWidgets.QDialog.Accepted:
            exit.close()
            self.close()
            QtWidgets.qApp.quit()
        else:
            exit.close()