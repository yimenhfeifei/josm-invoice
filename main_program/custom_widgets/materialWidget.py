try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import material_widget_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class MaterialWidget(QWidget, material_widget_generated.Ui_materialWidget):

    def __init__(self, parent=None):
        super(MaterialWidget, self).__init__(parent)
        self.setupUi(self)
        self.populateMaterialTable()

    def populateMaterialTable(self):
        self.materialTable.insertRow(0)
        self.materialTable.insertRow(0)
        self.materialTable.setItem(0, 0, QTableWidgetItem("Copper"))
        self.materialTable.setItem(0, 1, QTableWidgetItem("4.50"))
        
        self.materialTable.setItem(1, 0, QTableWidgetItem("Car"))
        self.materialTable.setItem(1, 1, QTableWidgetItem("1.20"))
    