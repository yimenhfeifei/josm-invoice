#!/usr/bin/env python3
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


class backdateDialog(QDialog):

    def __init__(self, parent=None):
        super(backdateDialog, self).__init__(parent)

        self.dateWidget = QDateEdit(calendarPopup=True,
                                    date=QDate().currentDate(),
                                    displayFormat="dd/MM/yyyy")
        
        self.sections = QDateEdit.DaySection | QDateEdit.YearSection
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.mainLayout = QVBoxLayout()

        self.widgetLayout = QVBoxLayout()

        self.widgetLayout.addWidget(self.dateWidget)
        
        self.widgetLayout.addWidget(self.buttonBox)

        self.mainLayout.addLayout(self.widgetLayout)

        self.setLayout(self.mainLayout)
        
        self.connect(self.buttonBox, SIGNAL("accepted()"),
                     self.accept)
        
        self.connect(self.buttonBox, SIGNAL("rejected()"),
                             self.reject)        
