try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4 import QtDesigner
    
    from custom_widgets.unitFrame import UnitFrame
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class UnitFramePlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(UnitFramePlugin, self).__init__(parent)

        self.initialised = False
    
    def initialize(self, core):

        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):

        return self.initialized
    
    def createWidget(self, parent):
        return UnitFrame(parent)
    
    def name(self):
        return "UnitFrame"
    
    def group(self):
        return "Custom Widgets"
    
    def toolTip(self):
        return "Custom frame."

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False
    
    def domXml(self):
        return ("<widget class='UnitFrame' name='unitFrame'>\n"
               " <property name=\"toolTip\" >\n"
               "  <string>Extended table widget.</string>\n"
               " </property>\n"
               " <property name=\"whatsThis\" >\n"
               "  <string>Extended table widget.</string>\n"
               " </property>\n"
               "</widget>\n")
               
    def includeFile(self):
        return "custom_widgets.unitFrame"
