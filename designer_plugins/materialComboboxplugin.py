try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4 import QtDesigner
    
    from custom_widgets.materialCombobox import MaterialCombobox
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class MaterialComboboxPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(MaterialComboboxPlugin, self).__init__(parent)

        self.initialised = False
    
    def initialize(self, core):

        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):

        return self.initialized
    
    def createWidget(self, parent):
        return MaterialCombobox(parent)
    
    def name(self):
        return "MaterialCombobox"
    
    def group(self):
        return "Custom Widgets"
    
    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""
    
    def isContainer(self):
        return False
    
    def domXml(self):
        return ("<widget class='MaterialCombobox' name='materialCombobox'>\n"
               " <property name=\"toolTip\" >\n"
               "  <string>Custom Line Edit</string>\n"
               " </property>\n"
               " <property name=\"whatsThis\" >\n"
               "  <string>The analog clock widget displays "
               "the current time.</string>\n"
               " </property>\n"
               "</widget>\n")
               
    def includeFile(self):
        return "custom_widgets.materialCombobox"