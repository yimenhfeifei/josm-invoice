# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payload_edit_dialog_design.ui'
#
# Created: Tue Sep 27 16:02:46 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_payloadEditDialog(object):
    def setupUi(self, payloadEditDialog):
        payloadEditDialog.setObjectName(_fromUtf8("payloadEditDialog"))
        payloadEditDialog.resize(296, 101)
        payloadEditDialog.setWindowTitle(QtGui.QApplication.translate("payloadEditDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(payloadEditDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(95, 22, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.payloadValueEdit = ValidatingLineEdit(payloadEditDialog)
        self.payloadValueEdit.setMaximumSize(QtCore.QSize(71, 25))
        self.payloadValueEdit.setToolTip(QtGui.QApplication.translate("payloadEditDialog", "Line edit that provides custom validation.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadValueEdit.setWhatsThis(QtGui.QApplication.translate("payloadEditDialog", "Base widget for custom validation.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadValueEdit.setStyleSheet(_fromUtf8(""))
        self.payloadValueEdit.setProperty("regexString", QtGui.QApplication.translate("payloadEditDialog", "value", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadValueEdit.setObjectName(_fromUtf8("payloadValueEdit"))
        self.gridLayout.addWidget(self.payloadValueEdit, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(94, 22, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cancelButton = QtGui.QPushButton(payloadEditDialog)
        self.cancelButton.setText(QtGui.QApplication.translate("payloadEditDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.acceptButton = QtGui.QPushButton(payloadEditDialog)
        self.acceptButton.setText(QtGui.QApplication.translate("payloadEditDialog", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.horizontalLayout.addWidget(self.acceptButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)

        self.retranslateUi(payloadEditDialog)
        QtCore.QMetaObject.connectSlotsByName(payloadEditDialog)

    def retranslateUi(self, payloadEditDialog):
        pass

from custom_widgets.validatingLineEdit import ValidatingLineEdit
