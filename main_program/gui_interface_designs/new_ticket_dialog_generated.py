# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_ticket_dialog_design.ui'
#
# Created: Sun Jul 24 20:56:12 2011
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
        newTicketDialog.resize(442, 574)
        newTicketDialog.setMinimumSize(QtCore.QSize(442, 574))
        newTicketDialog.setMaximumSize(QtCore.QSize(878754, 574))
        self.newTicketTabWidget = QtGui.QTabWidget(newTicketDialog)
        self.newTicketTabWidget.setGeometry(QtCore.QRect(9, 9, 435, 561))
        self.newTicketTabWidget.setMinimumSize(QtCore.QSize(431, 561))
        self.newTicketTabWidget.setMaximumSize(QtCore.QSize(4643, 561))
        self.newTicketTabWidget.setStyleSheet(_fromUtf8(""))
        self.newTicketTabWidget.setObjectName(_fromUtf8("newTicketTabWidget"))
        self.customerTab = QtGui.QWidget()
        self.customerTab.setObjectName(_fromUtf8("customerTab"))
        self.layoutWidget = QtGui.QWidget(self.customerTab)
        self.layoutWidget.setGeometry(QtCore.QRect(42, 13, 258, 178))
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
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 419, 112))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tareWeightLineEdit = TareWeightLineEdit(self.layoutWidget1)
        self.tareWeightLineEdit.setEnabled(False)
        self.tareWeightLineEdit.setMinimumSize(QtCore.QSize(71, 20))
        self.tareWeightLineEdit.setMaximumSize(QtCore.QSize(71, 20))
        self.tareWeightLineEdit.setStyleSheet(_fromUtf8(""))
        self.tareWeightLineEdit.setObjectName(_fromUtf8("tareWeightLineEdit"))
        self.gridLayout_2.addWidget(self.tareWeightLineEdit, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.grossWeightLineEdit = GrossWeightLineEdit(self.layoutWidget1)
        self.grossWeightLineEdit.setMinimumSize(QtCore.QSize(71, 20))
        self.grossWeightLineEdit.setMaximumSize(QtCore.QSize(71, 20))
        self.grossWeightLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.grossWeightLineEdit.setObjectName(_fromUtf8("grossWeightLineEdit"))
        self.gridLayout_2.addWidget(self.grossWeightLineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.netWeightLineEdit = NetWeightLineEdit(self.layoutWidget1)
        self.netWeightLineEdit.setMinimumSize(QtCore.QSize(71, 20))
        self.netWeightLineEdit.setMaximumSize(QtCore.QSize(71, 20))
        self.netWeightLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.netWeightLineEdit.setObjectName(_fromUtf8("netWeightLineEdit"))
        self.gridLayout_2.addWidget(self.netWeightLineEdit, 2, 1, 1, 1)
        self.materialCombobox = MaterialCombobox(self.layoutWidget1)
        self.materialCombobox.setObjectName(_fromUtf8("materialCombobox"))
        self.gridLayout_2.addWidget(self.materialCombobox, 2, 2, 1, 1)
        self.payloadValueLineEdit = PayloadValueLineEdit(self.layoutWidget1)
        self.payloadValueLineEdit.setMinimumSize(QtCore.QSize(81, 25))
        self.payloadValueLineEdit.setMaximumSize(QtCore.QSize(81, 25))
        self.payloadValueLineEdit.setReadOnly(True)
        self.payloadValueLineEdit.setObjectName(_fromUtf8("payloadValueLineEdit"))
        self.gridLayout_2.addWidget(self.payloadValueLineEdit, 2, 3, 1, 2)
        self.manualPriceCheckbox = QtGui.QCheckBox(self.layoutWidget1)
        self.manualPriceCheckbox.setMinimumSize(QtCore.QSize(91, 0))
        self.manualPriceCheckbox.setObjectName(_fromUtf8("manualPriceCheckbox"))
        self.gridLayout_2.addWidget(self.manualPriceCheckbox, 2, 5, 1, 1)
        self.deletePayloadButton = QtGui.QPushButton(self.layoutWidget1)
        self.deletePayloadButton.setObjectName(_fromUtf8("deletePayloadButton"))
        self.gridLayout_2.addWidget(self.deletePayloadButton, 3, 2, 1, 1)
        self.addPayloadButton = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addPayloadButton.sizePolicy().hasHeightForWidth())
        self.addPayloadButton.setSizePolicy(sizePolicy)
        self.addPayloadButton.setMinimumSize(QtCore.QSize(81, 0))
        self.addPayloadButton.setObjectName(_fromUtf8("addPayloadButton"))
        self.gridLayout_2.addWidget(self.addPayloadButton, 3, 5, 1, 1)
        self.layoutWidget2 = QtGui.QWidget(self.payloadTab)
        self.layoutWidget2.setGeometry(QtCore.QRect(53, 143, 343, 357))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.payloadTableWidget = PayloadTableWidget(self.layoutWidget2)
        self.payloadTableWidget.setMinimumSize(QtCore.QSize(341, 311))
        self.payloadTableWidget.setMaximumSize(QtCore.QSize(341, 311))
        self.payloadTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.payloadTableWidget.setTabKeyNavigation(True)
        self.payloadTableWidget.setProperty(_fromUtf8("showDropIndicator"), False)
        self.payloadTableWidget.setDragDropOverwriteMode(False)
        self.payloadTableWidget.setRowCount(0)
        self.payloadTableWidget.setColumnCount(3)
        self.payloadTableWidget.setObjectName(_fromUtf8("payloadTableWidget"))
        self.payloadTableWidget.setColumnCount(3)
        self.payloadTableWidget.setRowCount(0)
        self.payloadTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.payloadTableWidget, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.reviewTicketButton = QtGui.QCommandLinkButton(self.layoutWidget2)
        self.reviewTicketButton.setEnabled(False)
        self.reviewTicketButton.setMinimumSize(QtCore.QSize(131, 0))
        self.reviewTicketButton.setMaximumSize(QtCore.QSize(131, 16777215))
        self.reviewTicketButton.setObjectName(_fromUtf8("reviewTicketButton"))
        self.gridLayout_3.addWidget(self.reviewTicketButton, 0, 0, 1, 1)
        self.totalValueLabel = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.totalValueLabel.setFont(font)
        self.totalValueLabel.setObjectName(_fromUtf8("totalValueLabel"))
        self.gridLayout_3.addWidget(self.totalValueLabel, 0, 1, 1, 1)
        self.totalValueLineEdit = TotalValueLineEdit(self.layoutWidget2)
        self.totalValueLineEdit.setMinimumSize(QtCore.QSize(101, 25))
        self.totalValueLineEdit.setMaximumSize(QtCore.QSize(101, 25))
        self.totalValueLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.totalValueLineEdit.setReadOnly(True)
        self.totalValueLineEdit.setObjectName(_fromUtf8("totalValueLineEdit"))
        self.gridLayout_3.addWidget(self.totalValueLineEdit, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.newTicketTabWidget.addTab(self.payloadTab, _fromUtf8(""))

        self.retranslateUi(newTicketDialog)
        self.newTicketTabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.grossWeightLineEdit.onTextEdited)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.netWeightLineEdit.onTextEdited)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.netWeightLineEdit.onValid)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.netWeightLineEdit.onInvalid)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("enableNetWeight()")), self.netWeightLineEdit.onEnableNetWeight)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("disableNetWeight()")), self.netWeightLineEdit.onDisableNetWeight)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("enableGrossWeight()")), self.grossWeightLineEdit.onEnableGrossWeight)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("disableGrossWeight()")), self.grossWeightLineEdit.onDisableGrossWeight)
        QtCore.QObject.connect(self.firstNameLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.firstNameLineEdit.onTextEdited)
        QtCore.QObject.connect(self.firstNameLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.firstNameLineEdit.onValid)
        QtCore.QObject.connect(self.firstNameLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.firstNameLineEdit.onInvalid)
        QtCore.QObject.connect(self.lastNameLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.lastNameLineEdit.onTextEdited)
        QtCore.QObject.connect(self.lastNameLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.lastNameLineEdit.onValid)
        QtCore.QObject.connect(self.lastNameLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.lastNameLineEdit.onInvalid)
        QtCore.QObject.connect(self.houseNumberLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.houseNumberLineEdit.onTextEdited)
        QtCore.QObject.connect(self.houseNumberLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.houseNumberLineEdit.onValid)
        QtCore.QObject.connect(self.houseNumberLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.houseNumberLineEdit.onInvalid)
        QtCore.QObject.connect(self.streetLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.streetLineEdit.onTextEdited)
        QtCore.QObject.connect(self.streetLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.streetLineEdit.onValid)
        QtCore.QObject.connect(self.streetLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.streetLineEdit.onInvalid)
        QtCore.QObject.connect(self.townLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.townLineEdit.onTextEdited)
        QtCore.QObject.connect(self.townLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.townLineEdit.onValid)
        QtCore.QObject.connect(self.townLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.townLineEdit.onInvalid)
        QtCore.QObject.connect(self.postcodeLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.postcodeLineEdit.onTextEdited)
        QtCore.QObject.connect(self.postcodeLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.postcodeLineEdit.onValid)
        QtCore.QObject.connect(self.postcodeLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.postcodeLineEdit.onInvalid)
        QtCore.QObject.connect(self.vehicleRegistrationLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.vehicleRegistrationLineEdit.onTextEdited)
        QtCore.QObject.connect(self.vehicleRegistrationLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.vehicleRegistrationLineEdit.onValid)
        QtCore.QObject.connect(self.vehicleRegistrationLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.vehicleRegistrationLineEdit.onInvalid)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("enableTareWeight()")), self.tareWeightLineEdit.onEnableTareWeight)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("disableTareWeight()")), self.tareWeightLineEdit.onDisableTareWeight)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.grossWeightLineEdit.onValid)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.grossWeightLineEdit.onInvalid)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.tareWeightLineEdit.onTextEdited)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.tareWeightLineEdit.onValid)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("sendGrossWeightValue()")), self.grossWeightLineEdit.onSendGrossWeightValue)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("grossWeightValue(QString)")), self.tareWeightLineEdit.onGrossWeightValue)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("calculateNetWeight(QString,QString)")), self.netWeightLineEdit.onCalculateNetWeight)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.tareWeightLineEdit.onInvalid)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("clearNetWeight()")), self.netWeightLineEdit.onClearNetWeight)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("clearNetWeight()")), self.netWeightLineEdit.onClearNetWeight)
        QtCore.QObject.connect(self.firstNameLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), newTicketDialog.update)
        QtCore.QObject.connect(self.lastNameLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), newTicketDialog.update)
        QtCore.QObject.connect(self.houseNumberLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), newTicketDialog.update)
        QtCore.QObject.connect(self.streetLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), newTicketDialog.update)
        QtCore.QObject.connect(self.townLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), newTicketDialog.update)
        QtCore.QObject.connect(self.vehicleRegistrationLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), newTicketDialog.update)
        QtCore.QObject.connect(self.postcodeLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), newTicketDialog.update)
        QtCore.QObject.connect(self.grossWeightLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), newTicketDialog.update)
        QtCore.QObject.connect(self.tareWeightLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), newTicketDialog.update)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), newTicketDialog.update)
        QtCore.QObject.connect(self.payloadValueLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), newTicketDialog.update)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("calculatePayloadValue(QString,QString)")), self.payloadValueLineEdit.onCalculatePayloadValue)
        QtCore.QObject.connect(self.netWeightLineEdit, QtCore.SIGNAL(_fromUtf8("clearPayloadValue()")), self.payloadValueLineEdit.onClearPayloadValue)
        QtCore.QObject.connect(self.manualPriceCheckbox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.payloadValueLineEdit.setReadOnlyInverted)
        QtCore.QObject.connect(self.payloadValueLineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.payloadValueLineEdit.onTextEdited)
        QtCore.QObject.connect(self.payloadValueLineEdit, QtCore.SIGNAL(_fromUtf8("valid()")), self.payloadValueLineEdit.onValid)
        QtCore.QObject.connect(self.payloadValueLineEdit, QtCore.SIGNAL(_fromUtf8("invalid()")), self.payloadValueLineEdit.onInvalid)
        QtCore.QObject.connect(self.payloadTableWidget, QtCore.SIGNAL(_fromUtf8("cellChanged(int,int)")), self.payloadTableWidget.onChange)
        QtCore.QObject.connect(self.payloadTableWidget, QtCore.SIGNAL(_fromUtf8("calculateTotalValue(PyQt_PyObject)")), self.totalValueLineEdit.onCalculateTotalValue)
        QtCore.QObject.connect(self.payloadTableWidget, QtCore.SIGNAL(_fromUtf8("cellChanged(int,int)")), newTicketDialog.update)
        QtCore.QObject.connect(self.materialCombobox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), newTicketDialog.update)
        QtCore.QObject.connect(self.materialCombobox, QtCore.SIGNAL(_fromUtf8("materialChanged(QString)")), self.netWeightLineEdit.onMaterialChanged)
        QtCore.QObject.connect(self.materialCombobox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.materialCombobox.onIndexChange)
        QtCore.QMetaObject.connectSlotsByName(newTicketDialog)

    def retranslateUi(self, newTicketDialog):
        newTicketDialog.setWindowTitle(QtGui.QApplication.translate("newTicketDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLabel.setText(QtGui.QApplication.translate("newTicketDialog", "First name", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Customer first name.", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLineEdit.setStatusTip(QtGui.QApplication.translate("newTicketDialog", "Status test", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLabel.setText(QtGui.QApplication.translate("newTicketDialog", "Last name", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Customer last name.", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.houseNumberLabel.setText(QtGui.QApplication.translate("newTicketDialog", "House number", None, QtGui.QApplication.UnicodeUTF8))
        self.houseNumberLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Customer house number.", None, QtGui.QApplication.UnicodeUTF8))
        self.houseNumberLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.houseNumberLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "HouseNumber", None, QtGui.QApplication.UnicodeUTF8))
        self.streetLabel.setText(QtGui.QApplication.translate("newTicketDialog", "Street", None, QtGui.QApplication.UnicodeUTF8))
        self.streetLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Customer address street.", None, QtGui.QApplication.UnicodeUTF8))
        self.streetLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.streetLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Street", None, QtGui.QApplication.UnicodeUTF8))
        self.townLabel.setText(QtGui.QApplication.translate("newTicketDialog", "Town", None, QtGui.QApplication.UnicodeUTF8))
        self.townLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Customer address town.", None, QtGui.QApplication.UnicodeUTF8))
        self.townLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.townLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Town", None, QtGui.QApplication.UnicodeUTF8))
        self.postcodeLabel.setText(QtGui.QApplication.translate("newTicketDialog", "Postcode", None, QtGui.QApplication.UnicodeUTF8))
        self.postcodeLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Customer address postcode.", None, QtGui.QApplication.UnicodeUTF8))
        self.postcodeLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.postcodeLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Postcode", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLabel.setText(QtGui.QApplication.translate("newTicketDialog", "Vehicle Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Customer\'s vehicle registration number.", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.vehicleRegistrationLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "VehicleRegistration", None, QtGui.QApplication.UnicodeUTF8))
        self.newTicketTabWidget.setTabText(self.newTicketTabWidget.indexOf(self.customerTab), QtGui.QApplication.translate("newTicketDialog", "Customer", None, QtGui.QApplication.UnicodeUTF8))
        self.tareWeightLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Enter tare weight here. Fraction must be .5 or .0.", None, QtGui.QApplication.UnicodeUTF8))
        self.tareWeightLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.tareWeightLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("newTicketDialog", "Gross", None, QtGui.QApplication.UnicodeUTF8))
        self.grossWeightLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Enter gross weight. Fraction must be .5 or .0.", None, QtGui.QApplication.UnicodeUTF8))
        self.grossWeightLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.grossWeightLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("newTicketDialog", "Tare", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("newTicketDialog", "Net", None, QtGui.QApplication.UnicodeUTF8))
        self.netWeightLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Enter net weight here. Fraction must be .5 or .0.", None, QtGui.QApplication.UnicodeUTF8))
        self.netWeightLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.netWeightLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.materialCombobox.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Select material type. Vehicle entry opens new dialog.", None, QtGui.QApplication.UnicodeUTF8))
        self.materialCombobox.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadValueLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Total value for this payload in GBP.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadValueLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadValueLineEdit.setProperty(_fromUtf8("regexString"), QtGui.QApplication.translate("newTicketDialog", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.manualPriceCheckbox.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Check to allow manual entry of price.", None, QtGui.QApplication.UnicodeUTF8))
        self.manualPriceCheckbox.setText(QtGui.QApplication.translate("newTicketDialog", "Manual price", None, QtGui.QApplication.UnicodeUTF8))
        self.deletePayloadButton.setText(QtGui.QApplication.translate("newTicketDialog", "Delete payload", None, QtGui.QApplication.UnicodeUTF8))
        self.addPayloadButton.setText(QtGui.QApplication.translate("newTicketDialog", "Add payload", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTableWidget.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Double-click blue vehicle text to view/edit vehicle details.\n"
"Select any row with left-click and click \'Delete payload\' to remove.", None, QtGui.QApplication.UnicodeUTF8))
        self.payloadTableWidget.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "Extra functions for paylod widget.", None, QtGui.QApplication.UnicodeUTF8))
        self.reviewTicketButton.setText(QtGui.QApplication.translate("newTicketDialog", "Review ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.totalValueLabel.setText(QtGui.QApplication.translate("newTicketDialog", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.totalValueLineEdit.setToolTip(QtGui.QApplication.translate("newTicketDialog", "Total to pay customer in GBP.", None, QtGui.QApplication.UnicodeUTF8))
        self.totalValueLineEdit.setWhatsThis(QtGui.QApplication.translate("newTicketDialog", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.newTicketTabWidget.setTabText(self.newTicketTabWidget.indexOf(self.payloadTab), QtGui.QApplication.translate("newTicketDialog", "Payload", None, QtGui.QApplication.UnicodeUTF8))

from custom_widgets.validatingLineEdit import ValidatingLineEdit
from custom_widgets.tareWeightLineEdit import TareWeightLineEdit
from custom_widgets.grossWeightLineEdit import GrossWeightLineEdit
from custom_widgets.payloadValueLineEdit import PayloadValueLineEdit
from custom_widgets.netWeightLineEdit import NetWeightLineEdit
from custom_widgets.payloadTableWidget import PayloadTableWidget
from custom_widgets.totalValueLineEdit import TotalValueLineEdit
from custom_widgets.materialCombobox import MaterialCombobox
