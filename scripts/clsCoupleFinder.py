#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import pandas as pd
import numpy as np
import datetime

from clsSaveChanges import *

class Ui_FormCoupleFinder(object):
    def setupUi(self, FormCoupleFinder):
        FormCoupleFinder.setObjectName("FormCoupleFinder")
        FormCoupleFinder.resize(918, 664)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        FormCoupleFinder.setFont(font)
        self.btnBack = QtWidgets.QPushButton(FormCoupleFinder)
        self.btnBack.setGeometry(QtCore.QRect(770, 600, 121, 51))
        self.btnBack.setObjectName("btnBack")
        self.lcdStepCounter = QtWidgets.QLCDNumber(FormCoupleFinder)
        self.lcdStepCounter.setGeometry(QtCore.QRect(10, 40, 111, 81))
        self.lcdStepCounter.setObjectName("lcdStepCounter")
        self.labelTitle = QtWidgets.QLabel(FormCoupleFinder)
        self.labelTitle.setGeometry(QtCore.QRect(380, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.labelCount = QtWidgets.QLabel(FormCoupleFinder)
        self.labelCount.setGeometry(QtCore.QRect(50, 10, 91, 21))
        self.labelCount.setObjectName("labelCount")
        self.btn_1 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_1.setGeometry(QtCore.QRect(70, 150, 141, 91))
        self.btn_1.setText("")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_2.setGeometry(QtCore.QRect(230, 150, 141, 91))
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_3.setGeometry(QtCore.QRect(390, 150, 141, 91))
        self.btn_3.setText("")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_4.setGeometry(QtCore.QRect(550, 150, 141, 91))
        self.btn_4.setText("")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_5.setGeometry(QtCore.QRect(710, 150, 141, 91))
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_6.setGeometry(QtCore.QRect(70, 260, 141, 91))
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_7.setGeometry(QtCore.QRect(230, 260, 141, 91))
        self.btn_7.setText("")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_8.setGeometry(QtCore.QRect(390, 260, 141, 91))
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_9.setGeometry(QtCore.QRect(550, 260, 141, 91))
        self.btn_9.setText("")
        self.btn_9.setObjectName("btn_9")
        self.btn_10 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_10.setGeometry(QtCore.QRect(710, 260, 141, 91))
        self.btn_10.setText("")
        self.btn_10.setObjectName("btn_10")
        self.btn_11 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_11.setGeometry(QtCore.QRect(70, 370, 141, 91))
        self.btn_11.setText("")
        self.btn_11.setObjectName("btn_11")
        self.btn_12 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_12.setGeometry(QtCore.QRect(230, 370, 141, 91))
        self.btn_12.setText("")
        self.btn_12.setObjectName("btn_12")
        self.btn_13 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_13.setGeometry(QtCore.QRect(390, 370, 141, 91))
        self.btn_13.setText("")
        self.btn_13.setObjectName("btn_13")
        self.btn_14 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_14.setGeometry(QtCore.QRect(550, 370, 141, 91))
        self.btn_14.setText("")
        self.btn_14.setObjectName("btn_14")
        self.btn_15 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_15.setGeometry(QtCore.QRect(710, 370, 141, 91))
        self.btn_15.setText("")
        self.btn_15.setObjectName("btn_15")
        self.btn_16 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_16.setGeometry(QtCore.QRect(70, 480, 141, 91))
        self.btn_16.setText("")
        self.btn_16.setObjectName("btn_16")
        self.btn_17 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_17.setGeometry(QtCore.QRect(230, 480, 141, 91))
        self.btn_17.setText("")
        self.btn_17.setObjectName("btn_17")
        self.btn_18 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_18.setGeometry(QtCore.QRect(390, 480, 141, 91))
        self.btn_18.setText("")
        self.btn_18.setObjectName("btn_18")
        self.btn_19 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_19.setGeometry(QtCore.QRect(550, 480, 141, 91))
        self.btn_19.setText("")
        self.btn_19.setObjectName("btn_19")
        self.btn_20 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_20.setGeometry(QtCore.QRect(710, 480, 141, 91))
        self.btn_20.setText("")
        self.btn_20.setObjectName("btn_20")
        self.label_1 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_1.setGeometry(QtCore.QRect(70, 150, 141, 91))
        self.label_1.setText("")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setWordWrap(True)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_2.setGeometry(QtCore.QRect(230, 150, 141, 91))
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_3.setGeometry(QtCore.QRect(390, 150, 141, 91))
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_4.setGeometry(QtCore.QRect(550, 150, 141, 91))
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_5.setGeometry(QtCore.QRect(710, 150, 141, 91))
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_6.setGeometry(QtCore.QRect(70, 260, 141, 91))
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_7.setGeometry(QtCore.QRect(230, 260, 141, 91))
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_8.setGeometry(QtCore.QRect(390, 260, 141, 91))
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_9.setGeometry(QtCore.QRect(550, 260, 141, 91))
        self.label_9.setText("")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_10.setGeometry(QtCore.QRect(710, 260, 141, 91))
        self.label_10.setText("")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_11.setGeometry(QtCore.QRect(70, 370, 141, 91))
        self.label_11.setText("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_12.setGeometry(QtCore.QRect(230, 370, 141, 91))
        self.label_12.setText("")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_13.setGeometry(QtCore.QRect(390, 370, 141, 91))
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_14.setGeometry(QtCore.QRect(550, 370, 141, 91))
        self.label_14.setText("")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_15.setGeometry(QtCore.QRect(710, 370, 141, 91))
        self.label_15.setText("")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_16.setGeometry(QtCore.QRect(70, 480, 141, 91))
        self.label_16.setText("")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_17.setGeometry(QtCore.QRect(230, 480, 141, 91))
        self.label_17.setText("")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_18.setGeometry(QtCore.QRect(390, 480, 141, 91))
        self.label_18.setText("")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_19.setGeometry(QtCore.QRect(550, 480, 141, 91))
        self.label_19.setText("")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_20.setGeometry(QtCore.QRect(710, 480, 141, 91))
        self.label_20.setText("")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")

        self.retranslateUi(FormCoupleFinder)
        QtCore.QMetaObject.connectSlotsByName(FormCoupleFinder)

    def retranslateUi(self, FormCoupleFinder):
        _translate = QtCore.QCoreApplication.translate
        FormCoupleFinder.setWindowTitle(_translate("FormCoupleFinder", "Form"))
        self.btnBack.setText(_translate("FormCoupleFinder", "Back"))
        self.labelTitle.setText(_translate("FormCoupleFinder", "Соберите все пары"))
        self.labelCount.setText(_translate("FormCoupleFinder", "Step count"))

        
class CoupleFinder(QtWidgets.QDialog):
    def __init__(self, root, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_FormCoupleFinder()
        self.main = root
        self.cf_df = self.main.well_learned
        self.first = None
        self.second = None
        self.step_counter = 0
        self.couple_counter = 0
        
        self.ui.setupUi(self)
        self.initUi()
        
    def initUi(self):
        self.label_list = []
        self.label_list.append(self.ui.label_1)
        self.label_list.append(self.ui.label_2)
        self.label_list.append(self.ui.label_3)
        self.label_list.append(self.ui.label_4)
        self.label_list.append(self.ui.label_5)
        self.label_list.append(self.ui.label_6)
        self.label_list.append(self.ui.label_7)
        self.label_list.append(self.ui.label_8)
        self.label_list.append(self.ui.label_9)
        self.label_list.append(self.ui.label_10)
        self.label_list.append(self.ui.label_11)
        self.label_list.append(self.ui.label_12)
        self.label_list.append(self.ui.label_13)
        self.label_list.append(self.ui.label_14)
        self.label_list.append(self.ui.label_15)
        self.label_list.append(self.ui.label_16)
        self.label_list.append(self.ui.label_17)
        self.label_list.append(self.ui.label_18)
        self.label_list.append(self.ui.label_19)
        self.label_list.append(self.ui.label_20)
        
        self.ui.btnBack.clicked.connect(self.go_back)
        self.__btns_grp = QtWidgets.QButtonGroup()
        self.__btns_grp.addButton(self.ui.btn_1)
        self.__btns_grp.addButton(self.ui.btn_2)
        self.__btns_grp.addButton(self.ui.btn_3)
        self.__btns_grp.addButton(self.ui.btn_4)
        self.__btns_grp.addButton(self.ui.btn_5)
        self.__btns_grp.addButton(self.ui.btn_6)
        self.__btns_grp.addButton(self.ui.btn_7)
        self.__btns_grp.addButton(self.ui.btn_8)
        self.__btns_grp.addButton(self.ui.btn_9)
        self.__btns_grp.addButton(self.ui.btn_10)
        self.__btns_grp.addButton(self.ui.btn_11)
        self.__btns_grp.addButton(self.ui.btn_12)
        self.__btns_grp.addButton(self.ui.btn_13)
        self.__btns_grp.addButton(self.ui.btn_14)
        self.__btns_grp.addButton(self.ui.btn_15)
        self.__btns_grp.addButton(self.ui.btn_16)
        self.__btns_grp.addButton(self.ui.btn_17)
        self.__btns_grp.addButton(self.ui.btn_18)
        self.__btns_grp.addButton(self.ui.btn_19)
        self.__btns_grp.addButton(self.ui.btn_20)
        self.__btns = self.__btns_grp.buttons()
        self.__btns_grp.buttonClicked.connect(self.btn_on_click)
        
        self.show()
        self.create_set()
        
    def create_set(self):
        self.start_time = datetime.datetime.now()  
        np.random.seed(int(self.start_time.microsecond))
        df = self.cf_df.sample(n=10)
        df = df.drop(columns=df.columns[-1], axis=1)
        df = df.drop(columns=df.columns[0], axis=1)
        df = df[df.columns[0]].append(df[df.columns[1]])
        self.test_set = df.sample(frac=1)
        self.test_list = list(self.test_set.values)
        for i in range(len(self.test_list)):
            self.label_list[i].setText(self.test_list[i])
            self.label_list[i].hide()
        
    def change_step_counter(self):
        self.step_counter += 1
        self.ui.lcdStepCounter.setProperty("value", self.step_counter)
        self.ui.lcdStepCounter.repaint()
        
    def btn_on_click(self, btn):
        self.change_step_counter()
        if not self.first:
            self.__first_btn = btn
            self.__first_btn.hide()
            self.first = self.label_list[self.__btns.index(btn)]
            self.first.show()
        elif not self.second:
            self.__second_btn = btn
            self.__second_btn.hide()
            self.second = self.label_list[self.__btns.index(btn)]
            self.second.show()

            if self.test_set.index.values[self.test_list.index(self.first.text())] == self.test_set.index.values[self.test_list.index(self.second.text())]:
                self.couple_counter += 1
                self.first.setStyleSheet('QLabel {background-color: green; color: white;}')
                self.second.setStyleSheet('QLabel {background-color: green; color: white;}')
                self.first = None
                self.__first_btn = None
                self.second = None
                self.__second_btn = None
                if self.couple_counter == 10:
                    self.go_finish()
        else:
            self.first.hide()
            self.__first_btn.show()
            self.__first_btn.repaint()
            self.first = None
            self.__first_btn = None
            self.second.hide()
            self.__second_btn.show()
            self.__second_btn.repaint()
            self.second = None
            self.__second_btn = None
                
            self.__first_btn = btn
            self.__first_btn.hide()
            self.first = self.label_list[self.__btns.index(btn)]
            self.first.show()
            
    def go_finish(self):
        info = QtWidgets.QMessageBox.information(self, 'Complete',
                                                 f'Count of steps: {self.step_counter}',
                                                 buttons=QtWidgets.QMessageBox.Close,
                                                 defaultButton=QtWidgets.QMessageBox.Close)
        self.close()
    
    def go_back(self):
        exit = SaveChanges('Do you want to return to the main menu?')
        result = exit.exec_()
        if result == QtWidgets.QDialog.Accepted:
            exit.close()
            self.close()
        else:
            exit.close()
