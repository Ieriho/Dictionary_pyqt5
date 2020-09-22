#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets, Qt

class Ui_SaveDialog(object):
    def setupUi(self, SaveDialog):
        SaveDialog.setObjectName("SaveDialog")
        SaveDialog.resize(351, 145)
        self.buttonBox = QtWidgets.QDialogButtonBox(SaveDialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 100, 191, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(SaveDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(SaveDialog)
        self.buttonBox.accepted.connect(SaveDialog.accept)
        self.buttonBox.rejected.connect(SaveDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SaveDialog)

    def retranslateUi(self, SaveDialog):
        _translate = QtCore.QCoreApplication.translate
        SaveDialog.setWindowTitle(_translate("SaveDialog", "Dialog"))

class SaveChanges(QtWidgets.QDialog):
    def __init__(self, message="Save Changes?", parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_SaveDialog()
        self.frame = QtWidgets.QFrame()
        self.ui.setupUi(self)
        self.ui.label.setText(message)