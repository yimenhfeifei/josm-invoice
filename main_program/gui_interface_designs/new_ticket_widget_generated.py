# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_ticket_widget_design.ui'
#
# Created: Mon Sep 26 11:52:07 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_newTicketWidget(object):
    def setupUi(self, newTicketWidget):
        newTicketWidget.setObjectName(_fromUtf8("newTicketWidget"))
        newTicketWidget.resize(886, 584)
        newTicketWidget.setWindowTitle(QtGui.QApplication.translate("newTicketWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadsGroupBox = QtGui.QGroupBox(newTicketWidget)
        self.payloadsGroupBox.setGeometry(QtCore.QRect(280, 10, 601, 571))
        self.payloadsGroupBox.setTitle(QtGui.QApplication.translate("newTicketWidget", "Payloads", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadsGroupBox.setObjectName(_fromUtf8("payloadsGroupBox"))
        self.layoutWidget = QtGui.QWidget(self.payloadsGroupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(400, 390, 133, 98))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("newTicketWidget", "Ticket total", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ticketTotalLabel = QtGui.QLabel(self.groupBox_2)
        self.ticketTotalLabel.setText(QtGui.QApplication.translate("newTicketWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">$ 3400.00</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ticketTotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ticketTotalLabel.setObjectName(_fromUtf8("ticketTotalLabel"))
        self.horizontalLayout_2.addWidget(self.ticketTotalLabel)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.reviewTicketButton = QtGui.QCommandLinkButton(self.layoutWidget)
        self.reviewTicketButton.setEnabled(False)
        self.reviewTicketButton.setMinimumSize(QtCore.QSize(131, 0))
        self.reviewTicketButton.setMaximumSize(QtCore.QSize(131, 16777215))
        self.reviewTicketButton.setText(QtGui.QApplication.translate("newTicketWidget", "Review ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.reviewTicketButton.setObjectName(_fromUtf8("reviewTicketButton"))
        self.verticalLayout_3.addWidget(self.reviewTicketButton)
        self.payloadWidget = PayloadWidget(self.payloadsGroupBox)
        self.payloadWidget.setGeometry(QtCore.QRect(10, 20, 601, 281))
        self.payloadWidget.setToolTip(QtGui.QApplication.translate("newTicketWidget", "Payload details.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadWidget.setWhatsThis(QtGui.QApplication.translate("newTicketWidget", "Payload widget.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadWidget.setObjectName(_fromUtf8("payloadWidget"))
        self.payloadTotalWidget = PayloadTotalWidget(self.payloadsGroupBox)
        self.payloadTotalWidget.setGeometry(QtCore.QRect(60, 290, 254, 101))
        self.payloadTotalWidget.setToolTip(QtGui.QApplication.translate("newTicketWidget", "Payload total display.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTotalWidget.setWhatsThis(QtGui.QApplication.translate("newTicketWidget", "Payload total.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTotalWidget.setObjectName(_fromUtf8("payloadTotalWidget"))
        self.payloadTableWidget = PayloadTableWidget(self.payloadsGroupBox)
        self.payloadTableWidget.setGeometry(QtCore.QRect(20, 410, 321, 151))
        self.payloadTableWidget.setToolTip(QtGui.QApplication.translate("newTicketWidget", "Customer details.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTableWidget.setWhatsThis(QtGui.QApplication.translate("newTicketWidget", "Customer details widgte.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.payloadTableWidget.setColumnCount(4)
        self.payloadTableWidget.setObjectName(_fromUtf8("payloadTableWidget"))
        self.payloadTableWidget.setRowCount(0)
        self.deletePayloadButton = QtGui.QPushButton(self.payloadsGroupBox)
        self.deletePayloadButton.setGeometry(QtCore.QRect(340, 450, 51, 26))
        self.deletePayloadButton.setText(QtGui.QApplication.translate("newTicketWidget", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.deletePayloadButton.setObjectName(_fromUtf8("deletePayloadButton"))
        self.customerWidget = CustomerWidget(newTicketWidget)
        self.customerWidget.setGeometry(QtCore.QRect(0, 0, 290, 266))
        self.customerWidget.setToolTip(QtGui.QApplication.translate("newTicketWidget", "Customer details.", None, QtGui.QApplication.UnicodeUTF8))
        self.customerWidget.setWhatsThis(QtGui.QApplication.translate("newTicketWidget", "Customer details widgte.", None, QtGui.QApplication.UnicodeUTF8))
        self.customerWidget.setObjectName(_fromUtf8("customerWidget"))

        self.retranslateUi(newTicketWidget)
        QtCore.QMetaObject.connectSlotsByName(newTicketWidget)

    def retranslateUi(self, newTicketWidget):
        pass

from custom_widgets.payloadWidget import PayloadWidget
from custom_widgets.payloadTableWidget import PayloadTableWidget
from custom_widgets.payloadTotalWidget import PayloadTotalWidget
from custom_widgets.customerWidget import CustomerWidget
