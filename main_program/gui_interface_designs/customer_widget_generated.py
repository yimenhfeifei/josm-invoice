# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer_widget_design.ui'
#
# Created: Wed Sep 21 15:46:17 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_customerWidget(object):
    def setupUi(self, customerWidget):
        customerWidget.setObjectName(_fromUtf8("customerWidget"))
        customerWidget.resize(283, 262)
        customerWidget.setWindowTitle(QtGui.QApplication.translate("customerWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(customerWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.customerGroupBox = QtGui.QGroupBox(customerWidget)
        self.customerGroupBox.setTitle(QtGui.QApplication.translate("customerWidget", "Customer", None, QtGui.QApplication.UnicodeUTF8))
        self.customerGroupBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.customerGroupBox.setFlat(False)
        self.customerGroupBox.setCheckable(False)
        self.customerGroupBox.setObjectName(_fromUtf8("customerGroupBox"))
        self.formLayout = QtGui.QFormLayout(self.customerGroupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.firstNameLabel = QtGui.QLabel(self.customerGroupBox)
        self.firstNameLabel.setText(QtGui.QApplication.translate("customerWidget", "First name", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLabel.setObjectName(_fromUtf8("firstNameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameEdit = QtGui.QLineEdit(self.customerGroupBox)
        self.firstNameEdit.setObjectName(_fromUtf8("firstNameEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.firstNameEdit)
        self.lastNameLabel = QtGui.QLabel(self.customerGroupBox)
        self.lastNameLabel.setText(QtGui.QApplication.translate("customerWidget", "Last name", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLabel.setObjectName(_fromUtf8("lastNameLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameEdit = QtGui.QLineEdit(self.customerGroupBox)
        self.lastNameEdit.setObjectName(_fromUtf8("lastNameEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lastNameEdit)
        self.houseNumberLabel = QtGui.QLabel(self.customerGroupBox)
        self.houseNumberLabel.setText(QtGui.QApplication.translate("customerWidget", "House number", None, QtGui.QApplication.UnicodeUTF8))
        self.houseNumberLabel.setObjectName(_fromUtf8("houseNumberLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.houseNumberLabel)
        self.houseNumberEdit = QtGui.QLineEdit(self.customerGroupBox)
        self.houseNumberEdit.setObjectName(_fromUtf8("houseNumberEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.houseNumberEdit)
        self.streetLabel = QtGui.QLabel(self.customerGroupBox)
        self.streetLabel.setText(QtGui.QApplication.translate("customerWidget", "Street", None, QtGui.QApplication.UnicodeUTF8))
        self.streetLabel.setObjectName(_fromUtf8("streetLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.streetLabel)
        self.streetEdit = QtGui.QLineEdit(self.customerGroupBox)
        self.streetEdit.setObjectName(_fromUtf8("streetEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.streetEdit)
        self.townLabel = QtGui.QLabel(self.customerGroupBox)
        self.townLabel.setText(QtGui.QApplication.translate("customerWidget", "Town", None, QtGui.QApplication.UnicodeUTF8))
        self.townLabel.setObjectName(_fromUtf8("townLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.townLabel)
        self.townEdit = QtGui.QLineEdit(self.customerGroupBox)
        self.townEdit.setObjectName(_fromUtf8("townEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.townEdit)
        self.postcodeLabel = QtGui.QLabel(self.customerGroupBox)
        self.postcodeLabel.setText(QtGui.QApplication.translate("customerWidget", "Postcode", None, QtGui.QApplication.UnicodeUTF8))
        self.postcodeLabel.setObjectName(_fromUtf8("postcodeLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.postcodeLabel)
        self.postcodeEdit = QtGui.QLineEdit(self.customerGroupBox)
        self.postcodeEdit.setObjectName(_fromUtf8("postcodeEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.postcodeEdit)
        self.vehicleRegistrationLabel = QtGui.QLabel(self.customerGroupBox)
        self.vehicleRegistrationLabel.setText(QtGui.QApplication.translate("customerWidget", "Vehicle Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLabel.setObjectName(_fromUtf8("vehicleRegistrationLabel"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.vehicleRegistrationLabel)
        self.customerRegEdit = QtGui.QLineEdit(self.customerGroupBox)
        self.customerRegEdit.setObjectName(_fromUtf8("customerRegEdit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.customerRegEdit)
        self.verticalLayout.addWidget(self.customerGroupBox)

        self.retranslateUi(customerWidget)
        QtCore.QMetaObject.connectSlotsByName(customerWidget)

    def retranslateUi(self, customerWidget):
        pass

