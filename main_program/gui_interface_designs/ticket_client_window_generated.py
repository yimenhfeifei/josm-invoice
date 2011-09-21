# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticket_client_window_design.ui'
#
# Created: Wed Sep 21 14:54:37 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ticketClientWindow(object):
    def setupUi(self, ticketClientWindow):
        ticketClientWindow.setObjectName(_fromUtf8("ticketClientWindow"))
        ticketClientWindow.resize(720, 575)
        ticketClientWindow.setMinimumSize(QtCore.QSize(626, 62))
        ticketClientWindow.setWindowTitle(QtGui.QApplication.translate("ticketClientWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(ticketClientWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        ticketClientWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ticketClientWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("ticketClientWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setTitle(QtGui.QApplication.translate("ticketClientWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        ticketClientWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ticketClientWindow)
        self.statusbar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ticketClientWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(ticketClientWindow)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("ticketClientWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        ticketClientWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtGui.QAction(ticketClientWindow)
        self.actionExit.setText(QtGui.QApplication.translate("ticketClientWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionOrchard_Suite = QtGui.QAction(ticketClientWindow)
        self.actionOrchard_Suite.setText(QtGui.QApplication.translate("ticketClientWindow", "Orchard Suite", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOrchard_Suite.setObjectName(_fromUtf8("actionOrchard_Suite"))
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionOrchard_Suite)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(ticketClientWindow)
        QtCore.QMetaObject.connectSlotsByName(ticketClientWindow)

    def retranslateUi(self, ticketClientWindow):
        pass

