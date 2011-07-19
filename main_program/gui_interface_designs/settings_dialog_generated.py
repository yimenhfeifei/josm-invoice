# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_dialog_design.ui'
#
# Created: Tue Jul 19 11:03:00 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName(_fromUtf8("settingsDialog"))
        settingsDialog.resize(400, 299)
        self.settingsTabWidget = QtGui.QTabWidget(settingsDialog)
        self.settingsTabWidget.setGeometry(QtCore.QRect(20, 10, 371, 271))
        self.settingsTabWidget.setObjectName(_fromUtf8("settingsTabWidget"))
        self.generalTab = QtGui.QWidget()
        self.generalTab.setObjectName(_fromUtf8("generalTab"))
        self.settingsTabWidget.addTab(self.generalTab, _fromUtf8(""))
        self.serverTab = QtGui.QWidget()
        self.serverTab.setObjectName(_fromUtf8("serverTab"))
        self.addressLabel = QtGui.QLabel(self.serverTab)
        self.addressLabel.setGeometry(QtCore.QRect(40, 40, 41, 16))
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.portLabel = QtGui.QLabel(self.serverTab)
        self.portLabel.setGeometry(QtCore.QRect(40, 70, 21, 16))
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.timeoutLabel = QtGui.QLabel(self.serverTab)
        self.timeoutLabel.setGeometry(QtCore.QRect(40, 130, 101, 16))
        self.timeoutLabel.setObjectName(_fromUtf8("timeoutLabel"))
        self.addressLineEditOctet1 = QtGui.QLineEdit(self.serverTab)
        self.addressLineEditOctet1.setGeometry(QtCore.QRect(90, 40, 31, 20))
        self.addressLineEditOctet1.setObjectName(_fromUtf8("addressLineEditOctet1"))
        self.addressLineEditOctet2 = QtGui.QLineEdit(self.serverTab)
        self.addressLineEditOctet2.setGeometry(QtCore.QRect(130, 40, 31, 20))
        self.addressLineEditOctet2.setObjectName(_fromUtf8("addressLineEditOctet2"))
        self.addressLineEditOctet3 = QtGui.QLineEdit(self.serverTab)
        self.addressLineEditOctet3.setGeometry(QtCore.QRect(170, 40, 31, 20))
        self.addressLineEditOctet3.setObjectName(_fromUtf8("addressLineEditOctet3"))
        self.addressLineEditOctet4 = QtGui.QLineEdit(self.serverTab)
        self.addressLineEditOctet4.setGeometry(QtCore.QRect(210, 40, 31, 20))
        self.addressLineEditOctet4.setObjectName(_fromUtf8("addressLineEditOctet4"))
        self.portLineEdit = QtGui.QLineEdit(self.serverTab)
        self.portLineEdit.setGeometry(QtCore.QRect(80, 70, 51, 20))
        self.portLineEdit.setObjectName(_fromUtf8("portLineEdit"))
        self.timeoutDial = QtGui.QDial(self.serverTab)
        self.timeoutDial.setGeometry(QtCore.QRect(220, 110, 50, 64))
        self.timeoutDial.setMinimum(5)
        self.timeoutDial.setMaximum(120)
        self.timeoutDial.setNotchesVisible(True)
        self.timeoutDial.setObjectName(_fromUtf8("timeoutDial"))
        self.timeoutSpinbox = QtGui.QSpinBox(self.serverTab)
        self.timeoutSpinbox.setGeometry(QtCore.QRect(160, 130, 42, 22))
        self.timeoutSpinbox.setMinimum(5)
        self.timeoutSpinbox.setMaximum(120)
        self.timeoutSpinbox.setObjectName(_fromUtf8("timeoutSpinbox"))
        self.settingsTabWidget.addTab(self.serverTab, _fromUtf8(""))
        self.databaseTab = QtGui.QWidget()
        self.databaseTab.setObjectName(_fromUtf8("databaseTab"))
        self.layoutWidget = QtGui.QWidget(self.databaseTab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 181, 48))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.fileLabel = QtGui.QLabel(self.layoutWidget)
        self.fileLabel.setObjectName(_fromUtf8("fileLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.fileLabel)
        self.fileLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.fileLineEdit.setObjectName(_fromUtf8("fileLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.fileLineEdit)
        self.backendLabel = QtGui.QLabel(self.layoutWidget)
        self.backendLabel.setObjectName(_fromUtf8("backendLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.backendLabel)
        self.backendLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.backendLineEdit.setObjectName(_fromUtf8("backendLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.backendLineEdit)
        self.settingsTabWidget.addTab(self.databaseTab, _fromUtf8(""))
        self.addressLabel.setBuddy(self.addressLineEditOctet1)
        self.portLabel.setBuddy(self.portLineEdit)
        self.timeoutLabel.setBuddy(self.timeoutSpinbox)
        self.fileLabel.setBuddy(self.fileLineEdit)
        self.backendLabel.setBuddy(self.backendLineEdit)

        self.retranslateUi(settingsDialog)
        self.settingsTabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.timeoutSpinbox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.timeoutDial.setValue)
        QtCore.QObject.connect(self.timeoutDial, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.timeoutSpinbox.setValue)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QtGui.QApplication.translate("settingsDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.generalTab), QtGui.QApplication.translate("settingsDialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.addressLabel.setText(QtGui.QApplication.translate("settingsDialog", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.portLabel.setText(QtGui.QApplication.translate("settingsDialog", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.timeoutLabel.setText(QtGui.QApplication.translate("settingsDialog", "Connection Timeout", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.serverTab), QtGui.QApplication.translate("settingsDialog", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.fileLabel.setText(QtGui.QApplication.translate("settingsDialog", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.backendLabel.setText(QtGui.QApplication.translate("settingsDialog", "Backend", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.databaseTab), QtGui.QApplication.translate("settingsDialog", "Database", None, QtGui.QApplication.UnicodeUTF8))

