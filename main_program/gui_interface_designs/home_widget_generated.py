# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home_widget_design.ui'
#
# Created: Mon Sep 26 11:52:01 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(595, 449)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.newTicketButton = QtGui.QPushButton(Form)
        self.newTicketButton.setMinimumSize(QtCore.QSize(80, 26))
        self.newTicketButton.setText(QtGui.QApplication.translate("Form", "New Ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.newTicketButton.setObjectName(_fromUtf8("newTicketButton"))
        self.verticalLayout.addWidget(self.newTicketButton)
        self.verifyTicketButton = QtGui.QPushButton(Form)
        self.verifyTicketButton.setMinimumSize(QtCore.QSize(80, 26))
        self.verifyTicketButton.setText(QtGui.QApplication.translate("Form", "Verify Ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.verifyTicketButton.setObjectName(_fromUtf8("verifyTicketButton"))
        self.verticalLayout.addWidget(self.verifyTicketButton)
        self.searchTicketsButton = QtGui.QPushButton(Form)
        self.searchTicketsButton.setMinimumSize(QtCore.QSize(101, 26))
        self.searchTicketsButton.setText(QtGui.QApplication.translate("Form", "Search Tickets", None, QtGui.QApplication.UnicodeUTF8))
        self.searchTicketsButton.setObjectName(_fromUtf8("searchTicketsButton"))
        self.verticalLayout.addWidget(self.searchTicketsButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

