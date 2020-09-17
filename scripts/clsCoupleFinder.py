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
        self.lcdTime = QtWidgets.QLCDNumber(FormCoupleFinder)
        self.lcdTime.setGeometry(QtCore.QRect(790, 50, 111, 81))
        self.lcdTime.setObjectName("lcdTime")
        self.lcdStepCounter = QtWidgets.QLCDNumber(FormCoupleFinder)
        self.lcdStepCounter.setGeometry(QtCore.QRect(10, 40, 111, 81))
        self.lcdStepCounter.setObjectName("lcdStepCounter")
        self.label = QtWidgets.QLabel(FormCoupleFinder)
        self.label.setGeometry(QtCore.QRect(380, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(FormCoupleFinder)
        self.label_3.setGeometry(QtCore.QRect(790, 20, 91, 21))
        self.label_3.setObjectName("label_3")
        self.btn_1 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_1.setGeometry(QtCore.QRect(70, 150, 141, 91))
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_2.setGeometry(QtCore.QRect(230, 150, 141, 91))
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_3.setGeometry(QtCore.QRect(390, 150, 141, 91))
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_4.setGeometry(QtCore.QRect(550, 150, 141, 91))
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_5.setGeometry(QtCore.QRect(710, 150, 141, 91))
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_6.setGeometry(QtCore.QRect(230, 260, 141, 91))
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_7.setGeometry(QtCore.QRect(390, 260, 141, 91))
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_8.setGeometry(QtCore.QRect(70, 260, 141, 91))
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_9.setGeometry(QtCore.QRect(710, 260, 141, 91))
        self.btn_9.setObjectName("btn_9")
        self.btn_10 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_10.setGeometry(QtCore.QRect(550, 260, 141, 91))
        self.btn_10.setObjectName("btn_10")
        self.btn_11 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_11.setGeometry(QtCore.QRect(230, 370, 141, 91))
        self.btn_11.setObjectName("btn_11")
        self.btn_12 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_12.setGeometry(QtCore.QRect(390, 370, 141, 91))
        self.btn_12.setObjectName("btn_12")
        self.btn_13 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_13.setGeometry(QtCore.QRect(70, 370, 141, 91))
        self.btn_13.setObjectName("btn_13")
        self.btn_14 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_14.setGeometry(QtCore.QRect(710, 370, 141, 91))
        self.btn_14.setObjectName("btn_14")
        self.btn_15 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_15.setGeometry(QtCore.QRect(550, 370, 141, 91))
        self.btn_15.setObjectName("btn_15")
        self.btn_16 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_16.setGeometry(QtCore.QRect(230, 480, 141, 91))
        self.btn_16.setObjectName("btn_16")
        self.btn_17 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_17.setGeometry(QtCore.QRect(390, 480, 141, 91))
        self.btn_17.setObjectName("btn_17")
        self.btn_18 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_18.setGeometry(QtCore.QRect(70, 480, 141, 91))
        self.btn_18.setObjectName("btn_18")
        self.btn_19 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_19.setGeometry(QtCore.QRect(710, 480, 141, 91))
        self.btn_19.setObjectName("btn_19")
        self.btn_20 = QtWidgets.QPushButton(FormCoupleFinder)
        self.btn_20.setGeometry(QtCore.QRect(550, 480, 141, 91))
        self.btn_20.setObjectName("btn_20")

        self.retranslateUi(FormCoupleFinder)
        QtCore.QMetaObject.connectSlotsByName(FormCoupleFinder)

    def retranslateUi(self, FormCoupleFinder):
        _translate = QtCore.QCoreApplication.translate
        FormCoupleFinder.setWindowTitle(_translate("FormCoupleFinder", "FormCoupleFinder"))
        self.btnBack.setText(_translate("FormCoupleFinder", "Back"))
        self.label.setText(_translate("FormCoupleFinder", "Соберите все пары"))
        self.label_2.setText(_translate("FormCoupleFinder", "Step count"))
        self.label_3.setText(_translate("FormCoupleFinder", "Time"))
        self.btn_1.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_2.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_3.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_4.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_5.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_6.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_7.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_8.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_9.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_10.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_11.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_12.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_13.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_14.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_15.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_16.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_17.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_18.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_19.setText(_translate("FormCoupleFinder", "PushButton"))
        self.btn_20.setText(_translate("FormCoupleFinder", "PushButton"))
        
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
        self.ui.btnBack.clicked.connect(self.go_back)
        self.btns_grp = QtWidgets.QButtonGroup()
        self.btns_grp.addButton(self.ui.btn_1)
        self.btns_grp.addButton(self.ui.btn_2)
        self.btns_grp.addButton(self.ui.btn_3)
        self.btns_grp.addButton(self.ui.btn_4)
        self.btns_grp.addButton(self.ui.btn_5)
        self.btns_grp.addButton(self.ui.btn_6)
        self.btns_grp.addButton(self.ui.btn_7)
        self.btns_grp.addButton(self.ui.btn_8)
        self.btns_grp.addButton(self.ui.btn_9)
        self.btns_grp.addButton(self.ui.btn_10)
        self.btns_grp.addButton(self.ui.btn_11)
        self.btns_grp.addButton(self.ui.btn_12)
        self.btns_grp.addButton(self.ui.btn_13)
        self.btns_grp.addButton(self.ui.btn_14)
        self.btns_grp.addButton(self.ui.btn_15)
        self.btns_grp.addButton(self.ui.btn_16)
        self.btns_grp.addButton(self.ui.btn_17)
        self.btns_grp.addButton(self.ui.btn_18)
        self.btns_grp.addButton(self.ui.btn_19)
        self.btns_grp.addButton(self.ui.btn_20)
        self.btns = self.btns_grp.buttons()
        self.btns_grp.buttonClicked.connect(self.go_next)
        
        self.show()
        self.create_set()
        
    def create_set(self):
        self.start_time = datetime.datetime.now()  
        # Генерируем случайные числа, используя текущие микросекунды на устройстве
        np.random.seed(int(self.start_time.microsecond))
        df = self.cf_df.sample(n=20)
        df = df.drop(columns=df.columns[-1], axis=1)
        df = df.drop(columns=df.columns[0], axis=1)
        df = df[df.columns[0]].append(df[df.columns[1]])
        self.test_set = df.sample(frac=1)
        self.test_list = list(self.test_set.values)
        
    def change_step_counter(self):
        self.step_counter += 1
        self.ui.lcdStepCounter.setProperty("value", self.step_counter)
        self.ui.lcdStepCounter.repaint()
        
    def set_text_on_btn(self, first: bool, btn):
        if first:
            self.first = btn
            self.first.setDisabled(True)
            txt = self.test_set.values[self.btns.index(btn)]
            self.first.setText(txt)
            self.first.repaint()
        else:
            self.second = btn
            self.second.setDisabled(True)
            txt = self.test_set.values[self.btns.index(btn)]
            self.second.setText(txt)
            self.second.repaint()
    
    def btn_on_click(self, btn):
        self.change_step_counter()
        
        if not self.first:
            set_text_on_btn(True, btn)
            
        elif not self.second:
            set_text_on_btn(False, btn)
            
            if self.test_set.index.values[self.test_list.index(self.first)] == self.test_set.index.values[self.test_list.index(self.second)]:
                self.couple_counter += 1
                self.first = None
                self.second = None
                # перекрасить кнопки
                
                if self.couple_counter == 10:
                    self.go_finish()
        else:
            self.first.setText('')
            self.first.setEnabled(True)
            self.first.repaint()
            self.first = None
            self.second.setText('')
            self.second.setEnabled(True)
            self.second.repaint()
            self.second = None
                
            
            set_text_on_btn(True, btn)
            
            
        
            
            
            
    
    def go_finish(self):
        info = QtWidgets.QMessageBox.information(self, 'Выполнено',
                                                 f'Количество ходов: {self.step_counter}',
                                                 buttons=QtWidgets.QMessageBox.Close,
                                                 defaultButton=QtWidgets.QMessageBox.Close)
        
        self.close()
    
    
    def go_back(self):
        exit = SaveChanges('Вы действительно хотите вернуться в главное меню?')
        result = exit.exec_()
        if result == QtWidgets.QDialog.Accepted:
            exit.close()
            self.close()
        else:
            exit.close()
