#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets, Qt

import os
import pandas as pd
from clsSaveChanges import *

class Ui_FormCreateDict(object):
    def setupUi(self, FormCreateDict):
        FormCreateDict.setObjectName("FormCreateDict")
        FormCreateDict.resize(475, 361)
        self.btnCreate = QtWidgets.QPushButton(FormCreateDict)
        self.btnCreate.setGeometry(QtCore.QRect(160, 310, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.btnCreate.setFont(font)
        self.btnCreate.setObjectName("btnCreate")
        self.btnBack = QtWidgets.QPushButton(FormCreateDict)
        self.btnBack.setGeometry(QtCore.QRect(290, 310, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.lineKind = QtWidgets.QLineEdit(FormCreateDict)
        self.lineKind.setGeometry(QtCore.QRect(230, 180, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.lineKind.setFont(font)
        self.lineKind.setObjectName("lineKind")
        self.lineWord = QtWidgets.QLineEdit(FormCreateDict)
        self.lineWord.setGeometry(QtCore.QRect(230, 220, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.lineWord.setFont(font)
        self.lineWord.setObjectName("lineWord")
        self.lineTrsl = QtWidgets.QLineEdit(FormCreateDict)
        self.lineTrsl.setGeometry(QtCore.QRect(230, 260, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.lineTrsl.setFont(font)
        self.lineTrsl.setObjectName("lineTrsl")
        self.label = QtWidgets.QLabel(FormCreateDict)
        self.label.setGeometry(QtCore.QRect(10, 180, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FormCreateDict)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(FormCreateDict)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FormCreateDict)
        self.label_4.setGeometry(QtCore.QRect(110, 12, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(FormCreateDict)
        self.label_5.setGeometry(QtCore.QRect(130, 140, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineDictTitle = QtWidgets.QLineEdit(FormCreateDict)
        self.lineDictTitle.setGeometry(QtCore.QRect(230, 90, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.lineDictTitle.setFont(font)
        self.lineDictTitle.setObjectName("lineDictTitle")
        self.label_7 = QtWidgets.QLabel(FormCreateDict)
        self.label_7.setGeometry(QtCore.QRect(10, 90, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(FormCreateDict)
        QtCore.QMetaObject.connectSlotsByName(FormCreateDict)

    def retranslateUi(self, FormCreateDict):
        _translate = QtCore.QCoreApplication.translate
        FormCreateDict.setWindowTitle(_translate("FormCreateDict", "Form"))
        self.btnCreate.setText(_translate("FormCreateDict", "Create"))
        self.btnBack.setText(_translate("FormCreateDict", "Back"))
        self.lineKind.setText(_translate("FormCreateDict", "kind"))
        self.lineWord.setText(_translate("FormCreateDict", "word"))
        self.lineTrsl.setText(_translate("FormCreateDict", "translation"))
        self.label.setText(_translate("FormCreateDict", "Род (тип) слова:"))
        self.label_2.setText(_translate("FormCreateDict", "Слово (термин):"))
        self.label_3.setText(_translate("FormCreateDict", "Перевод (расшифровка):"))
        self.label_4.setText(_translate("FormCreateDict", "Создайте новый словарь!"))
        self.label_5.setText(_translate("FormCreateDict", "Подписи столбцов"))
        self.lineDictTitle.setText(_translate("FormCreateDict", "Dictionary"))
        self.label_7.setText(_translate("FormCreateDict", "Название словаря:"))
        
        
class CreateDict(QtWidgets.QDialog):
    def __init__(self, root, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_FormCreateDict()
        self.main = root
        self.ui.setupUi(self)
        self.initUi()
        
    def initUi(self):
        self.ui.btnCreate.clicked.connect(self.go_create)
        self.ui.btnBack.clicked.connect(self.go_back)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.show()
     
    def check_str(self, s: str):
        '''Обработка и Проверка правильности ввода слова'''
        s_state = False
        if s.isalpha:
            s_state = True            
        s = s.strip() #удаление пробелов в начале и в конце
        s = s.capitalize()
        return s, s_state
        
    def go_create(self):
        df_title = self.ui.lineDictTitle.text()
        cols = [self.ui.lineKind.text(), self.ui.lineWord.text(),
                self.ui.lineTrsl.text(), df_title]
        for i in range(len(cols)):
            new_col_name, state = self.check_str(cols[i])
            if state:
                cols[i] = new_col_name
            else:
                info = QtWidgets.QMessageBox.information(self, 'Ошибка',
                                                         'В названиях допустимы только буквы (пока так)!',
                                                         buttons=QtWidgets.QMessageBox.Close,
                                                         defaultButton=QtWidgets.QMessageBox.Close)
                
        df_title = cols[-1]
        cols[-1] = 'Knowledge'
        self.new_df = pd.DataFrame([], columns=cols)
        folder = QtWidgets.QFileDialog.getExistingDirectory(parent=self,
                                     directory=QtCore.QDir.currentPath())
        if not folder == '':
            print(folder, df_title)
            self.new_df.to_csv(folder + '/' + df_title + '.csv')
            info = QtWidgets.QMessageBox.information(self, 'Результат',
                                                    'Словарь создан!',
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