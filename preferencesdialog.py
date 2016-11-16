# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferencesdialog.ui'
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

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName(_fromUtf8("PreferencesDialog"))
        PreferencesDialog.resize(640, 480)
        self.buttonBox = QtGui.QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(PreferencesDialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 591, 401))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.generalpref_tab = QtGui.QWidget()
        self.generalpref_tab.setObjectName(_fromUtf8("generalpref_tab"))
        self.display_similarity = QtGui.QCheckBox(self.generalpref_tab)
        self.display_similarity.setGeometry(QtCore.QRect(20, 30, 344, 20))
        self.display_similarity.setChecked(True)
        self.display_similarity.setObjectName(_fromUtf8("display_similarity"))
        self.tabWidget.addTab(self.generalpref_tab, _fromUtf8(""))
        self.cutoff_tab = QtGui.QWidget()
        self.cutoff_tab.setObjectName(_fromUtf8("cutoff_tab"))
        self.label_2 = QtGui.QLabel(self.cutoff_tab)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 534, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.cutoff_tab)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 437, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.widget = QtGui.QWidget(self.cutoff_tab)
        self.widget.setGeometry(QtCore.QRect(12, 90, 309, 162))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.jaro_cutoff = QtGui.QDoubleSpinBox(self.widget)
        self.jaro_cutoff.setMaximumSize(QtCore.QSize(100, 16777215))
        self.jaro_cutoff.setDecimals(3)
        self.jaro_cutoff.setMaximum(1.0)
        self.jaro_cutoff.setSingleStep(0.05)
        self.jaro_cutoff.setObjectName(_fromUtf8("jaro_cutoff"))
        self.gridLayout.addWidget(self.jaro_cutoff, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.jarowink_cutoff = QtGui.QDoubleSpinBox(self.widget)
        self.jarowink_cutoff.setMaximumSize(QtCore.QSize(100, 16777215))
        self.jarowink_cutoff.setDecimals(3)
        self.jarowink_cutoff.setMaximum(1.0)
        self.jarowink_cutoff.setSingleStep(0.05)
        self.jarowink_cutoff.setObjectName(_fromUtf8("jarowink_cutoff"))
        self.gridLayout.addWidget(self.jarowink_cutoff, 3, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.mrac_cutoff = QtGui.QDoubleSpinBox(self.widget)
        self.mrac_cutoff.setMaximumSize(QtCore.QSize(100, 16777215))
        self.mrac_cutoff.setDecimals(3)
        self.mrac_cutoff.setSingleStep(0.1)
        self.mrac_cutoff.setObjectName(_fromUtf8("mrac_cutoff"))
        self.gridLayout.addWidget(self.mrac_cutoff, 4, 1, 1, 1)
        self.lev_cutoff = QtGui.QSpinBox(self.widget)
        self.lev_cutoff.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lev_cutoff.setObjectName(_fromUtf8("lev_cutoff"))
        self.gridLayout.addWidget(self.lev_cutoff, 0, 1, 1, 1)
        self.damlev_cutoff = QtGui.QSpinBox(self.widget)
        self.damlev_cutoff.setMaximumSize(QtCore.QSize(100, 16777215))
        self.damlev_cutoff.setObjectName(_fromUtf8("damlev_cutoff"))
        self.gridLayout.addWidget(self.damlev_cutoff, 1, 1, 1, 1)
        self.tabWidget.addTab(self.cutoff_tab, _fromUtf8(""))

        self.retranslateUi(PreferencesDialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PreferencesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PreferencesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(_translate("PreferencesDialog", "Dialog", None))
        self.display_similarity.setText(_translate("PreferencesDialog", "Display similarity measures in matched authority list", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generalpref_tab), _translate("PreferencesDialog", "General preferences", None))
        self.label_2.setText(_translate("PreferencesDialog", "Set minimum value of similarity measure to auto-fill best matching authority term:", None))
        self.label_3.setText(_translate("PreferencesDialog", "New values will take effect the next time Run->Match... is executed.", None))
        self.label_5.setText(_translate("PreferencesDialog", "Levenshtein Distance", None))
        self.label_4.setText(_translate("PreferencesDialog", "Damerau-Levenshtein Distance", None))
        self.label_6.setText(_translate("PreferencesDialog", "Jaro Distance", None))
        self.label_7.setText(_translate("PreferencesDialog", "Jaro-Winkler Distance", None))
        self.label_8.setText(_translate("PreferencesDialog", "Match Rating Approach Comparison", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cutoff_tab), _translate("PreferencesDialog", "Similarity cutoffs", None))

