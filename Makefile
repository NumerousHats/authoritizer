all: mainwindow importauthority importmessy rundialog startdialog

mainwindow: mainwindow.ui
	pyuic4 mainwindow.ui -o mainwindow.py

importauthority: importauthority.ui
	pyuic4 importauthority.ui -o importauthority.py

importmessy: importmessy.ui
	pyuic4 importmessy.ui -o importmessy.py

rundialog: rundialog.ui
	pyuic4 rundialog.ui -o rundialog.py

startdialog: startdialog.ui
	pyuic4 startdialog.ui -o startdialog.py
