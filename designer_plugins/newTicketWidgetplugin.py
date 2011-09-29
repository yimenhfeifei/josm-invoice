try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4 import QtDesigner
    
    from custom_widgets.newTicketWidget import NewTicketWidget
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class NewTicketWidgetPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(NewTicketWidgetPlugin, self).__init__(parent)

        self.initialised = False
    
    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized
    
    def createWidget(self, parent):
        return NewTicketWidget(parent)
    
    def name(self):
        return "NewTicketWidget"
    
    def group(self):
        return "Custom Widgets"
    
    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False
    
    def domXml(self):
        return ("<widget class='NewTicketWidget' name='newTicketWidget'>\n"
               " <property name=\"toolTip\" >\n"
               "  <string>New ticket.</string>\n"
               " </property>\n"
               " <property name=\"whatsThis\" >\n"
               "  <string>Allows entry of new ticket.</string>\n"
               " </property>\n"
               "</widget>\n")
               
    def includeFile(self):
        return "custom_widgets.newTicketWidget"