import sys, os
from threading import Thread
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from threading import Timer

#Define the window object
def ui(location):
	#Create window object
	qt_app = QApplication(sys.argv)
	#Load Web Engine to show localhost page
	web = QWebEngineView()
	#Set window title
	web.setWindowTitle("Calcy")
	#Size the window
	web.resize(900, 800)
	#Set the window icon as the brand logo
	scriptDir = os.path.dirname(os.path.realpath(__file__))
	web.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'icon.ico'))
	#Magnify the window just a bit
	web.setZoomFactor(1.2)
	#Load given URL
	web.load(QUrl(location))
	#Show the window object
	web.show()
	sys.exit(qt_app.exec_())

Timer(1,lambda: ui("http://calculator.coolcodersj.repl.co")).start()
