#!/usr/bin/python3
try:
    import traceback
    import sys

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from shared_modules.extendedCombobox import ExtendedComboBox

except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)


class Ui_invoiceWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_invoiceWindow, self).__init__(parent)
        self.resize(840, 670)
        self.setWindowTitle("Invoice")
        self.centralwidget = QWidget(self)
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6 = QVBoxLayout()
        self.horizontalLayout_3 = QHBoxLayout()

        spacerItem = QSpacerItem(58, 20, QSizePolicy.Expanding,
                                 QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(spacerItem)
        self.dataEntryBox = QGroupBox(self.centralwidget)

        self.dataEntryBox.setTitle(QApplication.translate("invoiceWindow",
                                                          "Data entry",
                                                          None,
                                                          QApplication.UnicodeUTF8))

        self.dataEntryBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_5 = QVBoxLayout(self.dataEntryBox)
        self.horizontalLayout_7 = QHBoxLayout()
        spacerItem1 = QSpacerItem(238, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.typeCombobox = ExtendedComboBox(self.dataEntryBox)
        self.horizontalLayout_7.addWidget(self.typeCombobox)
        spacerItem2 = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QHBoxLayout()
        spacerItem3 = QSpacerItem(238, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.customerCombobox = ExtendedComboBox(self.dataEntryBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customerCombobox.sizePolicy().hasHeightForWidth())

        self.customerCombobox.setSizePolicy(sizePolicy)
        self.customerCombobox.setMaxVisibleItems(20)
        self.customerCombobox.setMaxCount(100)
        self.customerCombobox.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.customerCombobox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_2.addWidget(self.customerCombobox)
        spacerItem4 = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QHBoxLayout()
        spacerItem5 = QSpacerItem(190, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.label_5 = QLabel(self.dataEntryBox)

        self.label_5.setText(QApplication.translate("invoiceWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">VAT %</span></p></body></html>", None, QApplication.UnicodeUTF8))

        self.horizontalLayout_6.addWidget(self.label_5)
        self.vatEdit = QLineEdit(self.dataEntryBox)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vatEdit.sizePolicy().hasHeightForWidth())

        self.vatEdit.setSizePolicy(sizePolicy)
        self.vatEdit.setMaximumSize(QSize(50, 16777215))

        self.vatEdit.setText(QApplication.translate("invoiceWindow",
                                                    "20",
                                                    None,
                                                    QApplication.UnicodeUTF8))

        self.horizontalLayout_6.addWidget(self.vatEdit)

        spacerItem6 = QSpacerItem(245, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QHBoxLayout()
        spacerItem7 = QSpacerItem(190, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.numberLabel = QLabel(self.dataEntryBox)

        self.numberLabel.setText(QApplication.translate("invoiceWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Number</span></p></body></html>", None, QApplication.UnicodeUTF8))

        self.horizontalLayout_8.addWidget(self.numberLabel)
        self.numberEdit = QLineEdit(self.dataEntryBox)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberEdit.sizePolicy().hasHeightForWidth())

        self.numberEdit.setSizePolicy(sizePolicy)
        self.numberEdit.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_8.addWidget(self.numberEdit)
        spacerItem8 = QSpacerItem(245, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem9 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem9)
        self.line = QFrame(self.dataEntryBox)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_5.addWidget(self.line)
        self.checkBox = QCheckBox(self.dataEntryBox)
        self.checkBox.setText(QApplication.translate("invoiceWindow",
                                                     "Show unit options",
                                                     None,
                                                     QApplication.UnicodeUTF8))
        self.verticalLayout_5.addWidget(self.checkBox)

        self.unitFrame = QFrame(self.dataEntryBox)
        self.unitFrame.resize(281, 129)
        self.unitFrame.setFrameShape(QFrame.StyledPanel)
        self.unitFrame.setFrameShadow(QFrame.Raised)
        self.unitFrame.horizontalLayout = QHBoxLayout(self.unitFrame)
        self.unitFrame.weightUnitBox = QGroupBox(self.unitFrame)
        self.unitFrame.weightUnitBox.setTitle(QApplication.translate("unitFrame",
                                                           "Weight unit",
                                                           None,
                                                           QApplication.UnicodeUTF8))

        self.unitFrame.weightUnitBox.setAlignment(Qt.AlignCenter)
        self.unitFrame.verticalLayout = QVBoxLayout(self.unitFrame.weightUnitBox)
        self.unitFrame.weightKgRadio = QRadioButton(self.unitFrame.weightUnitBox)

        self.unitFrame.weightKgRadio.setText(QApplication.translate("unitFrame",
                                                          "Kg",
                                                          None,
                                                          QApplication.UnicodeUTF8))

        self.unitFrame.weightKgRadio.setAutoExclusive(True)
        self.unitFrame.verticalLayout.addWidget(self.unitFrame.weightKgRadio)
        self.unitFrame.weightTonnesRadio = QRadioButton(self.unitFrame.weightUnitBox)

        self.unitFrame.weightTonnesRadio.setText(QApplication.translate("unitFrame",
                                                              "Tonnes",
                                                              None,
                                                              QApplication.UnicodeUTF8))

        self.unitFrame.weightTonnesRadio.setAutoExclusive(True)
        self.unitFrame.verticalLayout.addWidget(self.unitFrame.weightTonnesRadio)
        self.unitFrame.horizontalLayout.addWidget(self.unitFrame.weightUnitBox)
        self.unitFrame.priceUnitBox = QGroupBox(self.unitFrame)

        self.unitFrame.priceUnitBox.setTitle(QApplication.translate("unitFrame",
                                                          "Price unit",
                                                          None,
                                                          QApplication.UnicodeUTF8))

        self.unitFrame.priceUnitBox.setAlignment(Qt.AlignCenter)
        self.unitFrame.verticalLayout_2 = QVBoxLayout(self.unitFrame.priceUnitBox)
        self.unitFrame.priceKgRadio = QRadioButton(self.unitFrame.priceUnitBox)

        self.unitFrame.priceKgRadio.setText(QApplication.translate("unitFrame",
                                                         "Kg",
                                                         None,
                                                         QApplication.UnicodeUTF8))

        self.unitFrame.priceKgRadio.setAutoExclusive(True)
        self.unitFrame.verticalLayout_2.addWidget(self.unitFrame.priceKgRadio)
        self.unitFrame.priceTonnesRadio = QRadioButton(self.unitFrame.priceUnitBox)

        self.unitFrame.priceTonnesRadio.setText(QApplication.translate("unitFrame",
                                                             "Tonnes",
                                                             None,
                                                             QApplication.UnicodeUTF8))

        self.unitFrame.priceTonnesRadio.setAutoExclusive(True)
        self.unitFrame.verticalLayout_2.addWidget(self.unitFrame.priceTonnesRadio)
        self.unitFrame.horizontalLayout.addWidget(self.unitFrame.priceUnitBox)

        self.unitFrame.setToolTip(QApplication.translate("invoiceWindow",
                                                         "Extended table widget.",
                                                         None,
                                                         QApplication.UnicodeUTF8))

        self.unitFrame.setWhatsThis(QApplication.translate("invoiceWindow",
                                                           "Extended table widget.",
                                                           None,
                                                           QApplication.UnicodeUTF8))

        self.verticalLayout_5.addWidget(self.unitFrame)

        self.horizontalLayout = QHBoxLayout()
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.label = QLabel(self.dataEntryBox)

        self.label.setText(QApplication.translate("invoiceWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Description</span></p></body></html>", None, QApplication.UnicodeUTF8))

        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)
        self.descriptionEdit = QLineEdit(self.dataEntryBox)
        self.descriptionEdit.setMaximumSize(QSize(230, 16777215))
        self.verticalLayout.addWidget(self.descriptionEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QVBoxLayout()
        self.weightLabel = QLabel(self.dataEntryBox)

        self.weightLabel.setText(QApplication.translate("invoiceWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Weight (Tonnes)</span></p></body></html>", None, QApplication.UnicodeUTF8))

        self.weightLabel.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.weightLabel)
        self.weightEdit = QLineEdit(self.dataEntryBox)
        self.weightEdit.setMaximumSize(QSize(111, 16777215))
        self.verticalLayout_4.addWidget(self.weightEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QVBoxLayout()
        self.pricePerUnitLabel = QLabel(self.dataEntryBox)

        self.pricePerUnitLabel.setText(QApplication.translate("invoiceWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Price (Tonnes)</span></p></body></html>", None, QApplication.UnicodeUTF8))

        self.pricePerUnitLabel.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.pricePerUnitLabel)
        self.pricePerUnitEdit = QLineEdit(self.dataEntryBox)
        self.pricePerUnitEdit.setMaximumSize(QSize(111, 16777215))
        self.verticalLayout_3.addWidget(self.pricePerUnitEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QVBoxLayout()
        self.label_4 = QLabel(self.dataEntryBox)

        self.label_4.setText(QApplication.translate("invoiceWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Value</span></p></body></html>", None, QApplication.UnicodeUTF8))

        self.label_4.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.label_4)
        self.valueEdit = QLineEdit(self.dataEntryBox)
        self.valueEdit.setMaximumSize(QSize(111, 16777215))
        self.verticalLayout_2.addWidget(self.valueEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.addButton = QPushButton(self.dataEntryBox)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)

        self.addButton.setText(QApplication.translate("invoiceWindow",
                                                      "Add",
                                                      None,
                                                      QApplication.UnicodeUTF8))

        self.addButton.setShortcut(QApplication.translate("invoiceWindow",
                                                          "Return",
                                                          None,
                                                          QApplication.UnicodeUTF8))

        self.horizontalLayout.addWidget(self.addButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addWidget(self.dataEntryBox)
        spacerItem10 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QHBoxLayout()
        spacerItem11 = QSpacerItem(78, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.invoiceTable = InvoiceTable(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoiceTable.sizePolicy().hasHeightForWidth())
        self.invoiceTable.setSizePolicy(sizePolicy)

        self.invoiceTable.setToolTip(QApplication.translate("invoiceWindow",
                                                            "Current payloads.",
                                                            None,
                                                            QApplication.UnicodeUTF8))

        self.invoiceTable.setWhatsThis(QApplication.translate("invoiceWindow",
                                                              "PayloadTable widget.",
                                                              None,
                                                              QApplication.UnicodeUTF8))

        self.invoiceTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.invoiceTable.setAlternatingRowColors(True)
        self.invoiceTable.setShowGrid(False)
        self.invoiceTable.setRowCount(0)
        self.invoiceTable.horizontalHeader().setDefaultSectionSize(120)
        self.invoiceTable.horizontalHeader().setHighlightSections(False)
        self.invoiceTable.horizontalHeader().setMinimumSectionSize(120)
        self.invoiceTable.horizontalHeader().setSortIndicatorShown(False)
        self.invoiceTable.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_4.addWidget(self.invoiceTable)

        spacerItem12 = QSpacerItem(78, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_5 = QHBoxLayout()
        spacerItem13 = QSpacerItem(618, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.reviewButton = QCommandLinkButton(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reviewButton.sizePolicy().hasHeightForWidth())

        self.reviewButton.setSizePolicy(sizePolicy)
        self.reviewButton.setMaximumSize(QSize(168, 41))
        self.reviewButton.setText(QApplication.translate("invoiceWindow",
                                                         "Review invoice",
                                                         None,
                                                         QApplication.UnicodeUTF8))

        self.horizontalLayout_5.addWidget(self.reviewButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 840, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setTitle(QApplication.translate("invoiceWindow",
                                                      "&File",
                                                      None,
                                                      QApplication.UnicodeUTF8))
        
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setTitle(QApplication.translate("invoiceWindow",
                                                      "&Edit",
                                                      None,
                                                      QApplication.UnicodeUTF8))        

        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setTitle(QApplication.translate("invoiceWindow",
                                                      "&Help",
                                                      None,
                                                      QApplication.UnicodeUTF8))

        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setTitle(QApplication.translate("invoiceWindow",
                                                         "Options",
                                                         None,
                                                         QApplication.UnicodeUTF8))

        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.actionQuit = QAction(self)
        self.actionQuit.setText(QApplication.translate("invoiceWindow",
                                                       "&Quit",
                                                       None,
                                                       QApplication.UnicodeUTF8))

        self.actionQuit.setShortcut(QApplication.translate("invoiceWindow",
                                                           "Ctrl+Q",
                                                           None,
                                                           QApplication.UnicodeUTF8))
        
        self.actionQuit.setStatusTip("Quits the program.")

        self.actionAboutInvoice = QAction(self)
        self.actionAboutInvoice.setText(QApplication.translate("invoiceWindow",
                                                               "About &Invoice",
                                                               None,
                                                               QApplication.UnicodeUTF8))

        self.actionAboutInvoice.setShortcut(QApplication.translate("invoiceWindow",
                                                                   "Ctrl+I",
                                                                   None,
                                                                   QApplication.UnicodeUTF8))
        
        self.actionAboutInvoice.setStatusTip("Shows a dialog which displays program information.")
        
        self.actionAboutQt = QAction(self)
        self.actionAboutQt.setText(QApplication.translate("invoiceWindow",
                                                          "About &Qt",
                                                          None,
                                                          QApplication.UnicodeUTF8))
       
        self.actionAboutQt.setShortcut(QApplication.translate("invoiceWindow",
                                                              "Ctrl+K",
                                                              None,
                                                              QApplication.UnicodeUTF8))
        
        self.actionAboutQt.setStatusTip("Shows a dialog which displays information about Qt.")

        self.actionPrintPreview = QAction(self)
        self.actionPrintPreview.setText(QApplication.translate("invoiceWindow",
                                                               "&Print Preview",
                                                               None,
                                                               QApplication.UnicodeUTF8))

        self.actionPrintPreview.setShortcut(QApplication.translate("invoiceWindow",
                                                                   "Ctrl+P",
                                                                   None,
                                                                   QApplication.UnicodeUTF8))
        
        self.actionPrintPreview.setStatusTip("Allows printing and previewing of final output.")

        self.actionToggleAutoCalc = QAction(self)
        self.actionToggleAutoCalc.setText(QApplication.translate("invoiceWindow",
                                                                 "&Toggle Auto Calc",
                                                                 None,
                                                                 QApplication.UnicodeUTF8))

        self.actionToggleAutoCalc.setShortcut(QApplication.translate("invoiceWindow",
                                                                     "Ctrl+T",
                                                                     None,
                                                                     QApplication.UnicodeUTF8))
        
        self.actionToggleAutoCalc.setStatusTip("Toggles whether or not payload values are automatically calculated.")
        
        self.actionDatabaseDialog = QAction(self)
        self.actionDatabaseDialog.setText(QApplication.translate("Edit Database",
                                                                 "Edit &Database",
                                                                 None,
                                                                 QApplication.UnicodeUTF8))
        
        self.actionDatabaseDialog.setShortcut(QApplication.translate("Edit Database",
                                                                     "Ctrl+D",
                                                                     None,
                                                                     QApplication.UnicodeUTF8))
        
        self.actionDatabaseDialog.setStatusTip("Allows editing of customer information.")
        
        self.actionRevert = QAction(self)
        self.actionRevert.setText(QApplication.translate("Revert",
                                                         "R&evert",
                                                         None,
                                                         QApplication.UnicodeUTF8))
            
        self.actionRevert.setShortcut(QApplication.translate("Revert",
                                                             "Ctrl+E",
                                                             None,
                                                             QApplication.UnicodeUTF8))
        
        self.actionRevert.setStatusTip("Reverts the form to the last invoice that was printed in this session.")
        
        self.actionResetForm = QAction(self)
        self.actionResetForm.setText(QApplication.translate("Reset Form",
                                                            "&Reset Form",
                                                            None,
                                                            QApplication.UnicodeUTF8))
                    
        self.actionResetForm.setShortcut(QApplication.translate("Reset Form",
                                                                "Ctrl+R",
                                                                None,
                                                                QApplication.UnicodeUTF8))
        
        self.actionResetForm.setStatusTip("Resets the program to its default state.")
        
        self.actionSaveVat = QAction(self)
        self.actionSaveVat.setText(QApplication.translate("Save VAT",
                                                          "&Save VAT",
                                                          None,
                                                          QApplication.UnicodeUTF8))        
        
        self.actionSaveVat.setShortcut(QApplication.translate("Save VAT",
                                                              "Ctrl+S",
                                                              None,
                                                              QApplication.UnicodeUTF8))
                
        self.actionSaveVat.setStatusTip("Saves the current VAT rate to file, making it the default for the program.")

        self.menuFile.addAction(self.actionPrintPreview)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionDatabaseDialog)
        self.menuEdit.addAction(self.actionRevert)
        self.menuEdit.addAction(self.actionResetForm)  
        self.menuEdit.addAction(self.actionSaveVat) 
        self.menuHelp.addAction(self.actionAboutInvoice)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuOptions.addAction(self.actionToggleAutoCalc)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        QObject.connect(self.checkBox, SIGNAL("toggled(bool)"), self.unitFrame.setVisible)
        self.setTabOrder(self.addButton, self.invoiceTable)
        self.setTabOrder(self.invoiceTable, self.reviewButton)
        self.setTabOrder(self.reviewButton, self.typeCombobox)
        self.setTabOrder(self.typeCombobox, self.customerCombobox)

from view.invoiceTable import InvoiceTable
