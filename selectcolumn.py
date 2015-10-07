# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectcolumn.ui'
#
# Created: Wed Oct  7 15:38:21 2015
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

class Ui_SelectcolsDialog(object):
    def setupUi(self, SelectcolsDialog):
        SelectcolsDialog.setObjectName(_fromUtf8("SelectcolsDialog"))
        SelectcolsDialog.resize(640, 480)
        self.widget = QtGui.QWidget(SelectcolsDialog)
        self.widget.setGeometry(QtCore.QRect(10, 21, 611, 451))
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
        self.tableWidget = QtGui.QTableWidget(self.widget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SelectcolsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SelectcolsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SelectcolsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SelectcolsDialog)

    def retranslateUi(self, SelectcolsDialog):
        SelectcolsDialog.setWindowTitle(_translate("SelectcolsDialog", "Select columns", None))
        self.label.setText(_translate("SelectcolsDialog", "Select column to import", None))

