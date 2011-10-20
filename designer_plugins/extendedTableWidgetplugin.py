try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4 import QtDesigner
    
    from custom_widgets.extendedTableWidget import ExtendedTableWidget
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class ExtendedTableWidgetPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(ExtendedTableWidgetPlugin, self).__init__(parent)

        self.initialised = False
    
    def initialize(self, core):

        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):

        return self.initialized
    
    def createWidget(self, parent):
        return ExtendedTableWidget(parent)
    
    def name(self):
        return "ExtendedTableWidget"
    
    def group(self):
        return "Custom Widgets"
    
    def toolTip(self):
        return "Custom table widget with various extensions."

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False
    
    def domXml(self):
        return ("<widget class='ExtendedTableWidget' name='extendedTableWidget'>\n"
               " <property name=\"toolTip\" >\n"
               "  <string>Extended table widget.</string>\n"
               " </property>\n"
               " <property name=\"whatsThis\" >\n"
               "  <string>Extended table widget.</string>\n"
               " </property>\n"
               "</widget>\n")
               
    def includeFile(self):
        return "custom_widgets.extendedTableWidget"
