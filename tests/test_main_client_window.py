try:
    import unittest
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtTest import *
    
    from main_client_window import MainClientWindow
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TestMainClientWindowGui(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = MainClientWindow()
        self.testString = "It works!"
    
    def testCreateMainClientWindow(self):
        assert self.gui != False

    def tearDown(self):
        self.gui.deleteLater()
        self.app.deleteLater()

suite1 = unittest.makeSuite(TestMainClientWindowGui, "test")
    
if __name__ == "__main__":
    unittest.main()