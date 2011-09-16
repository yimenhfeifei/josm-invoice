# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verify_ticket_dialog_design.ui'
#
# Created: Fri Sep 16 16:29:29 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_verifyTicketDialog(object):
    def setupUi(self, verifyTicketDialog):
        verifyTicketDialog.setObjectName(_fromUtf8("verifyTicketDialog"))
        verifyTicketDialog.resize(486, 483)
        verifyTicketDialog.setWindowTitle(QtGui.QApplication.translate("verifyTicketDialog", "Verify Ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_2 = QtGui.QVBoxLayout(verifyTicketDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scanButton = QtGui.QToolButton(verifyTicketDialog)
        self.scanButton.setMinimumSize(QtCore.QSize(114, 65))
        self.scanButton.setMaximumSize(QtCore.QSize(114, 65))
        self.scanButton.setText(QtGui.QApplication.translate("verifyTicketDialog", "Auto scan ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.scanButton.setIconSize(QtCore.QSize(40, 40))
        self.scanButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.scanButton.setArrowType(QtCore.Qt.NoArrow)
        self.scanButton.setObjectName(_fromUtf8("scanButton"))
        self.verticalLayout.addWidget(self.scanButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(verifyTicketDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(51, 25))
        self.label.setMaximumSize(QtCore.QSize(51, 25))
        self.label.setText(QtGui.QApplication.translate("verifyTicketDialog", "Hash ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.hashIdLineEdit = QtGui.QLineEdit(verifyTicketDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hashIdLineEdit.sizePolicy().hasHeightForWidth())
        self.hashIdLineEdit.setSizePolicy(sizePolicy)
        self.hashIdLineEdit.setMinimumSize(QtCore.QSize(321, 25))
        self.hashIdLineEdit.setMaximumSize(QtCore.QSize(321, 25))
        self.hashIdLineEdit.setObjectName(_fromUtf8("hashIdLineEdit"))
        self.horizontalLayout.addWidget(self.hashIdLineEdit)
        self.submitButton = QtGui.QPushButton(verifyTicketDialog)
        self.submitButton.setText(QtGui.QApplication.translate("verifyTicketDialog", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.horizontalLayout.addWidget(self.submitButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 358, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(verifyTicketDialog)
        QtCore.QMetaObject.connectSlotsByName(verifyTicketDialog)

    def retranslateUi(self, verifyTicketDialog):
        pass

