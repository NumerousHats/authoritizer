import sys, time
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button = QtGui.QPushButton('Test', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        file = range(30)
        numberOfLinesInFile = len(file)
        progressWasCancelled = False
        progress = QtGui.QProgressDialog(
            "Parsing Log", "Stop", 0, numberOfLinesInFile, self)
        progress.setWindowModality(QtCore.Qt.WindowModal)
        progress.setMinimumDuration(0)
        for lineNumber, line in enumerate(file):
            progress.setValue(lineNumber)
            if progress.wasCanceled():
                progressWasCancelled = True
                break
            time.sleep(0.05)
        progress.setValue(numberOfLinesInFile)
        print 'cancelled', progress.wasCanceled(), progressWasCancelled
        progress.deleteLater()

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())