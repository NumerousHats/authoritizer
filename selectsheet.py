# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectsheet.ui'
#
# Created: Fri Oct 23 17:39:09 2015
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

class Ui_SelectsheetDialog(object):
    def setupUi(self, SelectsheetDialog):
        SelectsheetDialog.setObjectName(_fromUtf8("SelectsheetDialog"))
        SelectsheetDialog.resize(293, 291)
        self.widget = QtGui.QWidget(SelectsheetDialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 268, 271))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.sheet_list = QtGui.QListWidget(self.widget)
        self.sheet_list.setObjectName(_fromUtf8("sheet_list"))
        self.verticalLayout.addWidget(self.sheet_list)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SelectsheetDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SelectsheetDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SelectsheetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SelectsheetDialog)

    def retranslateUi(self, SelectsheetDialog):
        SelectsheetDialog.setWindowTitle(_translate("SelectsheetDialog", "Dialog", None))
        self.label.setText(_translate("SelectsheetDialog", "Select sheet to import", None))

