try:
    import sys
    import re
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import invoice_review_dialog_generated
    from shared_modules.regular_expressions import regexObjects
    from business_customers import customers
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class InvoiceReviewDialog(QDialog,
                      invoice_review_dialog_generated.Ui_invoiceReviewDialog):

    def __init__(self, details, payloads, parent=None):
        super(InvoiceReviewDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Invoice Review")
        
        self.spanTagContents = regexObjects["spanTagContents"]
        
        self.addInvoiceDetails(details)
        self.addPayloads(payloads)
        
    def addInvoiceDetails(self, details):
        name = details["name"]
        personalDetails = customers[name]
        
        self.numberLabel.setText(re.sub(self.spanTagContents,
                                        details["number"],
                                        self.numberLabel.text()))
        
        self.dateLabel.setText(re.sub(self.spanTagContents,
                                        details["date"],
                                        self.dateLabel.text()))
        
        self.nameLabel.setText(re.sub(self.spanTagContents,
                                        details["name"],
                                        self.nameLabel.text()))
        
        self.addressLabel.setText(re.sub(self.spanTagContents,
                                        personalDetails["address"],
                                        self.addressLabel.text()))
        
        self.vatRegLabel.setText(re.sub(self.spanTagContents,
                                        personalDetails["vatReg"],
                                        self.vatRegLabel.text()))
        
        self.payloadTotalLabel.setText(re.sub(self.spanTagContents,
                                              details["payloadTotal"],
                                              self.payloadTotalLabel.text()))
        
        self.vatTotalLabel.setText(re.sub(self.spanTagContents,
                                          details["vatTotal"],
                                          self.vatTotalLabel.text()))
        
        self.grandTotalLabel.setText(re.sub(self.spanTagContents,
                                            details["grandTotal"],
                                            self.grandTotalLabel.text()))

    def addPayloads(self, payloads):
        for row, payload in enumerate(payloads.values()):
            payloadValues = [QLabel(payload["description"]),
                             QLabel(payload["weight"]),
                             QLabel(payload["ppu"]),
                             QLabel(payload["value"])]
                
            for column, item in enumerate(payloadValues):
                item.setAlignment(Qt.AlignHCenter)
                self.payloadLayout.addWidget(item, row+1, column)