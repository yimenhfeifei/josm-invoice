# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_ticket_dialog_design.ui'
#
# Created: Tue Jun 14 12:12:00 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_newTicketDialog(object):
    def setupUi(self, newTicketDialog):
        newTicketDialog.setObjectName(_fromUtf8("newTicketDialog"))
        newTicketDialog.resize(386, 574)
        self.verticalLayout = QtGui.QVBoxLayout(newTicketDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.newTicketTabWidget = QtGui.QTabWidget(newTicketDialog)
        self.newTicketTabWidget.setMinimumSize(QtCore.QSize(0, 431))
        self.newTicketTabWidget.setObjectName(_fromUtf8("newTicketTabWidget"))
        self.customerTab = QtGui.QWidget()
        self.customerTab.setObjectName(_fromUtf8("customerTab"))
        self.layoutWidget = QtGui.QWidget(self.customerTab)
        self.layoutWidget.setGeometry(QtCore.QRect(42, 13, 234, 178))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.firstNameLabel = QtGui.QLabel(self.layoutWidget)
        self.firstNameLabel.setObjectName(_fromUtf8("firstNameLabel"))
        self.gridLayout.addWidget(self.firstNameLabel, 0, 0, 1, 1)
        self.firstNameLineEdit = ValidatingLineEdit(self.layoutWidget)
        self.firstNameLineEdit.setMinimumSize(QtCore.QSize(133, 20))
        self.firstNameLineEdit.setMaximumSize(QtCore.QSize(133, 20))
        self.firstNameLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.firstNameLineEdit.setObjectName(_fromUtf8("firstNameLineEdit"))
        self.gridLayout.addWidget(self.firstNameLineEdit, 0, 1, 1, 1)
        self.lastNameLabel = QtGui.QLabel(self.layoutWidget)
        self.lastNameLabel.setObjectName(_fromUtf8("lastNameLabel"))
        self.gridLayout.addWidget(self.lastNameLabel, 1, 0, 1, 1)
        self.lastNameLineEdit = ValidatingLineEdit(self.layoutWidget)
        self.lastNameLineEdit.setMinimumSize(QtCore.QSize(133, 20))
        self.lastNameLineEdit.setMaximumSize(QtCore.QSize(133, 20))
        self.lastNameLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.lastNameLineEdit.setObjectName(_fromUtf8("lastNameLineEdit"))
        self.gridLayout.addWidget(self.lastNameLineEdit, 1, 1, 1, 1)
        self.houseNumberLabel = QtGui.QLabel(self.layoutWidget)
        self.houseNumberLabel.setObjectName(_fromUtf8("houseNumberLabel"))
        self.gridLayout.addWidget(self.houseNumberLabel, 2, 0, 1, 1)
        self.houseNumberLineEdit = ValidatingLineEdit(self.layoutWidget)
        self.houseNumberLineEdit.setMinimumSize(QtCore.QSize(51, 20))
        self.houseNumberLineEdit.setMaximumSize(QtCore.QSize(51, 20))
        self.houseNumberLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.houseNumberLineEdit.setObjectName(_fromUtf8("houseNumberLineEdit"))
        self.gridLayout.addWidget(self.houseNumberLineEdit, 2, 1, 1, 1)
        self.streetLabel = QtGui.QLabel(self.layoutWidget)
        self.streetLabel.setObjectName(_fromUtf8("streetLabel"))
        self.gridLayout.addWidget(self.streetLabel, 3, 0, 1, 1)
        self.streetLineEdit = ValidatingLineEdit(self.layoutWidget)
        self.streetLineEdit.setMinimumSize(QtCore.QSize(133, 20))
        self.streetLineEdit.setMaximumSize(QtCore.QSize(133, 20))
        self.streetLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.streetLineEdit.setObjectName(_fromUtf8("streetLineEdit"))
        self.gridLayout.addWidget(self.streetLineEdit, 3, 1, 1, 1)
        self.townLabel = QtGui.QLabel(self.layoutWidget)
        self.townLabel.setObjectName(_fromUtf8("townLabel"))
        self.gridLayout.addWidget(self.townLabel, 4, 0, 1, 1)
        self.townLineEdit = ValidatingLineEdit(self.layoutWidget)
        self.townLineEdit.setMinimumSize(QtCore.QSize(101, 20))
        self.townLineEdit.setMaximumSize(QtCore.QSize(101, 20))
        self.townLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.townLineEdit.setObjectName(_fromUtf8("townLineEdit"))
        self.gridLayout.addWidget(self.townLineEdit, 4, 1, 1, 1)
        self.postcodeLabel = QtGui.QLabel(self.layoutWidget)
        self.postcodeLabel.setObjectName(_fromUtf8("postcodeLabel"))
        self.gridLayout.addWidget(self.postcodeLabel, 5, 0, 1, 1)
        self.postcodeLineEdit = ValidatingLineEdit(self.layoutWidget)
        self.postcodeLineEdit.setMinimumSize(QtCore.QSize(51, 20))
        self.postcodeLineEdit.setMaximumSize(QtCore.QSize(71, 20))
        self.postcodeLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.postcodeLineEdit.setObjectName(_fromUtf8("postcodeLineEdit"))
        self.gridLayout.addWidget(self.postcodeLineEdit, 5, 1, 1, 1)
        self.vehicleRegistrationLabel = QtGui.QLabel(self.layoutWidget)
        self.vehicleRegistrationLabel.setObjectName(_fromUtf8("vehicleRegistrationLabel"))
        self.gridLayout.addWidget(self.vehicleRegistrationLabel, 6, 0, 1, 1)
        self.vehicleRegistrationLineEdit = ValidatingLineEdit(self.layoutWidget)
        self.vehicleRegistrationLineEdit.setMinimumSize(QtCore.QSize(71, 20))
        self.vehicleRegistrationLineEdit.setMaximumSize(QtCore.QSize(71, 20))
        self.vehicleRegistrationLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.vehicleRegistrationLineEdit.setObjectName(_fromUtf8("vehicleRegistrationLineEdit"))
        self.gridLayout.addWidget(self.vehicleRegistrationLineEdit, 6, 1, 1, 1)
        self.newTicketTabWidget.addTab(self.customerTab, _fromUtf8(""))
        self.payloadTab = QtGui.QWidget()
        self.payloadTab.setObjectName(_fromUtf8("payloadTab"))
        self.layoutWidget1 = QtGui.QWidget(self.payloadTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 11, 334, 374))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.grossWeightLineEdit = GrossWeightLineEdit(self.layoutWidget1)
        self.grossWeightLineEdit.setMinimumSize(QtCore.QSize(71, 20))
        self.grossWeightLineEdit.setMaximumSize(QtCore.QSize(71, 20))
        self.grossWeightLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.grossWeightLineEdit.setObjectName(_fromUtf8("grossWeightLineEdit"))
        self.gridLayout_2.addWidget(self.grossWeightLineEdit, 0, 0, 1, 1)
        self.tareWeightLineEdit = TareWeightLineEdit(self.layoutWidget1)
        self.tareWeightLineEdit.setEnabled(False)
        self.tareWeightLineEdit.setMinimumSize(QtCore.QSize(71, 20))
        self.tareWeightLineEdit.setMaximumSize(QtCore.QSize(71, 20))
        self.tareWeightLineEdit.setStyleSheet(_fromUtf8(""))
        self.tareWeightLineEdit.setObjectName(_fromUtf8("tareWeightLineEdit"))
        self.gridLayout_2.addWidget(self.tareWeightLineEdit, 1, 0, 1, 1)
        self.netWeightLineEdit = NetWeightLineEdit(self.layoutWidget1)
        self.netWeightLineEdit.setMinimumSize(QtCore.QSize(71, 20))
        self.netWeightLineEdit.setMaximumSize(QtCore.QSize(71, 20))
        self.netWeightLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.netWeightLineEdit.setObjectName(_fromUtf8("netWeightLineEdit"))
        self.gridLayout_2.addWidget(self.netWeightLineEdit, 2, 0, 1, 1)
        self.materialCombobox = QtGui.QComboBox(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.materialCombobox.sizePolicy().hasHeightForWidth())
        self.materialCombobox.setSizePolicy(sizePolicy)
        self.materialCombobox.setMinimumSize(QtCore.QSize(91, 0))
        self.materialCombobox.setMaximumSize(QtCore.QSize(91, 16777215))
        self.materialCombobox.setObjectName(_fromUtf8("materialCombobox"))
        self.materialCombobox.addItem(_fromUtf8(""))
        self.materialCombobox.addItem(_fromUtf8(""))
        self.materialCombobox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.materialCombobox, 2, 1, 1, 1)
        self.payloadValueLineEdit = ValidatingLineEdit(self.layoutWidget1)
        self.payloadValueLineEdit.setMinimumSize(QtCore.QSize(61, 20))
        self.payloadValueLineEdit.setMaximumSize(QtCore.QSize(61, 20))
        self.payloadValueLineEdit.setReadOnly(True)
        self.payloadValueLineEdit.setObjectName(_fromUtf8("payloadValueLineEdit"))
        self.gridLayout_2.addWidget(self.payloadValueLineEdit, 2, 2, 1, 2)
        self.manualPriceCheckbox = QtGui.QCheckBox(self.layoutWidget1)
        self.manualPriceCheckbox.setMinimumSize(QtCore.QSize(91, 0))
        self.manualPriceCheckbox.setObjectName(_fromUtf8("manualPriceCheckbox"))
        self.gridLayout_2.addWidget(self.manualPriceCheckbox, 2, 4, 1, 1)
        self.addPayloadButton = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addPayloadButton.sizePolicy().hasHeightForWidth())
        self.addPayloadButton.setSizePolicy(sizePolicy)
        self.addPayloadButton.setMinimumSize(QtCore.QSize(81, 0))
        self.addPayloadButton.setObjectName(_fromUtf8("addPayloadButton"))
        self.gridLayout_2.addWidget(self.addPayloadButton, 3, 4, 1, 1)
        self.payloadTableWidget = QtGui.QTableWidget(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.payloadTableWidget.sizePolicy().hasHeightForWidth())
        self.payloadTableWidget.setSizePolicy(sizePolicy)
        self.payloadTableWidget.setMinimumSize(QtCore.QSize(341, 0))
        self.payloadTableWidget.setMaximumSize(QtCore.QSize(341, 16777215))
        self.payloadTableWidget.setRowCount(12)
        self.payloadTableWidget.setColumnCount(3)
        self.payloadTableWidget.setObjectName(_fromUtf8("payloadTableWidget"))
        self.payloadTableWidget.setColumnCount(3)
        self.payloadTableWidget.setRowCount(12)
        self.payloadTableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.payloadTableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.gridLayout_2.addWidget(self.payloadTableWidget, 4, 0, 1, 5)
        self.totalValueLabel = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.totalValueLabel.setFont(font)
        self.totalValueLabel.setObjectName(_fromUtf8("totalValueLabel"))
        self.gridLayout_2.addWidget(self.totalValueLabel, 5, 2, 1, 1)
        self.totalValueLineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.totalValueLineEdit.setMinimumSize(QtCore.QSize(101, 0))
        self.totalValueLineEdit.setMaximumSize(QtCore.QSize(101, 16777215))
        self.totalValueLineEdit.setObjectName(_fromUtf8("totalValueLineEdit"))
        self.gridLayout_2.addWidget(self.totalValueLineEdit, 5, 3, 1, 2)
        self.reviewTicketButton = QtGui.QCommandLinkButton(self.layoutWidget1)
        self.reviewTicketButton.setEnabled(False)
        self.reviewTicketButton.setMinimumSize(QtCore.QSize(131, 0))
        self.reviewTicketButton.setMaximumSize(QtCore.QSize(131, 16777215))
        self.reviewTicketButton.setObjectName(_fromUtf8("reviewTicketButton"))
        self.gridLayout_2.addWidget(self.reviewTicketButton, 6, 2, 1, 3)
        self.newTicketTabWidget.addTab(self.payloadTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.newTicketTabWidget)
        self.totalValueLabel.setBuddy(self.totalValueLineEdit)

        self.retranslateUi(newTicketDialog)
        self.newTicketTabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.grossWeightLineEdit.onTextEdited)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.grossWeightLineEdit.setValidStyleSheet)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.grossWeightLineEdit.setInvalidStyleSheet)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.netWeightLineEdit.onTextEdited)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.netWeightLineEdit.setValidStyleSheet)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.netWeightLineEdit.setInvalidStyleSheet)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("enableNetWeight()")), self.netWeightLineEdit.enableNetWeight)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("disableNetWeight()")), self.netWeightLineEdit.disableNetWeight)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("enableGrossWeight()")), self.grossWeightLineEdit.enableGrossWeight)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("disableGrossWeight()")), self.grossWeightLineEdit.disableGrossWeight)
        QtCore.QObject.connect(self.firstNameLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.firstNameLineEdit.onTextEdited)
        QtCore.QObject.connect(self.firstNameLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.firstNameLineEdit.setValidStyleSheet)
        QtCore.QObject.connect(self.firstNameLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.firstNameLineEdit.setInvalidStyleSheet)
        QtCore.QObject.connect(self.lastNameLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.lastNameLineEdit.onTextEdited)
        QtCore.QObject.connect(self.lastNameLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.lastNameLineEdit.setValidStyleSheet)
        QtCore.QObject.connect(self.lastNameLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.lastNameLineEdit.setInvalidStyleSheet)
        QtCore.QObject.connect(self.houseNumberLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.houseNumberLineEdit.onTextEdited)
        QtCore.QObject.connect(self.houseNumberLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.houseNumberLineEdit.setValidStyleSheet)
        QtCore.QObject.connect(self.houseNumberLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.houseNumberLineEdit.setInvalidStyleSheet)
        QtCore.QObject.connect(self.streetLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.streetLineEdit.onTextEdited)
        QtCore.QObject.connect(self.streetLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.streetLineEdit.setValidStyleSheet)
        QtCore.QObject.connect(self.streetLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.streetLineEdit.setInvalidStyleSheet)
        QtCore.QObject.connect(self.townLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.townLineEdit.onTextEdited)
        QtCore.QObject.connect(self.townLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.townLineEdit.setValidStyleSheet)
        QtCore.QObject.connect(self.townLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.townLineEdit.setInvalidStyleSheet)
        QtCore.QObject.connect(self.postcodeLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.postcodeLineEdit.onTextEdited)
        QtCore.QObject.connect(self.postcodeLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.postcodeLineEdit.setValidStyleSheet)
        QtCore.QObject.connect(self.postcodeLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.postcodeLineEdit.setInvalidStyleSheet)
        QtCore.QObject.connect(self.vehicleRegistrationLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.vehicleRegistrationLineEdit.onTextEdited)
        QtCore.QObject.connect(self.vehicleRegistrationLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.vehicleRegistrationLineEdit.setValidStyleSheet)
        QtCore.QObject.connect(self.vehicleRegistrationLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.vehicleRegistrationLineEdit.setInvalidStyleSheet)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("enableTare()")), self.tareWeightLineEdit.enableTare)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("disableTare()")), self.tareWeightLineEdit.disableTare)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.grossWeightLineEdit.validReceived)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.grossWeightLineEdit.invalidReceived)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.tareWeightLineEdit.onTextEdited)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.tareWeightLineEdit.setValidStyleSheet)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.tareWeightLineEdit.setInvalidStyleSheet)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.tareWeightLineEdit.validReceieved)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("requestGrossValue()")), self.grossWeightLineEdit.requestGrossValueReceived)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("sendGrossValue(QString)")), self.tareWeightLineEdit.grossValueReceived)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("calculateNetWeight(QString,QString)")), self.netWeightLineEdit.calculateNetWeight)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.tareWeightLineEdit.invalidReceieved)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("clearNetWeight()")), self.netWeightLineEdit.clearNetWeight)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("clearNetWeight()")), self.netWeightLineEdit.clearNetWeight)
        QtCore.QObject.connect(self.manualPriceCheckbox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.payloadValueLineEdit.setReadOnlyInverted)
        QtCore.QMetaObject.connectSlotsByName(newTicketDialog)

    def retranslateUi(self, newTicketDialog):
        newTicketDialog.setWindowTitle(QtGui.QApplication.translate("newTicketDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLabel.setText(QtGui.QApplication.translate("newTicketDialog", "First name", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLabel.setText(QtGui.QApplication.translate("newTicketDialog", "Last name", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.houseNumberLabel.setText(QtGui.QApplication.translate("newTicketDialog", "House number", None, QtGui.QApplication.UnicodeUTF8))
        self.houseNumberLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.houseNumberLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.houseNumberLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "HouseNumber", None, QtGui.QApplication.UnicodeUTF8))
        self.streetLabel.setText(QtGui.QApplication.translate("newTicketDialog", "Street", None, QtGui.QApplication.UnicodeUTF8))
        self.streetLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.streetLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.streetLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Street", None, QtGui.QApplication.UnicodeUTF8))
        self.townLabel.setText(QtGui.QApplication.translate("newTicketDialog", "Town", None, QtGui.QApplication.UnicodeUTF8))
        self.townLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.townLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.townLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Town", None, QtGui.QApplication.UnicodeUTF8))
        self.postcodeLabel.setText(QtGui.QApplication.translate("newTicketDialog", "Postcode", None, QtGui.QApplication.UnicodeUTF8))
        self.postcodeLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.postcodeLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.postcodeLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Postcode", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLabel.setText(QtGui.QApplication.translate("newTicketDialog", "Vehicle Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "VehicleRegistration", None, QtGui.QApplication.UnicodeUTF8))
        self.newTicketTabWidget.setTabText(self.newTicketTabWidget.indexOf(self.customerTab), QtGui.QApplication.translate("newTicketDialog", "Customer", None, QtGui.QApplication.UnicodeUTF8))
        self.grossWeightLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.grossWeightLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.grossWeightLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.tareWeightLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.tareWeightLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.tareWeightLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.netWeightLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.netWeightLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.netWeightLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.materialCombobox.setItemText(0, QtGui.QApplication.translate("newTicketDialog", "Copper", None, QtGui.QApplication.UnicodeUTF8))
        self.materialCombobox.setItemText(1, QtGui.QApplication.translate("newTicketDialog", "Car", None, QtGui.QApplication.UnicodeUTF8))
        self.materialCombobox.setItemText(2, QtGui.QApplication.translate("newTicketDialog", "Heavy Iron", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadValueLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Custom Line Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadValueLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.manualPriceCheckbox.setText(QtGui.QApplication.translate("newTicketDialog", "Manual price", None, QtGui.QApplication.UnicodeUTF8))
        self.addPayloadButton.setText(QtGui.QApplication.translate("newTicketDialog", "Add payload", None, QtGui.QApplication.UnicodeUTF8))
        self.totalValueLabel.setText(QtGui.QApplication.translate("newTicketDialog", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.reviewTicketButton.setText(QtGui.QApplication.translate("newTicketDialog", "Review ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.newTicketTabWidget.setTabText(self.newTicketTabWidget.indexOf(self.payloadTab), QtGui.QApplication.translate("newTicketDialog", "Payload", None, QtGui.QApplication.UnicodeUTF8))

from shared_modules.tareWeightLineEdit import TareWeightLineEdit
from shared_modules.grossWeightLineEdit import GrossWeightLineEdit
from shared_modules.netWeightLineEdit import NetWeightLineEdit
from shared_modules.validatingLineEdit import ValidatingLineEdit
