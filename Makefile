all: mainwindow rundialog selectcolumn preferencesdialog selectsheet

mainwindow: mainwindow.ui
	pyuic4 mainwindow.ui -o mainwindow.py

rundialog: rundialog.ui
	pyuic4 rundialog.ui -o rundialog.py

selectcolumn: selectcolumn.ui
	pyuic4 selectcolumn.ui -o selectcolumn.py

preferencesdialog: preferencesdialog.ui
	pyuic4 preferencesdialog.ui -o preferencesdialog.py

selectsheet: selectsheet.ui
	pyuic4 selectsheet.ui -o selectsheet.py
