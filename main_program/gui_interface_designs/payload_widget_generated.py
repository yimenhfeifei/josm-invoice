# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payload_widget_design.ui'
#
# Created: Thu Sep 22 11:19:26 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_payloadWidget(object):
    def setupUi(self, payloadWidget):
        payloadWidget.setObjectName(_fromUtf8("payloadWidget"))
        payloadWidget.resize(451, 282)
        payloadWidget.setWindowTitle(QtGui.QApplication.translate("payloadWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(payloadWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.weightWidget = WeightWidget(payloadWidget)
        self.weightWidget.setToolTip(QtGui.QApplication.translate("payloadWidget", "Custom weight entry.", None, QtGui.QApplication.UnicodeUTF8))
        self.weightWidget.setWhatsThis(QtGui.QApplication.translate("payloadWidget", "Weight widget.", None, QtGui.QApplication.UnicodeUTF8))
        self.weightWidget.setObjectName(_fromUtf8("weightWidget"))
        self.horizontalLayout.addWidget(self.weightWidget)
        self.materialWidget = MaterialWidget(payloadWidget)
        self.materialWidget.setToolTip(QtGui.QApplication.translate("payloadWidget", "Material selection.", None, QtGui.QApplication.UnicodeUTF8))
        self.materialWidget.setWhatsThis(QtGui.QApplication.translate("payloadWidget", "Material selection widget.", None, QtGui.QApplication.UnicodeUTF8))
        self.materialWidget.setObjectName(_fromUtf8("materialWidget"))
        self.horizontalLayout.addWidget(self.materialWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(payloadWidget)
        QtCore.QMetaObject.connectSlotsByName(payloadWidget)

    def retranslateUi(self, payloadWidget):
        pass

from custom_widgets.weightWidget import WeightWidget
from custom_widgets.materialWidget import MaterialWidget
