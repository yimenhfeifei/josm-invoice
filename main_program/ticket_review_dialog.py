try:
    import sys
    import re
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import ticket_review_dialog_generated
    from shared_modules.ticket import Ticket
    from shared_modules.regular_expressions import regexObjects
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
        self.customer = ticket.getCustomer()
        self.payload = ticket.getPayload()
        
        self.spanTagContents = regexObjects["SpanTagContents"]
        
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
                                        self.customer["postcode"],
                                        self.postcodeLabel.text()))
        
        self.vehicleRegistrationLabel.setText(re.sub(self.spanTagContents,
                                        self.customer["registration"],
                                        self.vehicleRegistrationLabel.text()))
        
        self.addPayloads()
        self.addTotalValue()
        
    def buildName(self):
        return " ".join([self.customer["firstName"],
                         self.customer["lastName"]])
    
    def buildAddress(self):
        return ", ".join([self.customer["houseNumber"],
                         self.customer["street"],
                         self.customer["town"]])
    
    def addTotalValue(self):
        total = QLabel(re.sub(self.spanTagContents,
                              "Total:",
                              self.numberLabel.text()))
        
        total.setAlignment(Qt.AlignHCenter)
        
        self.payloadLayout.addWidget(total,
                                     self.payloadLayout.rowCount(),
                                     2)
        
        totalValue = QLabel(re.sub(self.spanTagContents,
                                   self.ticket["totalValue"],
                                   self.numberLabel.text()))
        
        totalValue.setAlignment(Qt.AlignHCenter)
        
        self.payloadLayout.addWidget(totalValue,
                                     self.payloadLayout.rowCount()-1,
                                     3)
    
    def addPayloads(self):
        for row in range(len(self.payload.keys())):
            payload = "payload {}".format(row)
            
            payloadValues = [QLabel(self.payload[payload]["weight"]),
                     QLabel(self.payload[payload]["material"]),
                     QLabel(self.payload[payload]["value"])]
            
            for column, item in enumerate(payloadValues):
                item.setAlignment(Qt.AlignHCenter)
                self.payloadLayout.addWidget(item, row+1, column+1)
        