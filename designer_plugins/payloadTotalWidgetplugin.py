try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4 import QtDesigner
    
    from custom_widgets.payloadTotalWidget import PayloadTotalWidget
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class PayloadTotalWidgetPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent = None):
        super(PayloadTotalWidgetPlugin, self).__init__(parent)

        self.initialised = False
    
    def initialize(self, core):

        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):

        return self.initialized
    
    def createWidget(self, parent):
        return PayloadTotalWidget(parent)
    
    def name(self):
        return "PayloadTotalWidget"
    
    def group(self):
        return "Custom Widgets"
    
    def toolTip(self):
        return "Total for current material and weight."

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False
    
    def domXml(self):
        return ("<widget class='PayloadTotalWidget' name='payloadTotalWidget'>\n"
               " <property name=\"toolTip\" >\n"
               "  <string>Current payload total.</string>\n"
               " </property>\n"
               " <property name=\"whatsThis\" >\n"
               "  <string>Payload total.</string>\n"
               " </property>\n"
               "</widget>\n")
               
    def includeFile(self):
        return "custom_widgets.payloadTotalWidget"