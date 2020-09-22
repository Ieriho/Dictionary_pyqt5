#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class Ui_FormTestResult(object):
    def setupUi(self, FormTestResult):
        FormTestResult.setObjectName("FormTestResult")
        FormTestResult.resize(553, 398)
        self.labelTitle = QtWidgets.QLabel(FormTestResult)
        self.labelTitle.setGeometry(QtCore.QRect(170, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.label = QtWidgets.QLabel(FormTestResult)
        self.label.setGeometry(QtCore.QRect(20, 100, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FormTestResult)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnGoMainMenu = QtWidgets.QPushButton(FormTestResult)
        self.btnGoMainMenu.setGeometry(QtCore.QRect(180, 320, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.btnGoMainMenu.setFont(font)
        self.btnGoMainMenu.setObjectName("btnGoMainMenu")
        self.labelRightRatio = QtWidgets.QLabel(FormTestResult)
        self.labelRightRatio.setGeometry(QtCore.QRect(320, 100, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.labelRightRatio.setFont(font)
        self.labelRightRatio.setObjectName("labelRightRatio")
        self.labelTime = QtWidgets.QLabel(FormTestResult)
        self.labelTime.setGeometry(QtCore.QRect(320, 160, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.labelTime.setFont(font)
        self.labelTime.setObjectName("labelTime")

        self.retranslateUi(FormTestResult)
        QtCore.QMetaObject.connectSlotsByName(FormTestResult)

    def retranslateUi(self, FormTestResult):
        _translate = QtCore.QCoreApplication.translate
        FormTestResult.setWindowTitle(_translate("FormTestResult", "Form"))
        self.labelTitle.setText(_translate("FormTestResult", "Test result"))
        self.label.setText(_translate("FormTestResult", "Correct answers: "))
        self.label_2.setText(_translate("FormTestResult", "Average spent on question: "))
        self.btnGoMainMenu.setText(_translate("FormTestResult", "Back to main menu"))
        self.labelRightRatio.setText(_translate("FormTestResult", "000"))
        self.labelTime.setText(_translate("FormTestResult", "000 sec"))

class TestResult(QtWidgets.QDialog):
    def __init__(self, root, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_FormTestResult()
        self.frame = QtWidgets.QFrame()
        self.main = root
        self.ui.setupUi(self)
        self.initUi()
        
    def initUi(self):
        self.__text_count = str(self.main.right_count) + '/' + str(self.main.count) + ' - '
        self.__text_count += str(round((self.main.right_count/self.main.count)*100, 1)) + '%'
        self.ui.labelRightRatio.setText(self.__text_count)
        self.ui.labelTime.setText(str(round((self.main.delta_time - 2*(self.main.count-1))/self.main.count, 1)) + ' second')
        self.ui.btnGoMainMenu.clicked.connect(self.go_menu)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.show()
        
    def go_menu(self):
        self.close()
        self.main.close()
        
        