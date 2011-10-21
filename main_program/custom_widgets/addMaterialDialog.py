try:
    import sys
    import re
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from gui_interface_designs import add_material_dialog_generated
    from shared_modules.regular_expressions import regexObjects
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class AddMaterialDialog(QDialog,
                      add_material_dialog_generated.Ui_addMaterialDialog):

    def __init__(self, parent=None):
        super(AddMaterialDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.widgets = [self.materialEdit,
                        self.priceEdit]
        
        self.materialEdit.setValidator(regexObjects["qMaterial"])
        
        self.priceEdit.setValidator(regexObjects["qPrice"])
        
        self.materialEdit.setMaxLength(30)
        
        self.priceEdit.setMaxLength(8)
        
        self.ferrousBox.setItemData(0, "nonFerrous")
        
        self.ferrousBox.setItemData(1, "ferrous")
        
    def isValid(self):
        for widget in self.widgets:
            state = widget.validator().validate(widget.text(), 0)
            if state[0] == 0 or state[0] == 1:
                return False
        return True
