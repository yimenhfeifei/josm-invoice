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
        
        self.spanTagContents = regexObjects["SpanTagContents"]
        
        self.numberLabel.setText(re.sub(self.spanTagContents,
                                        ticket.getTicket()["number"],
                                        self.numberLabel.text()))
        
        self.hashIdLabel.setText(re.sub(self.spanTagContents,
                                        ticket.getTicket()["hashId"],
                                        self.hashIdLabel.text()))
        
        self.dateLabel.setText(re.sub(self.spanTagContents,
                                        ticket.getTicket()["date"],
                                        self.dateLabel.text()))
        
        self.timeLabel.setText(re.sub(self.spanTagContents,
                                        ticket.getTicket()["time"],
                                        self.timeLabel.text()))
        
        firstName = ticket.getCustomer()["firstName"]
        lastName = ticket.getCustomer()["lastName"]
        fullName = firstName + " " + lastName
        
        self.nameLabel.setText(re.sub(self.spanTagContents,
                                        fullName,
                                        self.nameLabel.text()))
        
        address = ", ".join([ticket.getCustomer()["houseNumber"],
                            ticket.getCustomer()["street"],
                            ticket.getCustomer()["town"]])
        
        self.addressLabel.setText(re.sub(self.spanTagContents,
                                        address,
                                        self.addressLabel.text()))
        
        self.postcodeLabel.setText(re.sub(self.spanTagContents,
                                        ticket.getCustomer()["postcode"],
                                        self.postcodeLabel.text()))
        
        self.vehicleRegistrationLabel.setText(re.sub(self.spanTagContents,
                                        ticket.getCustomer()["registration"],
                                        self.vehicleRegistrationLabel.text()))
        