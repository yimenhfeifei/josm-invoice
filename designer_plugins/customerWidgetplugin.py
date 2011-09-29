try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4 import QtDesigner
    
    from custom_widgets.customerWidget import CustomerWidget
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class CustomerWidgetPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent = None):
        super(CustomerWidgetPlugin, self).__init__(parent)

        self.initialised = False
    
    def initialize(self, core):

        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):

        return self.initialized
    
    def createWidget(self, parent):
        return CustomerWidget(parent)
    
    def name(self):
        return "CustomerWidget"
    
    def group(self):
        return "Custom Widgets"
    
    def toolTip(self):
        return "Customer details."

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False
    
    def domXml(self):
        return ("<widget class='CustomerWidget' name='customerWidget'>\n"
               " <property name=\"toolTip\" >\n"
               "  <string>Customer details.</string>\n"
               " </property>\n"
               " <property name=\"whatsThis\" >\n"
               "  <string>Customer details widget.</string>\n"
               " </property>\n"
               "</widget>\n")
               
    def includeFile(self):
        return "custom_widgets.customerWidget"