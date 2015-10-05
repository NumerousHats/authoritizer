# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importmessy.ui'
#
# Created: Mon Oct  5 13:41:32 2015
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
        Dialog.resize(383, 260)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 220, 271, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 332, 32))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.selectfile_button = QtGui.QPushButton(self.layoutWidget)
        self.selectfile_button.setObjectName(_fromUtf8("selectfile_button"))
        self.horizontalLayout_2.addWidget(self.selectfile_button)
        self.filename_label = QtGui.QLabel(self.layoutWidget)
        self.filename_label.setObjectName(_fromUtf8("filename_label"))
        self.horizontalLayout_2.addWidget(self.filename_label)
        self.layoutWidget_2 = QtGui.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 50, 358, 161))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget_2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.column_list = QtGui.QListWidget(self.layoutWidget_2)
        self.column_list.setObjectName(_fromUtf8("column_list"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.column_list)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.selectfile_button.setText(_translate("Dialog", "Select messy file...", None))
        self.filename_label.setText(_translate("Dialog", "(No file selected)", None))
        self.label_4.setText(_translate("Dialog", "Select column:", None))

