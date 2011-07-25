try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4 import QtDesigner
    
    
    from custom_widgets.grossWeightLineEdit import GrossWeightLineEdit
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class GrossWeightLineEditPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent = None):
        super(GrossWeightLineEditPlugin, self).__init__(parent)

        self.initialised = False
    
    def initialize(self, core):

        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):

        return self.initialized
    
    def createWidget(self, parent):
        return GrossWeightLineEdit(parent)
    
    def name(self):
        return "GrossWeightLineEdit"
    
    def group(self):
        return "Custom Widgets"
    
    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False
    
    def domXml(self):
        return ("<widget class='GrossWeightLineEdit' name='grossWeightLineEdit'>\n"
               " <property name=\"toolTip\" >\n"
               "  <string>Enter gross weight.</string>\n"
               " </property>\n"
               " <property name=\"whatsThis\" >\n"
               "  <string>Validating line edit for vehicle gross weight.</string>\n"
               " </property>\n"
               "</widget>\n")
               
    def includeFile(self):
        return "custom_widgets.grossWeightLineEdit"