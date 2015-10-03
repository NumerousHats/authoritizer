import sys
from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow

import jellyfish
import pandas as pd

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.have_auth = False
        self.have_mess = False

        self.ui.actionImport_auth.triggered.connect(self.importAuth)
        self.ui.actionImport_messy.triggered.connect(self.importMessy)
        self.ui.actionRun_matching.triggered.connect(self.runMatching)
        self.ui.actionQuit.triggered.connect(QtCore.QCoreApplication.instance().quit)

        self.ui.match_table.currentCellChanged.connect(self.updateTopHits)

        self.ui.tophit_list.itemDoubleClicked.connect(self.clickAssign)

        self.ui.createAuthority_button.clicked.connect(self.createAuth)
        self.ui.deleteAuthority_button.clicked.connect(self.deleteMatch)


    def importAuth(self):
        df = pd.read_csv("testdat/huge_real_life.csv")
        self.authorities = df['canonical firm'].dropna().values.tolist()
        self.authorities = list(set(self.authorities))
        self.authorities = [unicode(x) for x in self.authorities]
        self.have_auth = True

        if self.have_auth and self.have_mess:
            self.ui.actionRun_matching.setEnabled(True)

    def importMessy(self):
        df = pd.read_csv("testdat/huge_real_life.csv")
        self.mess = df['vendor'].dropna().values.tolist()
        self.mess = list(set(self.mess))
        self.mess = [unicode(x) for x in self.mess]
        self.have_mess = True

        if self.have_auth and self.have_mess:
            self.ui.actionRun_matching.setEnabled(True)

    def runMatching(self):
        self.all_scores = list()
        self.matched_authorities = list()

        for m in self.mess:
            scores = [ [x, jellyfish.jaro_winkler(m, unicode(x))] for x in self.authorities]
            scores = sorted(scores, key=lambda score: -score[1])[0:10]
            self.all_scores.append(scores)
            self.matched_authorities.append(scores[0][0] if scores[0][1] > 0.6 else False)

        self.ui.match_table.setRowCount(len(self.mess))
        self.updateTable()

    def updateTable(self):
        for row in range(len(self.mess)):
            self.ui.match_table.setItem(row, 0, QtGui.QTableWidgetItem(self.mess[row]))
            if self.matched_authorities[row]:
                self.ui.match_table.setItem(row, 1, QtGui.QTableWidgetItem(self.matched_authorities[row]))

    def updateTopHits(self, row, column, oldrow, oldcolumn):
        self.ui.tophit_list.clear()
        for i in range(10):
            item = QtGui.QListWidgetItem(self.all_scores[row][i][0])
            self.ui.tophit_list.addItem(item)

        if row != -1: # row gets set to -1 after deleteMatch(): ignore it and keep the old current_run
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




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())