try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import material_widget_generated
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class MaterialWidget(QWidget, material_widget_generated.Ui_materialWidget):
    
    widgetChanged = pyqtSignal()

    def __init__(self, parent=None):
        super(MaterialWidget, self).__init__(parent)
        self.setupUi(self)
        self.vehicleWidgets = [self.makeEdit,
                               self.modelEdit,
                               self.vehicleRegistrationEdit,
                               self.vinEdit]
        
        for widget in self.vehicleWidgets:
            self.connect(widget, SIGNAL("textChanged(QString)"),
                         self.changed)
        
        self.vehicles = []
        self.populateMaterialTable()
        
        self.connect(self.materialTable, SIGNAL("itemSelectionChanged()"),
                     self.changed)
        
    def changed(self):
        row = self.materialTable.currentRow()
        if self.materialTable.item(row, 0).text() in self.vehicles:
            print("vehicle selected")
            self.vehicleBox.setEnabled(True)
            for widget in self.vehicleWidgets:
                widget.validate()
        else:
            self.vehicleBox.setEnabled(False)
            for widget in self.vehicleWidgets:
                widget.clear()

        self.widgetChanged.emit()
        
    def getPricePerUnit(self):
        row = self.materialTable.currentRow()
        if row >= self.materialTable.rowCount() or row < 0:
            return "0"
        else:
            return self.materialTable.item(row, 1).text()
        
    def getMaterial(self):
        row = self.materialTable.currentRow()
        return self.materialTable.item(row, 0).text()

    def populateMaterialTable(self):
        self.vehicles = ["Car"]
        self.materialTable.insertRow(0)
        self.materialTable.insertRow(0)
        self.materialTable.setItem(0, 0, QTableWidgetItem("Copper"))
        self.materialTable.setItem(0, 1, QTableWidgetItem("4.50"))
        
        self.materialTable.setItem(1, 0, QTableWidgetItem("Car"))
        self.materialTable.setItem(1, 1, QTableWidgetItem("1.20"))
    
    def vehicleSelected(self):
        return self.vehicleBox.isEnabled()
        
    def isValid(self):
        if self.vehicleBox.isEnabled():
            for widget in self.vehicleWidgets:
                if not widget.isValid():
                    return False
        return True