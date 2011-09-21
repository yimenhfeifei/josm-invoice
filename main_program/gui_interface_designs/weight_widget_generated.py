# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weight_widget_design.ui'
#
# Created: Wed Sep 21 09:19:01 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_weightWidget(object):
    def setupUi(self, weightWidget):
        weightWidget.setObjectName(_fromUtf8("weightWidget"))
        weightWidget.resize(122, 223)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(weightWidget.sizePolicy().hasHeightForWidth())
        weightWidget.setSizePolicy(sizePolicy)
        weightWidget.setWindowTitle(QtGui.QApplication.translate("weightWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.widget = QtGui.QWidget(weightWidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 95, 200))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.grossGroupBox = QtGui.QGroupBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grossGroupBox.sizePolicy().hasHeightForWidth())
        self.grossGroupBox.setSizePolicy(sizePolicy)
        self.grossGroupBox.setTitle(QtGui.QApplication.translate("weightWidget", "Gross", None, QtGui.QApplication.UnicodeUTF8))
        self.grossGroupBox.setObjectName(_fromUtf8("grossGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.grossGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.grossEdit = QtGui.QLineEdit(self.grossGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grossEdit.sizePolicy().hasHeightForWidth())
        self.grossEdit.setSizePolicy(sizePolicy)
        self.grossEdit.setMaximumSize(QtCore.QSize(71, 25))
        self.grossEdit.setObjectName(_fromUtf8("grossEdit"))
        self.verticalLayout.addWidget(self.grossEdit)
        self.verticalLayout_4.addWidget(self.grossGroupBox)
        self.tareGroupBox = QtGui.QGroupBox(self.widget)
        self.tareGroupBox.setTitle(QtGui.QApplication.translate("weightWidget", "Tare", None, QtGui.QApplication.UnicodeUTF8))
        self.tareGroupBox.setObjectName(_fromUtf8("tareGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tareGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tareEdit = QtGui.QLineEdit(self.tareGroupBox)
        self.tareEdit.setMaximumSize(QtCore.QSize(71, 25))
        self.tareEdit.setObjectName(_fromUtf8("tareEdit"))
        self.verticalLayout_2.addWidget(self.tareEdit)
        self.verticalLayout_4.addWidget(self.tareGroupBox)
        self.netGroupBox = QtGui.QGroupBox(self.widget)
        self.netGroupBox.setTitle(QtGui.QApplication.translate("weightWidget", "Net", None, QtGui.QApplication.UnicodeUTF8))
        self.netGroupBox.setObjectName(_fromUtf8("netGroupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.netGroupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.netEdit = QtGui.QLineEdit(self.netGroupBox)
        self.netEdit.setMaximumSize(QtCore.QSize(71, 25))
        self.netEdit.setObjectName(_fromUtf8("netEdit"))
        self.verticalLayout_3.addWidget(self.netEdit)
        self.verticalLayout_4.addWidget(self.netGroupBox)

        self.retranslateUi(weightWidget)
        QtCore.QMetaObject.connectSlotsByName(weightWidget)

    def retranslateUi(self, weightWidget):
        pass

