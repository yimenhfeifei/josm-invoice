# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'material_widget_design.ui'
#
# Created: Wed Sep 21 14:54:40 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_materialWidget(object):
    def setupUi(self, materialWidget):
        materialWidget.setObjectName(_fromUtf8("materialWidget"))
        materialWidget.resize(215, 226)
        materialWidget.setWindowTitle(QtGui.QApplication.translate("materialWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(materialWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.materialTable = QtGui.QTableWidget(materialWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.materialTable.sizePolicy().hasHeightForWidth())
        self.materialTable.setSizePolicy(sizePolicy)
        self.materialTable.setObjectName(_fromUtf8("materialTable"))
        self.materialTable.setColumnCount(2)
        self.materialTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("materialWidget", "Material", None, QtGui.QApplication.UnicodeUTF8))
        self.materialTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("materialWidget", "Price Per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.materialTable.setHorizontalHeaderItem(1, item)
        self.materialTable.horizontalHeader().setCascadingSectionResizes(True)
        self.materialTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.materialTable)

        self.retranslateUi(materialWidget)
        QtCore.QMetaObject.connectSlotsByName(materialWidget)

    def retranslateUi(self, materialWidget):
        item = self.materialTable.horizontalHeaderItem(0)
        item = self.materialTable.horizontalHeaderItem(1)

