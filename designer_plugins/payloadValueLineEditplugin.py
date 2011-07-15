try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4 import QtDesigner
    
    from custom_widgets.payloadValueLineEdit import PayloadValueLineEdit
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class PayloadValueLineEditPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent = None):
        super(PayloadValueLineEditPlugin, self).__init__(parent)

        self.initialised = False
    
    def initialize(self, core):

        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):

        return self.initialized
    
    def createWidget(self, parent):
        return PayloadValueLineEdit(parent)
    
    def name(self):
        return "PayloadValueLineEdit"
    
    def group(self):
        return "Custom Widgets"
    
    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False
    
    def domXml(self):
        return ("<widget class='PayloadValueLineEdit' name=\'payloadValueLineEdit\'>\n"
               " <property name=\"toolTip\" >\n"
               "  <string>Custom Line Edit</string>\n"
               " </property>\n"
               " <property name=\"whatsThis\" >\n"
               "  <string>The analog clock widget displays "
               "the current time.</string>\n"
               " </property>\n"
               "</widget>\n")
               
    def includeFile(self):
        return "custom_widgets.payloadValueLineEdit"