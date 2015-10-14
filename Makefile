all: mainwindow rundialog startdialog selectcolumn preferencesdialog

mainwindow: mainwindow.ui
	pyuic4 mainwindow.ui -o mainwindow.py

rundialog: rundialog.ui
	pyuic4 rundialog.ui -o rundialog.py

startdialog: startdialog.ui
	pyuic4 startdialog.ui -o startdialog.py

selectcolumn: selectcolumn.ui
	pyuic4 selectcolumn.ui -o selectcolumn.py

preferencesdialog: preferencesdialog.ui
	pyuic4 preferencesdialog.ui -o preferencesdialog.py
