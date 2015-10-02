# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startdialog.ui'
#
# Created: Thu Oct  1 22:09:56 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(228, 154)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 110, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.loadproject_rb = QtGui.QRadioButton(Dialog)
        self.loadproject_rb.setEnabled(False)
        self.loadproject_rb.setGeometry(QtCore.QRect(20, 30, 166, 20))
        self.loadproject_rb.setObjectName(_fromUtf8("loadproject_rb"))
        self.buttonGroup = QtGui.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.loadproject_rb)
        self.importterms_rb = QtGui.QRadioButton(Dialog)
        self.importterms_rb.setGeometry(QtCore.QRect(20, 70, 138, 20))
        self.importterms_rb.setChecked(True)
        self.importterms_rb.setObjectName(_fromUtf8("importterms_rb"))
        self.buttonGroup.addButton(self.importterms_rb)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.loadproject_rb.setText(_translate("Dialog", "Load existing project...", None))
        self.importterms_rb.setText(_translate("Dialog", "Import term lists...", None))

