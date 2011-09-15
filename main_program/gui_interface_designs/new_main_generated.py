# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_main_design.ui'
#
# Created: Thu Sep 15 16:49:21 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainClientWindow(object):
    def setupUi(self, mainClientWindow):
        mainClientWindow.setObjectName(_fromUtf8("mainClientWindow"))
        mainClientWindow.resize(626, 516)
        mainClientWindow.setMinimumSize(QtCore.QSize(626, 62))
        mainClientWindow.setWindowTitle(QtGui.QApplication.translate("mainClientWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(mainClientWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.homeWidget = HomeWidget(self.centralwidget)
        self.homeWidget.setMinimumSize(QtCore.QSize(608, 533))
        self.homeWidget.setToolTip(QtGui.QApplication.translate("mainClientWindow", "Select material.", None, QtGui.QApplication.UnicodeUTF8))
        self.homeWidget.setWhatsThis(QtGui.QApplication.translate("mainClientWindow", "Allows selecting of material.", None, QtGui.QApplication.UnicodeUTF8))
        self.homeWidget.setObjectName(_fromUtf8("homeWidget"))
        self.horizontalLayout.addWidget(self.homeWidget)
        mainClientWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainClientWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("mainClientWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setTitle(QtGui.QApplication.translate("mainClientWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        mainClientWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainClientWindow)
        self.statusbar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainClientWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(mainClientWindow)
        self.actionExit.setText(QtGui.QApplication.translate("mainClientWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionOrchard_Suite = QtGui.QAction(mainClientWindow)
        self.actionOrchard_Suite.setText(QtGui.QApplication.translate("mainClientWindow", "Orchard Suite", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOrchard_Suite.setObjectName(_fromUtf8("actionOrchard_Suite"))
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionOrchard_Suite)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(mainClientWindow)
        QtCore.QMetaObject.connectSlotsByName(mainClientWindow)

    def retranslateUi(self, mainClientWindow):
        pass

from custom_widgets.homeWidget import HomeWidget
