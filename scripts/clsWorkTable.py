#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import os
import pandas as pd

from clsSaveChanges import *

class Ui_FormWorkTable(object):
    def setupUi(self, FormWorkTable):
        FormWorkTable.setObjectName("FormWorkTable")
        FormWorkTable.resize(772, 614)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        FormWorkTable.setFont(font)
        self.tableWidget = QtWidgets.QTableWidget(FormWorkTable)
        self.tableWidget.setGeometry(QtCore.QRect(20, 130, 681, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btnNew = QtWidgets.QPushButton(FormWorkTable)
        self.btnNew.setGeometry(QtCore.QRect(20, 480, 111, 51))
        self.btnNew.setObjectName("btnNew")
        self.btnOK = QtWidgets.QPushButton(FormWorkTable)
        self.btnOK.setGeometry(QtCore.QRect(640, 550, 111, 51))
        self.btnOK.setObjectName("btnOK")
        self.btnEdit = QtWidgets.QPushButton(FormWorkTable)
        self.btnEdit.setGeometry(QtCore.QRect(170, 480, 111, 51))
        self.btnEdit.setObjectName("btnEdit")
        self.btnRemove = QtWidgets.QPushButton(FormWorkTable)
        self.btnRemove.setGeometry(QtCore.QRect(320, 480, 111, 51))
        self.btnRemove.setObjectName("btnRemove")
        self.lineSearch = QtWidgets.QLineEdit(FormWorkTable)
        self.lineSearch.setGeometry(QtCore.QRect(160, 89, 291, 31))
        self.lineSearch.setObjectName("lineSearch")
        self.btnSearch = QtWidgets.QPushButton(FormWorkTable)
        self.btnSearch.setGeometry(QtCore.QRect(30, 90, 111, 31))
        self.btnSearch.setObjectName("btnSearch")
        self.label = QtWidgets.QLabel(FormWorkTable)
        self.label.setGeometry(QtCore.QRect(140, 20, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnCleanSearch = QtWidgets.QPushButton(FormWorkTable)
        self.btnCleanSearch.setGeometry(QtCore.QRect(470, 90, 131, 31))
        self.btnCleanSearch.setObjectName("btnSearch_2")

        self.retranslateUi(FormWorkTable)
        QtCore.QMetaObject.connectSlotsByName(FormWorkTable)

    def retranslateUi(self, FormWorkTable):
        _translate = QtCore.QCoreApplication.translate
        FormWorkTable.setWindowTitle(_translate("FormWorkTable", "Form"))
        self.btnNew.setText(_translate("FormWorkTable", "Add new"))
        self.btnOK.setText(_translate("FormWorkTable", "OK"))
        self.btnEdit.setText(_translate("FormWorkTable", "Edit"))
        self.btnRemove.setText(_translate("FormWorkTable", "Remove"))
        self.btnSearch.setText(_translate("FormWorkTable", "Search:"))
        self.label.setText(_translate("FormWorkTable", "Улучшайте свой словарь!"))
        self.btnCleanSearch.setText(_translate("FormWorkTable", "Clean search"))

class WorkTable(QtWidgets.QWidget):
    def __init__(self, root, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_FormWorkTable()
        self.ui.setupUi(self)
        
        self.main = root
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.df = self.main.df_dict
        self.df_orig = self.main.df_dict.copy(deep=True)
        self.df_head = self.df.columns.values.tolist()
        
        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.tableWidget.setColumnWidth(0, 4)
        self.ui.tableWidget.resizeColumnToContents(0)
        self.ui.tableWidget.setColumnWidth(1, 20)
        self.ui.tableWidget.resizeColumnToContents(1)
        self.ui.tableWidget.setColumnWidth(2, 35)
        self.ui.tableWidget.setColumnCount(len(self.df_head))
        self.ui.tableWidget.setHorizontalHeaderLabels(self.df_head)
        
        for i in range(self.df.shape[0]):
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
            for j in range(self.ui.tableWidget.columnCount()):
                item = Qt.QTableWidgetItem()
                item.setText(str(self.df.iloc[i][j]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(i, j, item)
                self.ui.tableWidget.cellClicked.connect(self.clicked_row_column)
        
        for i in range(self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.resizeColumnToContents(i)
        
        self.ui.btnNew.setToolTip('Create new dictionary entry')
        self.ui.btnNew.clicked.connect(self.go_new)
        self.ui.btnEdit.setDisabled(True)
        self.ui.btnEdit.setToolTip('Edit selected entry')
        self.ui.btnEdit.clicked.connect(self.go_edit)
        self.ui.btnRemove.setDisabled(True)
        self.ui.btnRemove.setToolTip('Delete selected entry')
        self.ui.btnRemove.clicked.connect(self.go_remove)
        self.ui.btnSearch.setToolTip('Dictionary search')
        self.ui.btnSearch.clicked.connect(self.go_search)
        self.ui.btnCleanSearch.setDisabled(True)
        self.ui.btnCleanSearch.setToolTip('Clean search')
        self.ui.btnCleanSearch.clicked.connect(self.clean_search)
        self.ui.btnOK.clicked.connect(self.go_ok)
        
        self.old_kind = ''
        self.old_word = ''
        self.old_trsl = []
        self.old_num_trsl = 1
        
        self.show()
        
    def clicked_row_column(self, r, c):
        self.cell_number = (r, c)
        self.ui.btnEdit.setEnabled(True)
        self.ui.btnRemove.setEnabled(True)

    def go_remove(self):
        self.remove_dialog = SaveChanges(message='Delete this line from the dictionary?')
        result = self.remove_dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            self.df.drop([self.cell_number[0]], inplace=True)
            self.ui.tableWidget.hideRow(self.cell_number[0])
            self.remove_dialog.close()
        else:
            self.remove_dialog.close()
        self.ui.btnEdit.setDisabled(True)
        self.ui.btnRemove.setDisabled(True)
 
    def go_search(self):
        search_color = QtGui.QColor(0, 250, 0)
        search_text = self.ui.lineSearch.text()
        first_found = None
        for i in range(self.df.shape[0]):
            if search_text in self.df.iloc[i][1] or search_text in self.df.iloc[i][2]:
                if not first_found:
                    first_found = self.ui.tableWidget.item(i, 1)
                
                self.ui.tableWidget.item(i, 1).setBackground(search_color)
                self.ui.tableWidget.item(i, 2).setBackground(search_color)
                    
        if not first_found:
            info = QtWidgets.QMessageBox.information(self, 'Error',
                                                    'Entered text is not found!',
                                                    buttons=QtWidgets.QMessageBox.Close,
                                                    defaultButton=QtWidgets.QMessageBox.Close)
        else:
            self.ui.tableWidget.setCurrentItem(first_found)      
        self.ui.tableWidget.repaint()
        self.ui.btnCleanSearch.setEnabled(True)

    def clean_search(self):
        clean_color = QtGui.QColor(255, 255, 255)
        self.ui.lineSearch.setText('')
        for i in range(self.df.shape[0]):
            self.ui.tableWidget.item(i, 1).setBackground(clean_color)
            self.ui.tableWidget.item(i, 2).setBackground(clean_color)
        self.ui.tableWidget.repaint()
        self.ui.btnRemove.setDisabled(True)
        
    def save_record(self, msg="Save changes?", *args):
        '''Exit recording window'''
        save_rec = SaveChanges(msg) 
        result = save_rec.exec_()
        if result == QtWidgets.QDialog.Accepted:
            save_rec.close()
            return tuple(args)
        else:
            save_rec.close()
            return tuple()
        
    def check_str(self, s: str):
        '''Processing and verification the entered word'''
        s_state = False
        if ' ' in s:
            temp = s.replace(' ', '')
            if temp.isalpha:
                s_state = True
        elif s.isalpha:
            s_state = True            
        s = s.strip()
        s = s.lower()
        return s, s_state
    
    def check_the_same_one(self, s: str, col: int):
        '''Verification, is there such a word with same kind in the dictionary'''
        s_state = True
        if s in self.df[self.df.columns[col]]:
            kind_idx = self.df[self.df.columns[0]].values.index(s)
            if self.df.loc[kind_idx, self.df.columns[0]] == kind[0]:
                s_state = False
        return s_state
                    
        
    def go_new(self):
        kind, kind_ok = QtWidgets.QInputDialog.getItem(self, 'Input', 'Выберите род слова',
                                                     ['S - Существительное', 'V - Глагол',
                                                      'E - Прилагательное', 'A - Наречие',
                                                      'P - Частица или предлог', 'C - Выражение'])
        word_ok = False
        if kind_ok:
            word_state = False
            while not word_state:
                word, word_ok = QtWidgets.QInputDialog.getText(self, 'Input',
                                                               'Write a word',
                                                               text=self.old_word)
                word, word_state = self.check_str(word)
                if not word_state:
                    info = QtWidgets.QMessageBox.information(self, 'Error',
                                                             'Only spaces and letters are allowed in the input!',
                                                             buttons=QtWidgets.QMessageBox.Close,
                                                             defaultButton=QtWidgets.QMessageBox.Close)
                word_state = self.check_the_same_one(word, 1)
                if not word_state:
                    info = QtWidgets.QMessageBox.information(self, 'Error',
                                                             'This word is already in the dictionary!',
                                                             buttons=QtWidgets.QMessageBox.Close,
                                                             defaultButton=QtWidgets.QMessageBox.Close)

        if word_ok:
            num, num_ok = QtWidgets.QInputDialog.getInt(self, 'Input', 'Input a number of translation options',
                                                        value=self.old_num_trsl, min=1, max=5, step=1)
            if num_ok:
                trsl_str = ''
                i = 0
                while num - i >= 1:
                    trsl_state = False
                    while not trsl_state:
                        try:
                            default_text = self.old_trsl[i]
                        except IndexError:
                            default_text = ''
                        
                        trsl_ok = False
                        trsl, trsl_ok = QtWidgets.QInputDialog.getText(self, 'Input',
                                                                       f'Write a translation №{i+1}',
                                                                       text=default_text)
                        trsl, trsl_state = self.check_str(trsl)
                        if not trsl_state:
                            info = QtWidgets.QMessageBox.information(self, 'Error',
                                                                    'Only spaces and letters are allowed in the input!',
                                                                    buttons=QtWidgets.QMessageBox.Close,
                                                                    defaultButton=QtWidgets.QMessageBox.Close)   
                    if trsl_ok:
                        trsl_str += (trsl + ', ')
                        if num - i == 1:
                            trsl_str_state = self.check_the_same_one(trsl_str[:len(trsl_str)-2], 2)
                            if trsl_str_state:
                                new_record = self.save_record("Save entry?", kind[0],
                                                          word, trsl_str[:len(trsl_str)-2], 0.1)
                            else:
                                txt = 'Exactly the same translation is already in the dictionary! Try input again'
                                info = QtWidgets.QMessageBox.information(self, 'Error',
                                                             txt,
                                                             buttons=QtWidgets.QMessageBox.Close,
                                                             defaultButton=QtWidgets.QMessageBox.Close)
                                i = 0
                        i += 1
                    else:
                        new_record = self.save_record("Save a kind, a word and current translation?",
                                                      kind[0], word, trsl_str[:len(trsl_str)-2], 0.1)
                        break
            else:
                new_record = self.save_record("Save the word without translation?", kind[0], word)
            ##############################    
            currentRowCount = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(currentRowCount)
            self.df.loc[currentRowCount+1] = new_record
            for i in range(len(self.df.columns)):
                item = Qt.QTableWidgetItem()
                item.setText(str(new_record[i]))
                self.ui.tableWidget.setItem(currentRowCount, i, item)
                
    def go_edit(self):
        row = self.cell_number[0]
        self.old_kind = self.df.iloc[row][0]
        self.old_word = self.df.iloc[row][1]
        self.old_trsl = self.df.iloc[row][2]
        if ', ' in self.old_trsl:
            self.old_trsl = old_trsl.split(', ')
            self.old_num_trsl = len(self.old_trsl)
        else:
            self.old_trsl = [self.old_trsl]
            self.old_num_trsl = 1
            
        self.go_new()
        
        self.ui.btnEdit.setDisabled(True)
        self.ui.btnRemove.setDisabled(True)
        self.old_kind = ''
        self.old_word = ''
        self.old_trsl = []
        self.old_num_trsl = 1

    def go_ok(self):
        self.save_dialog = SaveChanges()
        result = self.save_dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            self.main.df_dict = self.df
            self.main.df_dict.to_csv(self.main.file)
            self.save_dialog.close()
            self.close()
        else:
            self.main.df_dict = self.df_orig
            self.save_dialog.close()
            self.close()
# In[ ]:
