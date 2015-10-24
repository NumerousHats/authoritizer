# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rundialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(274, 188)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 253, 164))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lev_rb = QtGui.QRadioButton(self.layoutWidget)
        self.lev_rb.setChecked(True)
        self.lev_rb.setObjectName(_fromUtf8("lev_rb"))
        self.buttonGroup = QtGui.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.lev_rb)
        self.verticalLayout.addWidget(self.lev_rb)
        self.damlev_rb = QtGui.QRadioButton(self.layoutWidget)
        self.damlev_rb.setObjectName(_fromUtf8("damlev_rb"))
        self.buttonGroup.addButton(self.damlev_rb)
        self.verticalLayout.addWidget(self.damlev_rb)
        self.jaro_rb = QtGui.QRadioButton(self.layoutWidget)
        self.jaro_rb.setObjectName(_fromUtf8("jaro_rb"))
        self.buttonGroup.addButton(self.jaro_rb)
        self.verticalLayout.addWidget(self.jaro_rb)
        self.jarowink_rb = QtGui.QRadioButton(self.layoutWidget)
        self.jarowink_rb.setChecked(False)
        self.jarowink_rb.setObjectName(_fromUtf8("jarowink_rb"))
        self.buttonGroup.addButton(self.jarowink_rb)
        self.verticalLayout.addWidget(self.jarowink_rb)
        self.mrac_rb = QtGui.QRadioButton(self.layoutWidget)
        self.mrac_rb.setEnabled(False)
        self.mrac_rb.setObjectName(_fromUtf8("mrac_rb"))
        self.buttonGroup.addButton(self.mrac_rb)
        self.verticalLayout.addWidget(self.mrac_rb)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.runcancel_button = QtGui.QPushButton(self.layoutWidget)
        self.runcancel_button.setAutoDefault(False)
        self.runcancel_button.setObjectName(_fromUtf8("runcancel_button"))
        self.horizontalLayout.addWidget(self.runcancel_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.runrun_button = QtGui.QPushButton(self.layoutWidget)
        self.runrun_button.setObjectName(_fromUtf8("runrun_button"))
        self.horizontalLayout.addWidget(self.runrun_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.runrun_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.runcancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Match...", None))
        self.label.setText(_translate("Dialog", "Select fuzzy string comparison method:", None))
        self.lev_rb.setText(_translate("Dialog", "Levenshtein Distance", None))
        self.damlev_rb.setText(_translate("Dialog", "Damerau-Levenshtein Distance", None))
        self.jaro_rb.setText(_translate("Dialog", "Jaro Distance", None))
        self.jarowink_rb.setText(_translate("Dialog", "Jaro-Winkler Distance", None))
        self.mrac_rb.setText(_translate("Dialog", "Match Rating Approach Comparison", None))
        self.runcancel_button.setText(_translate("Dialog", "Cancel", None))
        self.runrun_button.setText(_translate("Dialog", "Run", None))

