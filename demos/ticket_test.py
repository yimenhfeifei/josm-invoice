import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
import ticket_dialog_ui
import car_widget_ui

PORT = 9407
SIZEOF_UINT16 = 2

class carW(QDialog, car_widget_ui.Ui_carWidget):

    def __init__(self, parent=None):
        super(carW, self).__init__(parent)
        self.__index = 0
        self.setupUi(self)

class testForm(QDialog, ticket_dialog_ui.Ui_ticketDialog):

    def __init__(self, text, parent=None):
        super(testForm, self).__init__(parent)
        self.__text = text
        self.__index = 0
        self.setupUi(self)
        self.connect(self.materialComboBox, SIGNAL("currentIndexChanged(QString)"),
                                  self.carSelected)
        self.connect(self.commandLinkButton, SIGNAL("clicked()"), self.issueRequest)
        
        self.socket = QTcpSocket()
        self.nextBlockSize = 0
        self.request = None

        self.connect(self.socket, SIGNAL("connected()"), self.sendRequest)
        self.connect(self.socket, SIGNAL("readyRead()"), self.readResponse)

        self.setWindowTitle("Building Services")


    def closeEvent(self, event):
        self.socket.close()
        event.accept()

    def issueRequest(self):
        self.request = QByteArray()
        stream = QDataStream(self.request, QIODevice.WriteOnly)
        stream.setVersion(QDataStream.Qt_4_2)
        stream.writeUInt16(0)
        stream.writeQString("INSERT")
        stream.device().seek(0)
        stream.writeUInt16(self.request.size() - SIZEOF_UINT16)
        if self.socket.isOpen():
            self.socket.close()
        print("Connecting")
        self.socket.connectToHost("localhost", PORT)

    def sendRequest(self):
        print("Sending")
        self.nextBlockSize = 0
        self.socket.write(self.request)
        self.request = None

    def readResponse(self):
        stream = QDataStream(self.socket)
        stream.setVersion(QDataStream.Qt_4_2)

        while True:
            if self.nextBlockSize == 0:
                if self.socket.bytesAvailable() < SIZEOF_UINT16:
                    break
                self.nextBlockSize = stream.readUInt16()
            if self.socket.bytesAvailable() < self.nextBlockSize:
                break
            action = stream.readQString()
            if action == "ERROR":
                msg = "Error: {}".format(room)
            else:
                msg = action
            print(msg)
            self.nextBlockSize = 0
                     
    
    def carSelected(self, text):
        self.tabWidget.addTab(carW(), text + "1")
        print(text)
        
app = QApplication(sys.argv)
form = testForm("My text")
form.show()
app.exec_()