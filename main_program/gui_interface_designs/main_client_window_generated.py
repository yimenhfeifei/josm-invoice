# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_client_window_design.ui'
#
# Created: Thu Sep 15 16:49:22 2011
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
        mainClientWindow.resize(519, 528)
        mainClientWindow.setWindowTitle(QtGui.QApplication.translate("mainClientWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(mainClientWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(501, 441))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(20, 20, 451, 87))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.newTicketButton = QtGui.QCommandLinkButton(self.widget)
        self.newTicketButton.setMinimumSize(QtCore.QSize(121, 41))
        self.newTicketButton.setMaximumSize(QtCore.QSize(121, 41))
        self.newTicketButton.setText(QtGui.QApplication.translate("mainClientWindow", "New Ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.newTicketButton.setObjectName(_fromUtf8("newTicketButton"))
        self.verticalLayout.addWidget(self.newTicketButton)
        self.verifyTicketButton = QtGui.QCommandLinkButton(self.widget)
        self.verifyTicketButton.setText(QtGui.QApplication.translate("mainClientWindow", "Verify Ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.verifyTicketButton.setObjectName(_fromUtf8("verifyTicketButton"))
        self.verticalLayout.addWidget(self.verifyTicketButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(128, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.searchTicketsButton = QtGui.QCommandLinkButton(self.widget)
        self.searchTicketsButton.setMinimumSize(QtCore.QSize(141, 41))
        self.searchTicketsButton.setMaximumSize(QtCore.QSize(141, 41))
        self.searchTicketsButton.setText(QtGui.QApplication.translate("mainClientWindow", "Search Tickets", None, QtGui.QApplication.UnicodeUTF8))
        self.searchTicketsButton.setObjectName(_fromUtf8("searchTicketsButton"))
        self.horizontalLayout.addWidget(self.searchTicketsButton)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        mainClientWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainClientWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 519, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("mainClientWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setTitle(QtGui.QApplication.translate("mainClientWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setTitle(QtGui.QApplication.translate("mainClientWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuServer = QtGui.QMenu(self.menubar)
        self.menuServer.setTitle(QtGui.QApplication.translate("mainClientWindow", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.menuServer.setObjectName(_fromUtf8("menuServer"))
        mainClientWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainClientWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainClientWindow.setStatusBar(self.statusbar)
        self.actionOptions = QtGui.QAction(mainClientWindow)
        self.actionOptions.setText(QtGui.QApplication.translate("mainClientWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOptions.setObjectName(_fromUtf8("actionOptions"))
        self.actionExit = QtGui.QAction(mainClientWindow)
        self.actionExit.setText(QtGui.QApplication.translate("mainClientWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(mainClientWindow)
        self.actionAbout.setText(QtGui.QApplication.translate("mainClientWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionConnect = QtGui.QAction(mainClientWindow)
        self.actionConnect.setText(QtGui.QApplication.translate("mainClientWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionDisconnect = QtGui.QAction(mainClientWindow)
        self.actionDisconnect.setText(QtGui.QApplication.translate("mainClientWindow", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisconnect.setObjectName(_fromUtf8("actionDisconnect"))
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionOptions)
        self.menuAbout.addAction(self.actionAbout)
        self.menuServer.addAction(self.actionConnect)
        self.menuServer.addAction(self.actionDisconnect)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuServer.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(mainClientWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainClientWindow)

    def retranslateUi(self, mainClientWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("mainClientWindow", "Ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("mainClientWindow", "Materials", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("mainClientWindow", "Money Pool", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("mainClientWindow", "Stocks", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QtGui.QApplication.translate("mainClientWindow", "Invoice", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("mainClientWindow", "Summary", None, QtGui.QApplication.UnicodeUTF8))

import dockwidgets_rc
