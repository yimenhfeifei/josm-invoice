# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_ticket_widget_design.ui'
#
# Created: Thu Sep 29 11:38:33 2011
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
        newTicketWidget.resize(973, 619)
        newTicketWidget.setMinimumSize(QtCore.QSize(836, 535))
        newTicketWidget.setWindowTitle(QtGui.QApplication.translate("newTicketWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(newTicketWidget)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.customerWidget = CustomerWidget(newTicketWidget)
        self.customerWidget.setToolTip(QtGui.QApplication.translate("newTicketWidget", "Customer details.", None, QtGui.QApplication.UnicodeUTF8))
        self.customerWidget.setWhatsThis(QtGui.QApplication.translate("newTicketWidget", "Customer details widgte.", None, QtGui.QApplication.UnicodeUTF8))
        self.customerWidget.setObjectName(_fromUtf8("customerWidget"))
        self.horizontalLayout_5.addWidget(self.customerWidget)
        self.payloadsGroupBox = QtGui.QGroupBox(newTicketWidget)
        self.payloadsGroupBox.setTitle(QtGui.QApplication.translate("newTicketWidget", "Payloads", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadsGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.payloadsGroupBox.setObjectName(_fromUtf8("payloadsGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.payloadsGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.payloadWidget = PayloadWidget(self.payloadsGroupBox)
        self.payloadWidget.setToolTip(QtGui.QApplication.translate("newTicketWidget", "Payload details.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadWidget.setWhatsThis(QtGui.QApplication.translate("newTicketWidget", "Payload widget.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadWidget.setObjectName(_fromUtf8("payloadWidget"))
        self.verticalLayout_2.addWidget(self.payloadWidget)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.payloadTotalWidget = PayloadTotalWidget(self.payloadsGroupBox)
        self.payloadTotalWidget.setToolTip(QtGui.QApplication.translate("newTicketWidget", "Payload total display.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTotalWidget.setWhatsThis(QtGui.QApplication.translate("newTicketWidget", "Payload total.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTotalWidget.setObjectName(_fromUtf8("payloadTotalWidget"))
        self.horizontalLayout_3.addWidget(self.payloadTotalWidget)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.payloadTableWidget = PayloadTableWidget(self.payloadsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.payloadTableWidget.sizePolicy().hasHeightForWidth())
        self.payloadTableWidget.setSizePolicy(sizePolicy)
        self.payloadTableWidget.setMinimumSize(QtCore.QSize(351, 160))
        self.payloadTableWidget.setToolTip(QtGui.QApplication.translate("newTicketWidget", "Customer details.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTableWidget.setWhatsThis(QtGui.QApplication.translate("newTicketWidget", "Customer details widgte.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.payloadTableWidget.setAlternatingRowColors(True)
        self.payloadTableWidget.setColumnCount(4)
        self.payloadTableWidget.setObjectName(_fromUtf8("payloadTableWidget"))
        self.payloadTableWidget.setRowCount(0)
        self.payloadTableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.payloadTableWidget.horizontalHeader().setMinimumSectionSize(70)
        self.payloadTableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.payloadTableWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem2 = QtGui.QSpacerItem(20, 68, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(78, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.payloadsGroupBox)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("newTicketWidget", "Ticket total", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem4 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setText(QtGui.QApplication.translate("newTicketWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">$</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.ticketTotalLabel = QtGui.QLabel(self.groupBox_2)
        self.ticketTotalLabel.setText(QtGui.QApplication.translate("newTicketWidget", "00.00", None, QtGui.QApplication.UnicodeUTF8))
        self.ticketTotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ticketTotalLabel.setObjectName(_fromUtf8("ticketTotalLabel"))
        self.horizontalLayout.addWidget(self.ticketTotalLabel)
        spacerItem5 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.reviewTicketButton = QtGui.QCommandLinkButton(self.payloadsGroupBox)
        self.reviewTicketButton.setEnabled(False)
        self.reviewTicketButton.setMinimumSize(QtCore.QSize(131, 0))
        self.reviewTicketButton.setMaximumSize(QtCore.QSize(131, 16777215))
        self.reviewTicketButton.setText(QtGui.QApplication.translate("newTicketWidget", "Review ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.reviewTicketButton.setObjectName(_fromUtf8("reviewTicketButton"))
        self.verticalLayout_3.addWidget(self.reviewTicketButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(88, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 2, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addWidget(self.payloadsGroupBox)

        self.retranslateUi(newTicketWidget)
        QtCore.QMetaObject.connectSlotsByName(newTicketWidget)

    def retranslateUi(self, newTicketWidget):
        pass

from custom_widgets.payloadWidget import PayloadWidget
from custom_widgets.payloadTableWidget import PayloadTableWidget
from custom_widgets.payloadTotalWidget import PayloadTotalWidget
from custom_widgets.customerWidget import CustomerWidget
