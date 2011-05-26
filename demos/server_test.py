#!/usr/bin/env python3
import bisect
import collections
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

PORT = 9407
SIZEOF_UINT16 = 2
MAX_BOOKINGS_PER_DAY = 5

class Socket(QTcpSocket):

    def __init__(self, parent=None):
        super(Socket, self).__init__(parent)
        self.connect(self, SIGNAL("readyRead()"), self.readRequest)
        self.connect(self, SIGNAL("disconnected()"), self.deleteLater)
        self.nextBlockSize = 0

    def readRequest(self):
        stream = QDataStream(self)
        stream.setVersion(QDataStream.Qt_4_2)

        if self.nextBlockSize == 0:
            if self.bytesAvailable() < SIZEOF_UINT16:
                return
            self.nextBlockSize = stream.readUInt16()
        if self.bytesAvailable() < self.nextBlockSize:
            return

        action = stream.readQString()
        if action in ("INSERT", "OPEN"):
            self.sendReply("INSERT_SUCCESS")
        else:
            self.sendError("INVALID_ACTION")

    def sendError(self, msg):
        reply = QByteArray()
        stream = QDataStream(reply, QIODevice.WriteOnly)
        stream.setVersion(QDataStream.Qt_4_2)
        stream.writeUInt16(0)
        stream.writeQString("ERROR")
        stream.writeQString(msg)
        stream.device().seek(0)
        stream.writeUInt16(reply.size() - SIZEOF_UINT16)
        self.write(reply)

    def sendReply(self, action):
        reply = QByteArray()
        stream = QDataStream(reply, QIODevice.WriteOnly)
        stream.setVersion(QDataStream.Qt_4_2)
        stream.writeUInt16(0)
        stream.writeQString(action)
        stream.device().seek(0)
        stream.writeUInt16(reply.size() - SIZEOF_UINT16)
        self.write(reply)

class TcpServer(QTcpServer):

    def __init__(self, parent=None):
        super(TcpServer, self).__init__(parent)


    def incomingConnection(self, socketId):
        socket = Socket(self)
        socket.setSocketDescriptor(socketId)
        
class BuildingServicesDlg(QPushButton):

    def __init__(self, parent=None):
        super(BuildingServicesDlg, self).__init__(
                "&Close Server", parent)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.tcpServer = TcpServer(self)
        if not self.tcpServer.listen(QHostAddress("0.0.0.0"), PORT):
            QMessageBox.critical(self, "Building Services Server",
                    "Failed to start server: {}".format(
                    self.tcpServer.errorString()))
            self.close()
            return

        self.connect(self, SIGNAL("clicked()"), self.close)
        font = self.font()
        font.setPointSize(24)
        self.setFont(font)
        self.setWindowTitle("Building Services Server")


app = QApplication(sys.argv)
form = BuildingServicesDlg()
form.show()
form.move(0, 0)
app.exec_()