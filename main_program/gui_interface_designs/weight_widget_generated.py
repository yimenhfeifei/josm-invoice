# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weight_widget_design.ui'
#
# Created: Wed Sep 21 14:54:38 2011
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
        weightWidget.resize(169, 268)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(weightWidget.sizePolicy().hasHeightForWidth())
        weightWidget.setSizePolicy(sizePolicy)
        weightWidget.setWindowTitle(QtGui.QApplication.translate("weightWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.widget = QtGui.QWidget(weightWidget)
        self.widget.setGeometry(QtCore.QRect(12, 12, 144, 246))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.useGrossBox = QtGui.QGroupBox(self.widget)
        self.useGrossBox.setEnabled(True)
        self.useGrossBox.setTitle(QtGui.QApplication.translate("weightWidget", "Use gross weight", None, QtGui.QApplication.UnicodeUTF8))
        self.useGrossBox.setCheckable(True)
        self.useGrossBox.setChecked(False)
        self.useGrossBox.setObjectName(_fromUtf8("useGrossBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.useGrossBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.grossBox = QtGui.QGroupBox(self.useGrossBox)
        self.grossBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grossBox.sizePolicy().hasHeightForWidth())
        self.grossBox.setSizePolicy(sizePolicy)
        self.grossBox.setTitle(QtGui.QApplication.translate("weightWidget", "Gross", None, QtGui.QApplication.UnicodeUTF8))
        self.grossBox.setCheckable(False)
        self.grossBox.setChecked(False)
        self.grossBox.setObjectName(_fromUtf8("grossBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.grossBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.grossEdit = QtGui.QLineEdit(self.grossBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grossEdit.sizePolicy().hasHeightForWidth())
        self.grossEdit.setSizePolicy(sizePolicy)
        self.grossEdit.setMaximumSize(QtCore.QSize(71, 25))
        self.grossEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grossEdit.setObjectName(_fromUtf8("grossEdit"))
        self.horizontalLayout_2.addWidget(self.grossEdit)
        self.verticalLayout.addWidget(self.grossBox)
        self.tareBox = QtGui.QGroupBox(self.useGrossBox)
        self.tareBox.setEnabled(False)
        self.tareBox.setTitle(QtGui.QApplication.translate("weightWidget", "Tare", None, QtGui.QApplication.UnicodeUTF8))
        self.tareBox.setCheckable(False)
        self.tareBox.setChecked(False)
        self.tareBox.setObjectName(_fromUtf8("tareBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tareBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tareEdit = QtGui.QLineEdit(self.tareBox)
        self.tareEdit.setMaximumSize(QtCore.QSize(71, 25))
        self.tareEdit.setObjectName(_fromUtf8("tareEdit"))
        self.horizontalLayout_3.addWidget(self.tareEdit)
        self.verticalLayout.addWidget(self.tareBox)
        self.verticalLayout_2.addWidget(self.useGrossBox)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.netBox = QtGui.QGroupBox(self.widget)
        self.netBox.setStyleSheet(_fromUtf8(""))
        self.netBox.setTitle(QtGui.QApplication.translate("weightWidget", "Net weight (Kg)", None, QtGui.QApplication.UnicodeUTF8))
        self.netBox.setObjectName(_fromUtf8("netBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.netBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.netEdit = QtGui.QLineEdit(self.netBox)
        self.netEdit.setMaximumSize(QtCore.QSize(71, 25))
        self.netEdit.setObjectName(_fromUtf8("netEdit"))
        self.horizontalLayout.addWidget(self.netEdit)
        self.verticalLayout_2.addWidget(self.netBox)

        self.retranslateUi(weightWidget)
        QtCore.QMetaObject.connectSlotsByName(weightWidget)

    def retranslateUi(self, weightWidget):
        pass

