# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payload_total_widget_design.ui'
#
# Created: Mon Sep 26 11:52:08 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_payloadTotalWidget(object):
    def setupUi(self, payloadTotalWidget):
        payloadTotalWidget.setObjectName(_fromUtf8("payloadTotalWidget"))
        payloadTotalWidget.resize(424, 107)
        payloadTotalWidget.setWindowTitle(QtGui.QApplication.translate("payloadTotalWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_2 = QtGui.QVBoxLayout(payloadTotalWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.payloadTotalBox = QtGui.QGroupBox(payloadTotalWidget)
        self.payloadTotalBox.setTitle(QtGui.QApplication.translate("payloadTotalWidget", "Payload Total", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTotalBox.setObjectName(_fromUtf8("payloadTotalBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.payloadTotalBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.payloadTotalLabel = QtGui.QLabel(self.payloadTotalBox)
        self.payloadTotalLabel.setText(QtGui.QApplication.translate("payloadTotalWidget", "00.00", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.payloadTotalLabel.setObjectName(_fromUtf8("payloadTotalLabel"))
        self.verticalLayout.addWidget(self.payloadTotalLabel)
        self.customTotalButton = QtGui.QPushButton(self.payloadTotalBox)
        self.customTotalButton.setText(QtGui.QApplication.translate("payloadTotalWidget", "Custom total", None, QtGui.QApplication.UnicodeUTF8))
        self.customTotalButton.setObjectName(_fromUtf8("customTotalButton"))
        self.verticalLayout.addWidget(self.customTotalButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.line = QtGui.QFrame(self.payloadTotalBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        spacerItem1 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.addPayloadButton = QtGui.QPushButton(self.payloadTotalBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addPayloadButton.sizePolicy().hasHeightForWidth())
        self.addPayloadButton.setSizePolicy(sizePolicy)
        self.addPayloadButton.setMinimumSize(QtCore.QSize(81, 0))
        self.addPayloadButton.setText(QtGui.QApplication.translate("payloadTotalWidget", "Add payload", None, QtGui.QApplication.UnicodeUTF8))
        self.addPayloadButton.setObjectName(_fromUtf8("addPayloadButton"))
        self.horizontalLayout.addWidget(self.addPayloadButton)
        self.verticalLayout_2.addWidget(self.payloadTotalBox)

        self.retranslateUi(payloadTotalWidget)
        QtCore.QMetaObject.connectSlotsByName(payloadTotalWidget)

    def retranslateUi(self, payloadTotalWidget):
        pass

