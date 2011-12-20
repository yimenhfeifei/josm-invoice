#!/usr/bin/python3
try:
    import traceback
    import sys

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)


class PrintPreviewDialogExtended(QDialog):

    def __init__(self, printer, paintCallback, parent=None):
        super(PrintPreviewDialogExtended, self).__init__(parent)

        self.mainLayout = QVBoxLayout()

        self.toolBar = QToolBar(self)

        self.mainLayout.addWidget(self.toolBar)

        self.resize(parent.width(), parent.height())

        self.printer = printer

        self.currentPageEditLength = 50

        self.previewWidget = QPrintPreviewWidget(self.printer, self)

        self.previewWidget.fitToWidth()

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/fit-width-32.png"),
                           "Fit page to width",
                           self.previewWidget.fitToWidth,
                           QKeySequence())

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/fit-page-32.png"),
                           "Fit page to view",
                           self.previewWidget.fitInView,
                           QKeySequence())

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/zoom-in-32.png"),
                           "Zoom in",
                           self.previewWidget.zoomIn,
                           QKeySequence())

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/zoom-out-32.png"),
                           "Zoom out",
                           self.previewWidget.zoomOut,
                           QKeySequence())

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/layout-portrait-32.png"),
                           "Set portrait layout",
                           self.previewWidget.setPortraitOrientation,
                           QKeySequence())

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/layout-landscape-32.png"),
                           "Set landscape layout",
                           self.previewWidget.setLandscapeOrientation,
                           QKeySequence())

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/go-first-32.png"),
                           "Go to first page",
                           self.goFirst,
                           QKeySequence.MoveToStartOfLine)

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/go-previous-32.png"),
                           "Go to previous page",
                           self.goPrevious,
                           QKeySequence.MoveToPreviousPage)

        self.addCurrentPage(self.currentPageEditLength)

        self.addPageCount()

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/go-next-32.png"),
                           "Go to next page",
                           self.goNext,
                           QKeySequence.MoveToNextPage)

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/go-last-32.png"),
                           "Go to last page",
                           self.goLast,
                           QKeySequence.MoveToEndOfLine)

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/view-page-one-32.png"),
                           "View single page",
                           lambda v=QPrintPreviewWidget.SinglePageView: self.previewWidget.setViewMode(v),
                           QKeySequence())

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/view-page-multi-32.png"),
                           "View multiple pages",
                           lambda v=QPrintPreviewWidget.AllPagesView: self.previewWidget.setViewMode(v),
                           QKeySequence())

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/page-setup-32.png"),
                           "Go to page setup",
                           self.pageSetup,
                           QKeySequence())

        self.addToolButton(QIcon(":/trolltech/dialogs/qprintpreviewdialog/images/print-32.png"),
                           "Print",
                           self.printDialog,
                           QKeySequence.Print)

        self.mainLayout.addWidget(self.previewWidget)

        self.setLayout(self.mainLayout)

        self.connect(self.previewWidget, SIGNAL("paintRequested(QPrinter*)"),
                     paintCallback)

        self.connect(self.previewWidget, SIGNAL("previewChanged()"),
                     self.updatePageCount)

    def goFirst(self):
        self.previewWidget.setCurrentPage(1)
        self.updateCurrentPage()

    def goPrevious(self):
        currentPage = self.previewWidget.currentPage()
        if currentPage > 1:
            self.previewWidget.setCurrentPage(currentPage - 1)
            self.updateCurrentPage()

    def goNext(self):
        currentPage = self.previewWidget.currentPage()
        if currentPage < self.previewWidget.pageCount():
            self.previewWidget.setCurrentPage(currentPage + 1)
            self.updateCurrentPage()

    def goLast(self):
        self.previewWidget.setCurrentPage(self.previewWidget.pageCount())
        self.updateCurrentPage()

    def pageSetup(self):
        dialog = QPageSetupDialog(self.printer, self)
        dialog.exec_()
        self.previewWidget.updatePreview()

    def printDialog(self):
        dialog = QPrintDialog(self.printer, self)

        self.connect(dialog, SIGNAL("accepted()"),
                     self.previewWidget.print)

        if dialog.exec_():
            self.accept()

    def addCurrentPage(self, maxWidth):
        self.currentPageEdit = QLineEdit()
        self.currentPageEdit.setMaximumWidth(maxWidth)
        self.currentPageEdit.setAlignment(Qt.AlignHCenter)
        self.currentPageEdit.setToolTip("Current page")

        self.connect(self.currentPageEdit, SIGNAL("textEdited(QString)"),
                     self.onCurrentPageEdited)

        self.updateCurrentPage()
        self.toolBar.addWidget(self.currentPageEdit)

    def onCurrentPageEdited(self, text):
        try:
            self.previewWidget.setCurrentPage(int(text))
        except ValueError:
            pass

    def addPageCount(self):
        self.pageCount = QLabel()
        self.pageCount.setToolTip("Total pages")
        self.updatePageCount()
        self.toolBar.addWidget(self.pageCount)

    def updatePageCount(self):
        self.pageCount.setText(" / {}".format(self.previewWidget.pageCount()))

    def updateCurrentPage(self):
        self.currentPageEdit.setText(str(self.previewWidget.currentPage()))

    def addToolButton(self, icon, tooltip, slot, shortcut):
        action = QAction(icon,
                         "",
                         self)

        action.setToolTip(tooltip)

        self.connect(action, SIGNAL("triggered()"),
                     slot)

        action.setShortcut(shortcut)

        self.toolBar.addAction(action)
