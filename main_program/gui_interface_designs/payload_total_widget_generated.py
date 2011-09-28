# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payload_total_widget_design.ui'
#
# Created: Wed Sep 28 14:18:58 2011
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
        payloadTotalWidget.resize(269, 111)
        payloadTotalWidget.setWindowTitle(QtGui.QApplication.translate("payloadTotalWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(payloadTotalWidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.payloadTotalBox = QtGui.QGroupBox(payloadTotalWidget)
        self.payloadTotalBox.setTitle(QtGui.QApplication.translate("payloadTotalWidget", "Payload Total", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTotalBox.setAlignment(QtCore.Qt.AlignCenter)
        self.payloadTotalBox.setObjectName(_fromUtf8("payloadTotalBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.payloadTotalBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.poundLabel = QtGui.QLabel(self.payloadTotalBox)
        self.poundLabel.setText(QtGui.QApplication.translate("payloadTotalWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">$</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.poundLabel.setObjectName(_fromUtf8("poundLabel"))
        self.horizontalLayout.addWidget(self.poundLabel)
        self.payloadTotalLabel = QtGui.QLabel(self.payloadTotalBox)
        self.payloadTotalLabel.setText(QtGui.QApplication.translate("payloadTotalWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"fake\"><span style=\" text-decoration: underline; color:#0000ff;\">00.00</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.payloadTotalLabel.setObjectName(_fromUtf8("payloadTotalLabel"))
        self.horizontalLayout.addWidget(self.payloadTotalLabel)
        spacerItem1 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.line = QtGui.QFrame(self.payloadTotalBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_2.addWidget(self.line)
        spacerItem3 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.addPayloadButton = QtGui.QPushButton(self.payloadTotalBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addPayloadButton.sizePolicy().hasHeightForWidth())
        self.addPayloadButton.setSizePolicy(sizePolicy)
        self.addPayloadButton.setMinimumSize(QtCore.QSize(81, 0))
        self.addPayloadButton.setText(QtGui.QApplication.translate("payloadTotalWidget", "Add payload", None, QtGui.QApplication.UnicodeUTF8))
        self.addPayloadButton.setObjectName(_fromUtf8("addPayloadButton"))
        self.horizontalLayout_2.addWidget(self.addPayloadButton)
        self.horizontalLayout_3.addWidget(self.payloadTotalBox)

        self.retranslateUi(payloadTotalWidget)
        QtCore.QMetaObject.connectSlotsByName(payloadTotalWidget)

    def retranslateUi(self, payloadTotalWidget):
        pass

