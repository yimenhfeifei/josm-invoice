# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'car_widget_design.ui'
#
# Created: Tue May 17 13:54:08 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_carWidget(object):
    def setupUi(self, carWidget):
        carWidget.setObjectName(_fromUtf8("carWidget"))
        carWidget.resize(309, 180)
        self.layoutWidget = QtGui.QWidget(carWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 257, 152))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.makeLineEdit = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.makeLineEdit.sizePolicy().hasHeightForWidth())
        self.makeLineEdit.setSizePolicy(sizePolicy)
        self.makeLineEdit.setMinimumSize(QtCore.QSize(181, 0))
        self.makeLineEdit.setMaximumSize(QtCore.QSize(181, 16777215))
        self.makeLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.makeLineEdit.setObjectName(_fromUtf8("makeLineEdit"))
        self.gridLayout.addWidget(self.makeLineEdit, 0, 1, 1, 2)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.modelLineEdit = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelLineEdit.sizePolicy().hasHeightForWidth())
        self.modelLineEdit.setSizePolicy(sizePolicy)
        self.modelLineEdit.setMinimumSize(QtCore.QSize(181, 0))
        self.modelLineEdit.setMaximumSize(QtCore.QSize(181, 16777215))
        self.modelLineEdit.setObjectName(_fromUtf8("modelLineEdit"))
        self.gridLayout.addWidget(self.modelLineEdit, 1, 1, 1, 2)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.colourLineEdit = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colourLineEdit.sizePolicy().hasHeightForWidth())
        self.colourLineEdit.setSizePolicy(sizePolicy)
        self.colourLineEdit.setMinimumSize(QtCore.QSize(101, 0))
        self.colourLineEdit.setMaximumSize(QtCore.QSize(101, 16777215))
        self.colourLineEdit.setObjectName(_fromUtf8("colourLineEdit"))
        self.gridLayout.addWidget(self.colourLineEdit, 2, 1, 1, 2)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.registrationLineEdit = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registrationLineEdit.sizePolicy().hasHeightForWidth())
        self.registrationLineEdit.setSizePolicy(sizePolicy)
        self.registrationLineEdit.setMinimumSize(QtCore.QSize(101, 0))
        self.registrationLineEdit.setMaximumSize(QtCore.QSize(101, 20))
        self.registrationLineEdit.setStyleSheet(_fromUtf8("QLineEdit {background-color: red;}"))
        self.registrationLineEdit.setObjectName(_fromUtf8("registrationLineEdit"))
        self.gridLayout.addWidget(self.registrationLineEdit, 3, 1, 1, 2)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.vinLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.vinLineEdit.setMinimumSize(QtCore.QSize(191, 0))
        self.vinLineEdit.setMaximumSize(QtCore.QSize(191, 16777215))
        self.vinLineEdit.setObjectName(_fromUtf8("vinLineEdit"))
        self.gridLayout.addWidget(self.vinLineEdit, 4, 1, 1, 2)
        self.catalyticCheckbox = QtGui.QCheckBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catalyticCheckbox.sizePolicy().hasHeightForWidth())
        self.catalyticCheckbox.setSizePolicy(sizePolicy)
        self.catalyticCheckbox.setMinimumSize(QtCore.QSize(117, 17))
        self.catalyticCheckbox.setMaximumSize(QtCore.QSize(117, 17))
        self.catalyticCheckbox.setObjectName(_fromUtf8("catalyticCheckbox"))
        self.gridLayout.addWidget(self.catalyticCheckbox, 5, 0, 1, 2)
        self.catalyticLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.catalyticLineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catalyticLineEdit.sizePolicy().hasHeightForWidth())
        self.catalyticLineEdit.setSizePolicy(sizePolicy)
        self.catalyticLineEdit.setMinimumSize(QtCore.QSize(61, 0))
        self.catalyticLineEdit.setMaximumSize(QtCore.QSize(61, 16777215))
        self.catalyticLineEdit.setObjectName(_fromUtf8("catalyticLineEdit"))
        self.gridLayout.addWidget(self.catalyticLineEdit, 5, 2, 1, 1)
        self.label_8.setBuddy(self.makeLineEdit)
        self.label_9.setBuddy(self.modelLineEdit)
        self.label_10.setBuddy(self.colourLineEdit)
        self.label_11.setBuddy(self.registrationLineEdit)
        self.label.setBuddy(self.vinLineEdit)

        self.retranslateUi(carWidget)
        QtCore.QObject.connect(self.catalyticCheckbox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.catalyticLineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(carWidget)
        carWidget.setTabOrder(self.makeLineEdit, self.modelLineEdit)
        carWidget.setTabOrder(self.modelLineEdit, self.colourLineEdit)
        carWidget.setTabOrder(self.colourLineEdit, self.registrationLineEdit)
        carWidget.setTabOrder(self.registrationLineEdit, self.vinLineEdit)
        carWidget.setTabOrder(self.vinLineEdit, self.catalyticCheckbox)
        carWidget.setTabOrder(self.catalyticCheckbox, self.catalyticLineEdit)

    def retranslateUi(self, carWidget):
        carWidget.setWindowTitle(QtGui.QApplication.translate("carWidget", "carWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("carWidget", "Make", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("carWidget", "Model", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("carWidget", "Colour", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("carWidget", "Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("carWidget", "VIN", None, QtGui.QApplication.UnicodeUTF8))
        self.catalyticCheckbox.setText(QtGui.QApplication.translate("carWidget", "Catalytic Converter", None, QtGui.QApplication.UnicodeUTF8))

