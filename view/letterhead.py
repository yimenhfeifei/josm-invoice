#!/bin/env python3

try:
    import traceback
    import sys
    import platform
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *    

except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)

class LetterHead(object):

    def __init__(self, painter, pageRect):
        self.painter = painter
        self.pageRect = pageRect

        self.fonts = {"companyFont": QFont("Helvetica", 16,
                                           weight=QFont.Bold),
                      "businessFont": QFont("Helvetica", 14,
                                            weight=QFont.Bold),
                      "addressFont": QFont("Helvetica", 12,
                                           weight=QFont.Bold),
                      "numberLineFont": QFont("Helvetica", 10,
                                              weight=QFont.Bold),
                      "vatFont": QFont("Helvetica", 10)}

        self.name = "John Orchard and Company"
        self.business = "Scrap Metal Merchants"
        self.address = "Chosen View, United Road, St Day, Redruth, TR16 5HT"
        self.wml = "WML: 20659"
        self.telephone = "TEL.: (01209) 820313"
        self.fax = "FAX: (01209) 822512"
        self.wcl = "WCL: CB / JM3986P2"
        self.vatReg = "VAT Registration number: 1319249 76"

        self.letterHead = [(self.name,
                            self.fonts["companyFont"]),
                           
                           (self.business,
                            self.fonts["businessFont"]),
                           
                           (self.address,
                            self.fonts["addressFont"]),
                           
                           [(self.wml,
                            self.fonts["numberLineFont"]),
                           
                           (self.telephone,
                            self.fonts["numberLineFont"]),
                           
                           (self.fax,
                            self.fonts["numberLineFont"]),
                           
                           (self.wcl,
                            self.fonts["numberLineFont"])],
                           
                           (self.vatReg,
                            self.fonts["vatFont"])]

    def paint(self, x, y):
        for num, line in enumerate(self.letterHead):
                # Handles horizontal spacing of elements on a single line.
                if isinstance(line, list):
                    length = 0
                    
                    for item in line:
                        self.painter.setFont(item[1])
                        length += self.painter.fontMetrics().width(item[0])
                    
                    availableSpace = (self.pageRect.width() - length)
                    numOfSpaces = len(line) - 1
                    
                    widthOfSpace = availableSpace / numOfSpaces
                    totalSpaceWidth = widthOfSpace * numOfSpaces
                    
                    lineLength = length + totalSpaceWidth
                    x = (self.pageRect.width() - lineLength) / 2
                    
                    for item in line:
                        self.painter.setFont(item[1])
                        self.painter.drawText(x, y, item[0])
                        x += (self.painter.fontMetrics().width(item[0]) + widthOfSpace)
                else:
                    # This prints a single element on a line.
                    self.painter.setFont(line[1])
                    x = (self.pageRect.width() - self.painter.fontMetrics().width(line[0])) / 2
                    self.painter.drawText(x, y, line[0])
                    
                y += self.painter.fontMetrics().height()

        return (x, y)

if __name__ == "__main__":
    pass
