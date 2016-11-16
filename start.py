# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created: Sat Mar  5 17:38:29 2016
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

class Ui_StartDialog(object):
    def setupUi(self, StartDialog):
        StartDialog.setObjectName(_fromUtf8("StartDialog"))
        StartDialog.resize(490, 242)
        self.buttonBox = QtGui.QDialogButtonBox(StartDialog)
        self.buttonBox.setGeometry(QtCore.QRect(-170, 180, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(StartDialog)
        self.widget.setGeometry(QtCore.QRect(50, 50, 392, 118))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(StartDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), StartDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), StartDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(StartDialog)

    def retranslateUi(self, StartDialog):
        StartDialog.setWindowTitle(_translate("StartDialog", "Dialog", None))
        self.label.setText(_translate("StartDialog", "Authority terms not loaded", None))
        self.pushButton.setText(_translate("StartDialog", "Load authority terms", None))
        self.label_2.setText(_translate("StartDialog", "Nonstandard terms not loaded", None))
        self.pushButton_2.setText(_translate("StartDialog", "Load nonstandard terms", None))
        self.label_3.setText(_translate("StartDialog", "Not ready to run matching", None))
        self.pushButton_3.setText(_translate("StartDialog", "Run matching", None))

