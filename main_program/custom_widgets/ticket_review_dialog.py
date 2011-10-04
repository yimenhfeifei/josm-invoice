try:
    import sys
    import re
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import ticket_review_dialog_generated
    from shared_modules.ticket import Ticket
    from shared_modules.regular_expressions import regexObjects
    from shared_modules.widgetPrinter import WidgetPrinter
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TicketReviewDialog(QDialog,
                      ticket_review_dialog_generated.Ui_ticketReviewDialog):

    def __init__(self, ticket, parent=None):
        super(TicketReviewDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Review Ticket")
       
        self.ticket = ticket.getTicket()
        
        self.connect(self.confirmButtonbox, SIGNAL("accepted()"),
                     self.submitTicket)
        
        self.connect(self.confirmButtonbox, SIGNAL("rejected()"),
                     self.cancelSumbit)
        
        self.spanTagContents = regexObjects["spanTagContents"]
        
        self.numberLabel.setText(re.sub(self.spanTagContents,
                                        self.ticket["number"],
                                        self.numberLabel.text()))
        
        self.hashIdLabel.setText(re.sub(self.spanTagContents,
                                        self.ticket["hashId"],
                                        self.hashIdLabel.text()))
        
        self.dateLabel.setText(re.sub(self.spanTagContents,
                                        self.ticket["date"],
                                        self.dateLabel.text()))
        
        self.timeLabel.setText(re.sub(self.spanTagContents,
                                        self.ticket["time"],
                                        self.timeLabel.text()))
        
        self.nameLabel.setText(re.sub(self.spanTagContents,
                                        self.buildName(),
                                        self.nameLabel.text()))
        
        self.addressLabel.setText(re.sub(self.spanTagContents,
                                        self.buildAddress(),
                                        self.addressLabel.text()))
        
        self.postcodeLabel.setText(re.sub(self.spanTagContents,
                                        self.ticket["postcode"],
                                        self.postcodeLabel.text()))
        
        self.vehicleRegistrationLabel.setText(re.sub(self.spanTagContents,
                                        self.ticket["customerReg"],
                                        self.vehicleRegistrationLabel.text()))
        
        self.addPayloads()
        self.addTotal()
        
        self.printer = WidgetPrinter(self, 300, QPrinter.HighResolution)
        
    def submitTicket(self):
        self.confirmButtonbox.hide()
        self.printer.showPrintDialog()
        self.accept()
        
    def cancelSumbit(self):
        self.reject()
        
    def buildName(self):
        return " ".join([self.ticket["firstName"],
                         self.ticket["lastName"]])
    
    def buildAddress(self):
        return ", ".join([self.ticket["houseNumber"],
                         self.ticket["street"],
                         self.ticket["town"]])
    
    def addTotal(self):
        totalRow = self.payloadLayout.rowCount()
        self.addTotalLabel(totalRow)
        self.addTotalValue(totalRow)
        
    def addTotalValue(self, totalRow):
        totalValue = QLabel(re.sub(self.spanTagContents,
                                   self.ticket["ticketValue"],
                                   self.numberLabel.text()))
        
        totalValue.setAlignment(Qt.AlignHCenter)
        
        self.payloadLayout.addWidget(totalValue, totalRow, 2)
        
    def addTotalLabel(self, totalRow):
        totalLabel = QLabel(re.sub(self.spanTagContents,
                              "Total:",
                              self.numberLabel.text()))
        
        totalLabel.setAlignment(Qt.AlignHCenter)
        
        self.payloadLayout.addWidget(totalLabel, totalRow, 1)
    
    def addPayloads(self):
        for key, value in self.ticket.items():
            match = re.search(r"[0-9]{1,3}", key, re.I)
            if match:
                payloadValues = [QLabel(value["weight"]),
                                 QLabel(value["material"]),
                                 QLabel(value["value"])]
                
                for column, item in enumerate(payloadValues):
                    item.setAlignment(Qt.AlignHCenter)
                    self.payloadLayout.addWidget(item, int(match.group(0))+1, column)
        