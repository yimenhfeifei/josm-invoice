# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vehicle_dialog_design.ui'
#
# Created: Thu Jul 21 11:23:00 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_vehicleDialog(object):
    def setupUi(self, vehicleDialog):
        vehicleDialog.setObjectName(_fromUtf8("vehicleDialog"))
        vehicleDialog.resize(248, 313)
        vehicleDialog.setMinimumSize(QtCore.QSize(248, 313))
        vehicleDialog.setStyleSheet(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(vehicleDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.typeLabel = QtGui.QLabel(vehicleDialog)
        self.typeLabel.setMinimumSize(QtCore.QSize(31, 16))
        self.typeLabel.setMaximumSize(QtCore.QSize(31, 16))
        self.typeLabel.setObjectName(_fromUtf8("typeLabel"))
        self.gridLayout.addWidget(self.typeLabel, 0, 0, 1, 1)
        self.typeCombobox = QtGui.QComboBox(vehicleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeCombobox.sizePolicy().hasHeightForWidth())
        self.typeCombobox.setSizePolicy(sizePolicy)
        self.typeCombobox.setMinimumSize(QtCore.QSize(161, 25))
        self.typeCombobox.setMaximumSize(QtCore.QSize(161, 25))
        self.typeCombobox.setObjectName(_fromUtf8("typeCombobox"))
        self.gridLayout.addWidget(self.typeCombobox, 0, 1, 1, 3)
        self.makeLabel = QtGui.QLabel(vehicleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.makeLabel.sizePolicy().hasHeightForWidth())
        self.makeLabel.setSizePolicy(sizePolicy)
        self.makeLabel.setMinimumSize(QtCore.QSize(32, 16))
        self.makeLabel.setMaximumSize(QtCore.QSize(32, 16))
        self.makeLabel.setObjectName(_fromUtf8("makeLabel"))
        self.gridLayout.addWidget(self.makeLabel, 1, 0, 1, 1)
        self.makeLineEdit = ValidatingLineEdit(vehicleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.makeLineEdit.sizePolicy().hasHeightForWidth())
        self.makeLineEdit.setSizePolicy(sizePolicy)
        self.makeLineEdit.setMinimumSize(QtCore.QSize(161, 25))
        self.makeLineEdit.setMaximumSize(QtCore.QSize(161, 25))
        self.makeLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.makeLineEdit.setObjectName(_fromUtf8("makeLineEdit"))
        self.gridLayout.addWidget(self.makeLineEdit, 1, 1, 1, 3)
        self.modelLabel = QtGui.QLabel(vehicleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelLabel.sizePolicy().hasHeightForWidth())
        self.modelLabel.setSizePolicy(sizePolicy)
        self.modelLabel.setMinimumSize(QtCore.QSize(36, 16))
        self.modelLabel.setMaximumSize(QtCore.QSize(36, 16))
        self.modelLabel.setObjectName(_fromUtf8("modelLabel"))
        self.gridLayout.addWidget(self.modelLabel, 2, 0, 1, 1)
        self.modelLineEdit = ValidatingLineEdit(vehicleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelLineEdit.sizePolicy().hasHeightForWidth())
        self.modelLineEdit.setSizePolicy(sizePolicy)
        self.modelLineEdit.setMinimumSize(QtCore.QSize(161, 25))
        self.modelLineEdit.setMaximumSize(QtCore.QSize(161, 25))
        self.modelLineEdit.setObjectName(_fromUtf8("modelLineEdit"))
        self.gridLayout.addWidget(self.modelLineEdit, 2, 1, 1, 3)
        self.colourLabel = QtGui.QLabel(vehicleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colourLabel.sizePolicy().hasHeightForWidth())
        self.colourLabel.setSizePolicy(sizePolicy)
        self.colourLabel.setMinimumSize(QtCore.QSize(39, 16))
        self.colourLabel.setMaximumSize(QtCore.QSize(39, 16))
        self.colourLabel.setObjectName(_fromUtf8("colourLabel"))
        self.gridLayout.addWidget(self.colourLabel, 3, 0, 1, 1)
        self.colourCombobox = QtGui.QComboBox(vehicleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colourCombobox.sizePolicy().hasHeightForWidth())
        self.colourCombobox.setSizePolicy(sizePolicy)
        self.colourCombobox.setMinimumSize(QtCore.QSize(121, 25))
        self.colourCombobox.setMaximumSize(QtCore.QSize(121, 25))
        self.colourCombobox.setObjectName(_fromUtf8("colourCombobox"))
        self.colourCombobox.addItem(_fromUtf8(""))
        self.colourCombobox.addItem(_fromUtf8(""))
        self.colourCombobox.addItem(_fromUtf8(""))
        self.colourCombobox.addItem(_fromUtf8(""))
        self.colourCombobox.addItem(_fromUtf8(""))
        self.colourCombobox.addItem(_fromUtf8(""))
        self.colourCombobox.addItem(_fromUtf8(""))
        self.colourCombobox.addItem(_fromUtf8(""))
        self.colourCombobox.addItem(_fromUtf8(""))
        self.colourCombobox.addItem(_fromUtf8(""))
        self.colourCombobox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.colourCombobox, 3, 1, 1, 3)
        self.vehicleRegistrationLabel = QtGui.QLabel(vehicleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vehicleRegistrationLabel.sizePolicy().hasHeightForWidth())
        self.vehicleRegistrationLabel.setSizePolicy(sizePolicy)
        self.vehicleRegistrationLabel.setMinimumSize(QtCore.QSize(71, 16))
        self.vehicleRegistrationLabel.setMaximumSize(QtCore.QSize(71, 16))
        self.vehicleRegistrationLabel.setObjectName(_fromUtf8("vehicleRegistrationLabel"))
        self.gridLayout.addWidget(self.vehicleRegistrationLabel, 4, 0, 1, 2)
        self.vehicleRegistrationLineEdit = ValidatingLineEdit(vehicleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vehicleRegistrationLineEdit.sizePolicy().hasHeightForWidth())
        self.vehicleRegistrationLineEdit.setSizePolicy(sizePolicy)
        self.vehicleRegistrationLineEdit.setMinimumSize(QtCore.QSize(91, 25))
        self.vehicleRegistrationLineEdit.setMaximumSize(QtCore.QSize(91, 25))
        self.vehicleRegistrationLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.vehicleRegistrationLineEdit.setObjectName(_fromUtf8("vehicleRegistrationLineEdit"))
        self.gridLayout.addWidget(self.vehicleRegistrationLineEdit, 4, 2, 1, 2)
        self.vinLabel = QtGui.QLabel(vehicleDialog)
        self.vinLabel.setMaximumSize(QtCore.QSize(21, 16))
        self.vinLabel.setObjectName(_fromUtf8("vinLabel"))
        self.gridLayout.addWidget(self.vinLabel, 5, 0, 1, 1)
        self.vinLineEdit = ValidatingLineEdit(vehicleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vinLineEdit.sizePolicy().hasHeightForWidth())
        self.vinLineEdit.setSizePolicy(sizePolicy)
        self.vinLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.vinLineEdit.setMaximumSize(QtCore.QSize(183, 25))
        self.vinLineEdit.setObjectName(_fromUtf8("vinLineEdit"))
        self.gridLayout.addWidget(self.vinLineEdit, 5, 1, 1, 3)
        self.catalyticCheckbox = QtGui.QCheckBox(vehicleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catalyticCheckbox.sizePolicy().hasHeightForWidth())
        self.catalyticCheckbox.setSizePolicy(sizePolicy)
        self.catalyticCheckbox.setMinimumSize(QtCore.QSize(141, 17))
        self.catalyticCheckbox.setMaximumSize(QtCore.QSize(141, 17))
        self.catalyticCheckbox.setObjectName(_fromUtf8("catalyticCheckbox"))
        self.gridLayout.addWidget(self.catalyticCheckbox, 6, 0, 1, 3)
        self.catalyticLineEdit = ValidatingLineEdit(vehicleDialog)
        self.catalyticLineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catalyticLineEdit.sizePolicy().hasHeightForWidth())
        self.catalyticLineEdit.setSizePolicy(sizePolicy)
        self.catalyticLineEdit.setMinimumSize(QtCore.QSize(81, 25))
        self.catalyticLineEdit.setMaximumSize(QtCore.QSize(81, 25))
        self.catalyticLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.catalyticLineEdit.setObjectName(_fromUtf8("catalyticLineEdit"))
        self.gridLayout.addWidget(self.catalyticLineEdit, 6, 3, 1, 1)
        self.idLabel = QtGui.QLabel(vehicleDialog)
        self.idLabel.setMinimumSize(QtCore.QSize(16, 16))
        self.idLabel.setMaximumSize(QtCore.QSize(16, 16))
        self.idLabel.setObjectName(_fromUtf8("idLabel"))
        self.gridLayout.addWidget(self.idLabel, 7, 0, 1, 1)
        self.idCombobox = QtGui.QComboBox(vehicleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idCombobox.sizePolicy().hasHeightForWidth())
        self.idCombobox.setSizePolicy(sizePolicy)
        self.idCombobox.setMinimumSize(QtCore.QSize(121, 25))
        self.idCombobox.setMaximumSize(QtCore.QSize(121, 25))
        self.idCombobox.setObjectName(_fromUtf8("idCombobox"))
        self.idCombobox.addItem(_fromUtf8(""))
        self.idCombobox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.idCombobox, 7, 1, 1, 3)
        self.rejectButton = QtGui.QPushButton(vehicleDialog)
        self.rejectButton.setMinimumSize(QtCore.QSize(80, 26))
        self.rejectButton.setMaximumSize(QtCore.QSize(80, 26))
        self.rejectButton.setObjectName(_fromUtf8("rejectButton"))
        self.gridLayout.addWidget(self.rejectButton, 8, 0, 1, 2)
        self.acceptButton = QtGui.QPushButton(vehicleDialog)
        self.acceptButton.setEnabled(False)
        self.acceptButton.setMinimumSize(QtCore.QSize(80, 26))
        self.acceptButton.setMaximumSize(QtCore.QSize(80, 26))
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.gridLayout.addWidget(self.acceptButton, 8, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vehicleDialog)
        QtCore.QObject.connect(self.catalyticCheckbox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.catalyticLineEdit.setEnabled)
        QtCore.QObject.connect(self.makeLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.makeLineEdit.onTextEdited)
        QtCore.QObject.connect(self.makeLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.makeLineEdit.onValid)
        QtCore.QObject.connect(self.makeLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.makeLineEdit.onInvalid)
        QtCore.QObject.connect(self.vehicleRegistrationLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.vehicleRegistrationLineEdit.onTextEdited)
        QtCore.QObject.connect(self.vehicleRegistrationLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.vehicleRegistrationLineEdit.onValid)
        QtCore.QObject.connect(self.vehicleRegistrationLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.vehicleRegistrationLineEdit.onInvalid)
        QtCore.QObject.connect(self.modelLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.modelLineEdit.onTextEdited)
        QtCore.QObject.connect(self.modelLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.modelLineEdit.onValid)
        QtCore.QObject.connect(self.modelLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.modelLineEdit.onInvalid)
        QtCore.QObject.connect(self.vinLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.vinLineEdit.onTextEdited)
        QtCore.QObject.connect(self.vinLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.vinLineEdit.onValid)
        QtCore.QObject.connect(self.vinLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.vinLineEdit.onInvalid)
        QtCore.QObject.connect(self.catalyticLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.catalyticLineEdit.onTextEdited)
        QtCore.QObject.connect(self.catalyticLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.catalyticLineEdit.onValid)
        QtCore.QObject.connect(self.catalyticLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.catalyticLineEdit.onInvalid)
        QtCore.QObject.connect(self.rejectButton, QtCore.SIGNAL(_fromUtf8("clicked()")), vehicleDialog.reject)
        QtCore.QObject.connect(self.acceptButton, QtCore.SIGNAL(_fromUtf8("clicked()")), vehicleDialog.accept)
        QtCore.QObject.connect(self.makeLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), vehicleDialog.update)
        QtCore.QObject.connect(self.modelLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), vehicleDialog.update)
        QtCore.QObject.connect(self.vehicleRegistrationLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), vehicleDialog.update)
        QtCore.QObject.connect(self.vinLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), vehicleDialog.update)
        QtCore.QObject.connect(self.catalyticLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), vehicleDialog.update)
        QtCore.QObject.connect(self.catalyticCheckbox, QtCore.SIGNAL(_fromUtf8("clicked()")), vehicleDialog.update)
        QtCore.QMetaObject.connectSlotsByName(vehicleDialog)

    def retranslateUi(self, vehicleDialog):
        vehicleDialog.setWindowTitle(QtGui.QApplication.translate("vehicleDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.typeLabel.setText(QtGui.QApplication.translate("vehicleDialog", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.makeLabel.setText(QtGui.QApplication.translate("vehicleDialog", "Make", None, QtGui.QApplication.UnicodeUTF8))
        self.makeLineEdit.setToolTip(QtGui.QApplication.translate("vehicleDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.makeLineEdit.setWhatsThis(QtGui.QApplication.translate("vehicleDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.makeLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("vehicleDialog", "Street", None, QtGui.QApplication.UnicodeUTF8))
        self.modelLabel.setText(QtGui.QApplication.translate("vehicleDialog", "Model", None, QtGui.QApplication.UnicodeUTF8))
        self.modelLineEdit.setToolTip(QtGui.QApplication.translate("vehicleDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.modelLineEdit.setWhatsThis(QtGui.QApplication.translate("vehicleDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.modelLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("vehicleDialog", "Model", None, QtGui.QApplication.UnicodeUTF8))
        self.colourLabel.setText(QtGui.QApplication.translate("vehicleDialog", "Colour", None, QtGui.QApplication.UnicodeUTF8))
        self.colourCombobox.setItemText(0, QtGui.QApplication.translate("vehicleDialog", "Black", None, QtGui.QApplication.UnicodeUTF8))
        self.colourCombobox.setItemText(1, QtGui.QApplication.translate("vehicleDialog", "Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.colourCombobox.setItemText(2, QtGui.QApplication.translate("vehicleDialog", "Brown", None, QtGui.QApplication.UnicodeUTF8))
        self.colourCombobox.setItemText(3, QtGui.QApplication.translate("vehicleDialog", "Green", None, QtGui.QApplication.UnicodeUTF8))
        self.colourCombobox.setItemText(4, QtGui.QApplication.translate("vehicleDialog", "Grey", None, QtGui.QApplication.UnicodeUTF8))
        self.colourCombobox.setItemText(5, QtGui.QApplication.translate("vehicleDialog", "Orange", None, QtGui.QApplication.UnicodeUTF8))
        self.colourCombobox.setItemText(6, QtGui.QApplication.translate("vehicleDialog", "Pink", None, QtGui.QApplication.UnicodeUTF8))
        self.colourCombobox.setItemText(7, QtGui.QApplication.translate("vehicleDialog", "Purple", None, QtGui.QApplication.UnicodeUTF8))
        self.colourCombobox.setItemText(8, QtGui.QApplication.translate("vehicleDialog", "Red", None, QtGui.QApplication.UnicodeUTF8))
        self.colourCombobox.setItemText(9, QtGui.QApplication.translate("vehicleDialog", "White", None, QtGui.QApplication.UnicodeUTF8))
        self.colourCombobox.setItemText(10, QtGui.QApplication.translate("vehicleDialog", "Yellow", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLabel.setText(QtGui.QApplication.translate("vehicleDialog", "Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLineEdit.setToolTip(QtGui.QApplication.translate("vehicleDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLineEdit.setWhatsThis(QtGui.QApplication.translate("vehicleDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("vehicleDialog", "VehicleRegistration", None, QtGui.QApplication.UnicodeUTF8))
        self.vinLabel.setText(QtGui.QApplication.translate("vehicleDialog", "VIN", None, QtGui.QApplication.UnicodeUTF8))
        self.vinLineEdit.setToolTip(QtGui.QApplication.translate("vehicleDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.vinLineEdit.setWhatsThis(QtGui.QApplication.translate("vehicleDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.vinLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("vehicleDialog", "Vin", None, QtGui.QApplication.UnicodeUTF8))
        self.catalyticCheckbox.setText(QtGui.QApplication.translate("vehicleDialog", "Catalytic Converter", None, QtGui.QApplication.UnicodeUTF8))
        self.catalyticLineEdit.setToolTip(QtGui.QApplication.translate("vehicleDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.catalyticLineEdit.setWhatsThis(QtGui.QApplication.translate("vehicleDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.catalyticLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("vehicleDialog", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.idLabel.setText(QtGui.QApplication.translate("vehicleDialog", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.idCombobox.setItemText(0, QtGui.QApplication.translate("vehicleDialog", "Checked", None, QtGui.QApplication.UnicodeUTF8))
        self.idCombobox.setItemText(1, QtGui.QApplication.translate("vehicleDialog", "Known", None, QtGui.QApplication.UnicodeUTF8))
        self.rejectButton.setText(QtGui.QApplication.translate("vehicleDialog", "Reject", None, QtGui.QApplication.UnicodeUTF8))
        self.acceptButton.setText(QtGui.QApplication.translate("vehicleDialog", "Accept", None, QtGui.QApplication.UnicodeUTF8))

from custom_widgets.validatingLineEdit import ValidatingLineEdit
