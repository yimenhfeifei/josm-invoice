try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class WidgetPrinter(QPrinter):
    def __init__(self, widget, resolution, flag):
        super(WidgetPrinter, self).__init__(flag)
        self.widget = widget
        self.setResolution(resolution)
        self.printDialog = QPrintDialog(self)
        
        #self.setGeometry(printer.pageRect())
        #self.render(printer)
        #try qimage etc.
       
    def showPrintDialog(self):
        if self.printDialog.exec_():
            self.printWidget()
        else:
            return
        
    def printWidget(self):
        image = QPixmap.grabWidget(self.widget, self.widget.rect())
        #window = window.toImage()
        image = image.scaled(self.pageRect().width(),
                             self.pageRect().height(),
                             Qt.KeepAspectRatio)
        
        painter = QPainter()
        painter.begin(self)
        painter.drawPixmap(0, 0, image)
        painter.end()
        