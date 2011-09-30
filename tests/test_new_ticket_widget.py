try:
    import unittest
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtTest import *
    
    from custom_widgets.newTicketWidget import NewTicketWidget
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TestNewTicketDialogUsage(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = NewTicketWidget()
        
    def testUsage(self):
        QTest.keyClicks(self.gui.firstNameLineEdit, "John")
        QTest.keyClicks(self.gui.lastNameLineEdit, "Orchard")
        QTest.keyClicks(self.gui.houseNumberLineEdit, "8")
        QTest.keyClicks(self.gui.streetLineEdit, "Kensington Place")
        QTest.keyClicks(self.gui.townLineEdit, "Bath")
        QTest.keyClicks(self.gui.postcodeLineEdit, "BA1 6AW")
        QTest.keyClicks(self.gui.vehicleRegistrationLineEdit, "WK55RED")
        
        QTest.keyClicks(self.gui.grossWeightLineEdit, "2500.00")
        QTest.keyClicks(self.gui.tareWeightLineEdit, "1554.00")
        
        self.assertEquals(self.gui.netWeightLineEdit.text(), "946.00")
        self.gui.addPayload()
        self.assertTrue(self.gui.reviewTicketButton.isEnabled())
        
        QTest.keyClicks(self.gui.tareWeightLineEdit, "1")
        
        self.assertFalse(self.gui.tareWeightLineEdit.getValidatedStatus())
        self.assertFalse(self.gui.netWeightLineEdit.getValidatedStatus())
        self.assertTrue(self.gui.reviewTicketButton.isEnabled())
    
    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()
    
if __name__ == "__main__":
    unittest.main()
