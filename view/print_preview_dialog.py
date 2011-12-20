#!/usr/bin/python3
try:
    import traceback
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)

class PrintPreviewDialogExtended(QDialog):
    
    def __init__(self, printer, parent=None):
        super(PrintPreviewDialogExtended, self).__init__(parent)
        
        self.resize(600, 800)
        
        self.printer = printer
        
        self.previewWidget = QPrintPreviewWidget(self.printer, self)
        previewWidget.setZoomFactor(1.0)
        previewWidget.setZoomMode(1)
        
        self.toolBar = QToolBar(self)
        
        self.actionFitToWidth = QAction(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/fit-width-32.png"),
                                    "",
                                    self)
        
        self.actionPrint = QAction(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/print-32.png"),
                                    "",
                                    self)
        
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addAction(self.actionFitToWidth)
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.toolBar)
        self.mainLayout.addWidget(self.previewWidget)
        self.setLayout(self.mainLayout)
