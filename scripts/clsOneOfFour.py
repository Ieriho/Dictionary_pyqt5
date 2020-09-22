#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import datetime
import time
import math
import numpy as np
import pandas as pd

from clsSaveChanges import *
from clsTestResult import *

class Ui_FormOOFMain(object):
    def setupUi(self, FormOOFMain):
        FormOOFMain.setObjectName("FormOOFMain")
        FormOOFMain.resize(625, 533)
        self.labelTitle = QtWidgets.QLabel(FormOOFMain)
        self.labelTitle.setGeometry(QtCore.QRect(10, 10, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.btnA = QtWidgets.QPushButton(FormOOFMain)
        self.btnA.setGeometry(QtCore.QRect(30, 140, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.btnA.setFont(font)
        self.btnA.setObjectName("btnA")
        self.btnB = QtWidgets.QPushButton(FormOOFMain)
        self.btnB.setGeometry(QtCore.QRect(30, 220, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.btnB.setFont(font)
        self.btnB.setObjectName("btnB")
        self.btnD = QtWidgets.QPushButton(FormOOFMain)
        self.btnD.setGeometry(QtCore.QRect(30, 400, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.btnD.setFont(font)
        self.btnD.setObjectName("btnD")
        self.btnC = QtWidgets.QPushButton(FormOOFMain)
        self.btnC.setGeometry(QtCore.QRect(30, 310, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.btnC.setFont(font)
        self.btnC.setObjectName("btnC")
        self.labelTask = QtWidgets.QLabel(FormOOFMain)
        self.labelTask.setGeometry(QtCore.QRect(16, 70, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.labelTask.setFont(font)
        self.labelTask.setObjectName("labelTask")
        self.progressBar = QtWidgets.QProgressBar(FormOOFMain)
        self.progressBar.setGeometry(QtCore.QRect(0, 490, 621, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.btnBack = QtWidgets.QPushButton(FormOOFMain)
        self.btnBack.setGeometry(QtCore.QRect(554, 412, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.lcdNumber = QtWidgets.QLCDNumber(FormOOFMain)
        self.lcdNumber.setGeometry(QtCore.QRect(500, 60, 121, 61))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 30.0)
        self.lcdNumber.setProperty("intValue", 30)
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(FormOOFMain)
        QtCore.QMetaObject.connectSlotsByName(FormOOFMain)

    def retranslateUi(self, FormOOFMain):
        _translate = QtCore.QCoreApplication.translate
        FormOOFMain.setWindowTitle(_translate("FormOOFMain", "Form"))
        self.labelTitle.setText(_translate("FormOOFMain", "Select right translation:"))
        self.btnA.setText(_translate("FormOOFMain", "PushButton"))
        self.btnB.setText(_translate("FormOOFMain", "PushButton"))
        self.btnD.setText(_translate("FormOOFMain", "PushButton"))
        self.btnC.setText(_translate("FormOOFMain", "PushButton"))
        self.labelTask.setText(_translate("FormOOFMain", "TextLabel"))
        self.btnBack.setText(_translate("FormOOFMain", "Back"))

        
class OneOfFour(QtWidgets.QWidget):
    def __init__(self, root, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_FormOOFMain()
        self.ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.main = root
        self.df_dict = self.main.df
        self.count = self.main.count
        self.directForward = self.main.directForward
        self.time_is_set = self.main.time_is_set
        self.timer_val = self.main.timer_val
        self.i = 0
        
        if self.time_is_set:
            self.ui.lcdNumber.setEnabled(True)
        else:
            self.ui.lcdNumber.setDisabled(False)
        self.main_timer = QtCore.QTimer()
        self.main_timer.setSingleShot(False)
        self.main_timer.timeout.connect(self.main_timer_out)
        self.lcd_timer = QtCore.QTimer()
        self.lcd_timer.setSingleShot(False)
        self.lcd_timer.timeout.connect(self.lcd_timer_out)
        
        self.ui.btnBack.clicked.connect(self.go_back)
        self.btns_grp = QtWidgets.QButtonGroup()
        self.btns_grp.addButton(self.ui.btnA)
        self.btns_grp.addButton(self.ui.btnB)
        self.btns_grp.addButton(self.ui.btnC)
        self.btns_grp.addButton(self.ui.btnD)
        self.btns_grp.buttonClicked.connect(self.go_next)

        self.right_count = 0 # counter of correct answers
        self.delta_time = 0 # elapsed time counter
        self.show()
        self.create_test()
        
    def create_test(self):
        self.start_time = datetime.datetime.now()  
        # Generate a random numbers using current microseconds on device
        np.random.seed(self.count * int(self.start_time.microsecond))
        
        if self.directForward:
            self.col_task = 1
            self.col_ans = 2
        else:
            self.col_task = 2
            self.col_ans = 1

        if self.time_is_set:
            self.main_timer.setInterval(self.timer_val*1000)
            self.lcd_timer.setInterval(100)
            self.lcd_timer.start()
        else:
            self.main_timer.setInterval(-1)
        self.main_timer.start()
        
        self.right_answer = self.df_dict.sample(n=1, weights=(1-self.df_dict['Knowledge']))
        # выбираем count_var неправильных записей в словаре так, что их род совпадает с родом правильного ответа
        # и не совпадает с индексом правильного ответа (чтоб не было повторов)
        left_answers = self.df_dict.loc[(self.df_dict.kind == self.right_answer["kind"].values[0])
                           & (self.df_dict.index != self.right_answer.index[0])].sample(n=3)
        self.test_i = self.right_answer.append(left_answers) 
        self.test_i = self.test_i.sample(frac=1) # mix

        # Output task
        self.ui.labelTask.setText(f'Word for tranlation: {self.right_answer.iloc[0][self.col_task]}')
        
        self.btns = self.btns_grp.buttons()
        for j in range(self.test_i.shape[0]):
            if self.test_i.iloc[j][self.col_task] == self.right_answer.iloc[0][self.col_task]:
                self.row_right = j # number of button (row) with right answer
            pos = self.test_i.iloc[j][self.col_ans]
            self.btns[j].setText(pos)
                                    
        self.progress_counter = ((self.i+1)/self.count) * 100 
        self.ui.progressBar.setProperty("value", self.progress_counter)
        self.ui.progressBar.repaint()
        
        for btn in self.btns:
            btn.repaint
        self.ui.labelTask.repaint()
        
        
    def change_stat(self, add: bool, row: int):
        '''Change value in the column of the given word'''
        if add:
            if self.df_dict.loc[row, 'Knowledge'] < 0.9:
                x = self.df_dict.loc[row, 'Knowledge'] + 0.075
                self.df_dict.loc[row, 'Knowledge'] = round(x, 2)
            else:
                pass #придумать f(x) -> 1 при x: [0.9, 1)
        else:
            if self.df_dict.loc[row, 'Knowledge'] > 0.1:
                x = self.df_dict.loc[row, 'Knowledge'] - 0.08
                self.df_dict.loc[row, 'Knowledge'] = round(x, 2)
            else:
                x = round(math.asinh(self.df_dict.loc[row, 'Knowledge']-0.2*self.df_dict.loc[row, 'Knowledge']), 3)
                self.df_dict.loc[row, 'Knowledge'] = x
        
    def main_timer_out(self):
        self.btns[self.row_right].setStyleSheet('QPushButton {background-color: yellow; color: black;}')
        time.sleep(2)
        self.main.main.main.df_dict = self.df_dict
        row = self.right_answer.index[0]
        self.change_stat(False, row)
        if self.progress_counter == 100:
            self.delta_time += self.timer_val
            self.test_result = TestResult(self)
        else:
            self.i += 1
            self.create_test()
            
    def lcd_timer_out(self):
        time_on_display = round(((-1)*(self.timer_val - self.main_timer.remainingTime()) / 1000), 1)
        self.ui.lcdNumber.setProperty("value", time_on_display)
        self.ui.lcdNumber.repaint()

    def go_next(self, btn):
        curr_time = round(((-1)*(self.timer_val - self.main_timer.remainingTime()) / 1000), 1)
        self.delta_time += curr_time
        self.main_timer.stop()
        
        clicked_btn = self.btns.index(btn)
        row = self.right_answer.index[0]
        if self.test_i.iloc[clicked_btn][self.col_ans] == self.right_answer.iloc[0][self.col_ans]:
            self.right_count += 1
            self.change_stat(True, row)
            
            self.btns[clicked_btn].setStyleSheet('QPushButton {background-color: green; color: white;}')
            self.btns[clicked_btn].repaint()
        else:
            self.change_stat(False, row)
            self.btns[clicked_btn].setStyleSheet('QPushButton {background-color: red; color: white;}')
            self.btns[self.row_right].setStyleSheet('QPushButton {background-color: green; color: white;}')
            self.btns[clicked_btn].repaint()
            self.btns[self.row_right].repaint()
        
        time.sleep(2)
        self.btns[clicked_btn].setStyleSheet('QPushButton {background-color: none; color: black;}')
        self.btns[self.row_right].setStyleSheet('QPushButton {background-color: none; color: black;}')
        self.btns[clicked_btn].repaint()
        self.btns[self.row_right].repaint()
        if self.progress_counter == 100:
            self.test_result = TestResult(self)
            self.main.main.main.df_dict = self.df_dict
        else:
            self.i += 1
            self.create_test()
    
    def go_back(self):
        self.save_dialog = SaveChanges(message='Leave test? Progress will not saved!')
        result = self.save_dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            self.save_dialog.close()
            
            self.close()
        else:
            self.save_dialog.close()