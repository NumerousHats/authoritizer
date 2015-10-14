import sys
from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
from selectcolumn import Ui_SelectcolsDialog
from rundialog import Ui_Dialog
from preferencesdialog import Ui_PreferencesDialog

import os
import jellyfish
import unicodecsv as csv


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.have_auth = False
        self.have_mess = False

        ###############
        ##### set up signals/slots
        ###############

        ##### menu items

        # use the trick from http://eli.thegreenplace.net/2011/04/25/passing-extra-arguments-to-pyqt-slot
        # to use same callback for two menu items
        self.ui.actionImport_auth.triggered.connect(lambda: self.importData("auth"))
        self.ui.actionImport_messy.triggered.connect(lambda: self.importData("messy"))
        self.ui.actionRun_matching.triggered.connect(self.runMatching)
        self.ui.actionExport_CSV.triggered.connect(self.exportCSV)
        self.ui.actionPreferences.triggered.connect(self.setPreferences)
        self.ui.actionQuit.triggered.connect(QtCore.QCoreApplication.instance().quit)

        ##### GUI elements

        self.ui.match_table.currentCellChanged.connect(self.updateTopHits)
        self.ui.tophit_list.itemDoubleClicked.connect(self.clickAssign)
        self.ui.createAuthority_button.clicked.connect(self.createAuth)
        self.ui.deleteAuthority_button.clicked.connect(self.deleteMatch)

        ###### default preferences

        self.cutoffs = {"lev": 10, "damlev": 10, "jaro": 0.6, "jarowink": 0.6, "mrac": 9999}
        self.display_similarity = True

    def importData(self, data_type):
        fname = str(QtGui.QFileDialog.getOpenFileName(self, "Open file", "~"))
        filename, file_extension = os.path.splitext(fname)

        if file_extension == ".csv":
            csv_fileh = open(fname, 'rU')
            try:
                dialect = csv.Sniffer().sniff(csv_fileh.read(1024))
                csv_fileh.seek(0)
                reader = csv.DictReader(csv_fileh, dialect=dialect)
                self.header = reader.next().keys()
            except csv.Error:
                QtGui.QMessageBox.warning(self, 'Warning', 'File does not appear to be valid CSV')
                return

            # everything's okay, so reopen the file and read some sample data to pass to column selector dialog

            csv_fileh.close()
            csv_fileh = open(fname, 'rU')
            reader = csv.DictReader(csv_fileh, dialect=dialect)
            self.sample = [ reader.next() for i in range(20) ]

            dlg = StartSelectColumns(self)
            if dlg.exec_(): 
                selected_column = dlg.getValues()
            else:
                return

            # read the data from the selected column. reopen file for safety (even though it's absurdly inefficient)

            csv_fileh.close()
            csv_fileh = open(fname, 'rU')
            reader = csv.DictReader(csv_fileh, dialect=dialect)

            data = list()
            for row in reader:
                data.append(row[selected_column])

            data = [i for i in data if i != ""]
            data = list(set(data))
 

        elif file_extension == ".txt":
            QtGui.QMessageBox.information(self, 'Information', 'Flat text import not yet supported.')
        elif file_extension == ".xlsx":
            QtGui.QMessageBox.information(self, 'Information', 'Excel .xlsx import not yet supported')
        elif file_extension == ".xls":
            QtGui.QMessageBox.information(self, 'Information', 'Excel .xls import not yet supported')
        else:
            QtGui.QMessageBox.warning(self, 'Warning', 'File type {} is not supported'.format(file_extension))
            return

        if data_type == "auth":
            self.authorities = data
            self.have_auth = True
        elif data_type == "messy":
            self.mess = data
            self.have_mess = True
        else:
            QtGui.QMessageBox.critical(self, 'Warning', 'Internal error: importData received unexpected argument')

        if self.have_auth and self.have_mess:
            self.ui.actionRun_matching.setEnabled(True)

    def runMatching(self):
        dlg = StartRunDialog() 
        if dlg.exec_(): 
            match_method = dlg.getValues() 
        else:
            return

        if match_method == "lev":
            match_function = jellyfish.levenshtein_distance
        elif match_method == "damlev":
            match_function = jellyfish.damerau_levenshtein_distance
        elif match_method == "jaro":
            match_function = jellyfish.jaro_distance
        elif match_method == "jarowink":
            match_function = jellyfish.jaro_winkler
        elif match_method == "mrac":
            match_function = jellyfish.match_rating_comparison
        else:
            QtGui.QMessageBox.critical(self, 'Warning', 'Internal error: runMatching received unexpected argument')

        self.all_scores = list()
        self.matched_authorities = list()

        for m in self.mess: # ideally, we want a progress bar for this loop
            scores = [ [x, match_function(m, unicode(x))] for x in self.authorities ]
            scores = sorted(scores, key=lambda score: -score[1])[0:10]
            self.all_scores.append(scores)
            cutoff = self.cutoffs[match_method]
            if match_method == "lev" or match_method == "damlev":
                self.matched_authorities.append(scores[0][0] if scores[0][1] < cutoff else False)
            else:
                self.matched_authorities.append(scores[0][0] if scores[0][1] > cutoff else False)

        self.ui.match_table.setRowCount(len(self.mess))
        self.ui.match_table.clearContents()
        self.updateTable()

    def exportCSV(self):
        fname = QtGui.QFileDialog.getSaveFileNameAndFilter(self, 'Export CSV', '~', "*.csv")
        print "got {}".format(fname)

        with open(fname[0], 'wb') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["Messy term", "Authority term"])

            for i in range(len(self.mess)):
                if self.matched_authorities[i]:
                    csvwriter.writerow([self.mess[i], self.matched_authorities[i]])

    def setPreferences(self):
        dlg = StartPreferences(self) 
        if dlg.exec_(): 
            preferences = dlg.getValues() 
        else:
            return

        self.display_similarity = preferences["display_similarity"]
        self.cutoffs = preferences["cutoffs"]

    def updateTable(self):
        for row in range(len(self.mess)):
            self.ui.match_table.setItem(row, 0, QtGui.QTableWidgetItem(self.mess[row]))
            if self.matched_authorities[row]:
                self.ui.match_table.setItem(row, 1, QtGui.QTableWidgetItem(self.matched_authorities[row]))

    def updateTopHits(self, row, column, oldrow, oldcolumn):
        self.ui.tophit_list.clear()
        for i in range(10):
            text = self.all_scores[row][i][0]
            if self.display_similarity:
                text = "{} ({:.3})".format(text, float(self.all_scores[row][i][1]))
            item = QtGui.QListWidgetItem(text)
            self.ui.tophit_list.addItem(item)

        if row != -1: # row gets set to -1 after deleteMatch(): ignore it and keep the old current_row
            self.current_row = row
        
    def clickAssign(self, item):
        self.matched_authorities[self.current_row] = item.text()
        self.updateTable()

    def createAuth(self):
        self.matched_authorities[self.current_row] = self.ui.new_authority.text()
        self.updateTable()

    def deleteMatch(self):
        self.matched_authorities[self.current_row] = False

        # there doesn't seem to be any way to clear a single cell (?!?)
        # so clear the entire table before re-rendering it
        self.ui.match_table.clearContents()
        self.updateTable()
        self.ui.match_table.setCurrentCell(self.current_row, 0)

class StartSelectColumns(QtGui.QDialog, Ui_SelectcolsDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.header = parent.header

        self.tableWidget.setColumnCount(len(self.header))
        self.tableWidget.setRowCount(len(parent.sample))
        self.tableWidget.setHorizontalHeaderLabels(self.header)
        self.tableWidget.cellClicked.connect(self.columnClicked)


        for row in range(len(parent.sample)):
            for column in range(len(self.header)):
                if parent.sample[row][self.header[column]]:
                    self.tableWidget.setItem(row, column, QtGui.QTableWidgetItem(parent.sample[row][self.header[column]]))

    def columnClicked(self, row, column):
        self.buttonBox.setEnabled(True)
        self.current_column = column

    def getValues(self):
        return self.header[self.current_column]

class StartPreferences(QtGui.QDialog, Ui_PreferencesDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.lev_cutoff.setValue(parent.cutoffs["lev"])
        self.damlev_cutoff.setValue(parent.cutoffs["damlev"])
        self.jaro_cutoff.setValue(parent.cutoffs["jaro"])
        self.jarowink_cutoff.setValue(parent.cutoffs["jarowink"])
        self.mrac_cutoff.setValue(parent.cutoffs["mrac"])

        self.display_similarity.setChecked(parent.display_similarity)

    def getValues(self):
        cutoffs = {"lev": self.lev_cutoff.value(), 
                    "damlev": self.damlev_cutoff.value(),
                    "jaro": self.jaro_cutoff.value(),
                    "jarowink": self.jarowink_cutoff.value(),
                    "mrac": self.mrac_cutoff.value()}
        prefs = {"display_similarity": self.display_similarity.isChecked(), "cutoffs": cutoffs}

        return prefs

class StartRunDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.lev_rb.toggled.connect(self.levToggled)
        self.damlev_rb.toggled.connect(self.damlevToggled)
        self.jaro_rb.toggled.connect(self.jaroToggled)
        self.jarowink_rb.toggled.connect(self.jarowinkToggled)
        self.mrac_rb.toggled.connect(self.mracToggled)

        # lev_rb is selected by default within the .ui file,
        # therefore the following line is guaranteed to generate
        # a "toggled" event, and thereby makes sure that the default
        # matching algorithm (jaro-winkler) is set even if the user
        # doesn't actually click on anything

        self.jarowink_rb.click()

    def levToggled(self, state):
        if state:
            self.distfun = "lev"
    def damlevToggled(self, state):
        if state:
            self.distfun = "damlev"
    def jaroToggled(self, state):
        if state:
            self.distfun = 'jaro'
    def jarowinkToggled(self, state):
        if state:
            self.distfun = "jarowink"
    def mracToggled(self, state):
        if state:
            self.distfun = "mrac"

    def getValues(self):
        return self.distfun


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())



# for future preference setting

# from sys import platform as _platform

# if _platform == "linux" or _platform == "linux2":
#    # linux
# elif _platform == "darwin":
#    # MAC OS X
# elif _platform == "win32":
#    # Windows

# windows prefs are in the Application Data folder for the user or for all users.
# mac prefs are in /Users/username/Library/Preferences
# linux prefs are in ~/.authoritizer

