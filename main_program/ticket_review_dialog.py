try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import ticket_review_dialog_generated
    from shared_modules.ticket import Ticket
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TicketReviewDialog(QDialog,
                      ticket_review_dialog_generated.Ui_ticketReviewDialog):

    def __init__(self, parent=None):
        super(TicketReviewDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Review Ticket")
        