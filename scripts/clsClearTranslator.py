#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import math
import time
import datetime
import numpy as np
import pandas as pd

from clsSaveChanges import *
from clsTestResult import *

class Ui_FormClearTranslator(object):
    def setupUi(self, FormClearTranslator):
        FormClearTranslator.setObjectName("FormClearTranslator")
        FormClearTranslator.resize(643, 305)
        self.label = QtWidgets.QLabel(FormClearTranslator)
        self.label.setGeometry(QtCore.QRect(210, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelTask = QtWidgets.QLabel(FormClearTranslator)
        self.labelTask.setGeometry(QtCore.QRect(20, 80, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.labelTask.setFont(font)
        self.labelTask.setWordWrap(True)
        self.labelTask.setObjectName("labelTask")
        self.lineAnswer = QtWidgets.QLineEdit(FormClearTranslator)
        self.lineAnswer.setGeometry(QtCore.QRect(120, 150, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.lineAnswer.setFont(font)
        self.lineAnswer.setObjectName("lineAnswer")
        self.progressBar = QtWidgets.QProgressBar(FormClearTranslator)
        self.progressBar.setGeometry(QtCore.QRect(10, 270, 621, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.btnEnter = QtWidgets.QPushButton(FormClearTranslator)
        self.btnEnter.setGeometry(QtCore.QRect(380, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.btnEnter.setFont(font)
        self.btnEnter.setObjectName("btnEnter")
        self.btnBack = QtWidgets.QPushButton(FormClearTranslator)
        self.btnBack.setGeometry(QtCore.QRect(530, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.labelRightAnswer = QtWidgets.QLabel(FormClearTranslator)
        self.labelRightAnswer.setGeometry(QtCore.QRect(80, 200, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.labelRightAnswer.setFont(font)
        self.labelRightAnswer.setWordWrap(True)
        self.labelRightAnswer.setObjectName("labelRightAnswer")
        self.lcdNumber = QtWidgets.QLCDNumber(FormClearTranslator)
        self.lcdNumber.setGeometry(QtCore.QRect(550, 30, 81, 51))
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(FormClearTranslator)
        QtCore.QMetaObject.connectSlotsByName(FormClearTranslator)

    def retranslateUi(self, FormClearTranslator):
        _translate = QtCore.QCoreApplication.translate
        FormClearTranslator.setWindowTitle(_translate("FormClearTranslator", "Form"))
        self.label.setText(_translate("FormClearTranslator", "Translate a word"))
        self.labelTask.setText(_translate("FormClearTranslator", "TextLabel"))
        self.btnEnter.setText(_translate("FormClearTranslator", "Enter"))
        self.btnBack.setText(_translate("FormClearTranslator", "Back"))
        self.labelRightAnswer.setText(_translate("FormClearTranslator", "TextLabel"))

        
class ClearTranslator(QtWidgets.QDialog):
    def __init__(self, root, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_FormClearTranslator()
        self.ui.setupUi(self)
        
        self.main = root
        self.df_dict = self.main.main.well_learned
        self.count = self.main.count
        self.directForward = self.main.directForward
        self.time_is_set = self.main.time_is_set
        self.timer_val = self.main.timer_val
        self.i = 0
        self.right_count = 0
        self.delta_time = 0
        
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
        
        self.ui.labelRightAnswer.setText('')
        
        self.ui.btnEnter.clicked.connect(self.go_next)
        self.ui.btnBack.clicked.connect(self.go_exit)
        
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.show()
        self.create_task()
    
    def create_task(self):
        self.start_time = datetime.datetime.now()  
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
        self.right_ans_str = str(self.right_answer.values[0][self.col_task])
        self.ui.labelTask.setText(self.right_ans_str)
        self.ui.labelTask.repaint()
        
        self.progress_counter = ((self.i+1)/self.count) * 100 
        self.ui.progressBar.setProperty("value", self.progress_counter)
        self.ui.progressBar.repaint()
        
    def go_next(self):
        row = self.right_answer.index[0]
        user_ans_is_true = False
        user_ans = self.ui.lineAnswer.text()
        user_ans = user_ans.strip()
        user_ans = user_ans.lower()
        if ', ' in self.right_ans_str:
            real_ans = self.right_ans_str.split(', ')
            if user_ans in real_ans:
                user_ans_is_true = True
        else:
            real_ans = self.right_answer.values[0][self.col_ans]
            if user_ans == real_ans:
                user_ans_is_true = True
        if user_ans_is_true:
            self.change_stat(True, row)
            self.ui.labelRightAnswer.setText('Right!')
            self.ui.labelRightAnswer.repaint()
            time.sleep(2)
            self.right_count += 1
        else:
            self.change_stat(False, row)
            self.ui.labelRightAnswer.setText(f'Wrong: {real_ans}')
            self.ui.labelRightAnswer.repaint()
            time.sleep(2)
            
        self.ui.lineAnswer.setText('')
        self.ui.lineAnswer.repaint()
        self.ui.labelRightAnswer.setText('')
        self.ui.labelRightAnswer.repaint()
             
        if self.progress_counter == 100:
            self.test_result = TestResult(self)
            self.main.main.main.df_dict = self.df_dict
        else:
            self.i += 1
            self.create_task()
            
    def change_stat(self, add: bool, row: int):
        '''Change value in the column of the given word'''
        if add:
            if self.df_dict.loc[row, 'Knowledge'] < 0.9:
                x = self.df_dict.loc[row, 'Knowledge'] + 0.1
                self.df_dict.loc[row, 'Knowledge'] = round(x, 2)
            else:
                pass #придумать f(x) -> 1 при x: [0.9, 1)
        else:
            if self.df_dict.loc[row, 'Knowledge'] > 0.16:
                x = self.df_dict.loc[row, 'Knowledge'] - 0.15
                self.df_dict.loc[row, 'Knowledge'] = round(x, 2)
            else:
                x = round(math.asinh(self.df_dict.loc[row, 'Knowledge']-0.2*self.df_dict.loc[row, 'Knowledge']), 3)
                self.df_dict.loc[row, 'Knowledge'] = x
     
    def main_timer_out(self):
        self.change_stat(False, row)
        self.ui.labelRightAnswer.setText(f'Did not have time! Right: {self.right_answer[self.col_ans]}')
        self.ui.labelRightAnswer.repaint()
        time.sleep(2)
        row = self.right_answer.index[0]
        self.change_stat(False, row)
        if self.progress_counter == 100:
            self.main.main.main.df_dict = self.df_dict
            self.delta_time += self.timer_val
            self.test_result = TestResult(self)
        else:
            self.i += 1
            self.create_task()
        
    def lcd_timer_out(self):
        time_on_display = round(((-1)*(self.timer_val - self.main_timer.remainingTime()) / 1000), 1)
        self.ui.lcdNumber.setProperty("value", time_on_display)
        self.ui.lcdNumber.repaint()
        
    def go_exit(self):
        self.save_dialog = SaveChanges(message='Leave test? Progress will not saved!')
        result = self.save_dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            self.save_dialog.close()
            self.close()
        else:
            self.save_dialog.close()