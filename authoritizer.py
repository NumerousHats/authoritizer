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

        self.ui.ok_button.clicked.connect(self.updateMatch)


    def importAuth(self):
        df = pd.read_csv("testdat/huge_real_life.csv")
        self.authorities = df['canonical firm'].dropna().values.tolist()
        self.authorities = list(set(self.authorities))
        self.authorities = [unicode(x) for x in self.authorities]
        self.have_auth = True

        if self.have_auth and self.have_mess:
            self.ui.actionRun_matching.setEnabled(self, True)

    def importMessy(self):
        df = pd.read_csv("testdat/huge_real_life.csv")
        self.mess = df['vendor'].dropna().values.tolist()
        self.mess = list(set(self.mess))
        self.mess = [unicode(x) for x in self.mess]
        self.have_mess = True

        if self.have_auth and self.have_mess:
            self.ui.actionRun_matching.setEnabled(True)

    def runMatching(self):
        self.all_scores = dict()
        for m in self.mess:
            scores = [ [x, jellyfish.jaro_winkler(m, unicode(x))] for x in self.authorities]
            scores = sorted(scores, key=lambda score: -score[1])[0:9]
            self.all_scores[m] = scores

        self.updateTable()

    def updateTable(self):
        self.ui.match_table.setRowCount(len(self.all_scores))
        len_table = len(self.all_scores)
        keys = self.all_scores.keys()

        for row in range(len_table):
            self.ui.match_table.setItem(row, 0, QtGui.QTableWidgetItem(keys[row]))


        # update table

    def updateMatch(self):
        print "Yowza!!"




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())