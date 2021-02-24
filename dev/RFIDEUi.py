import sys
import os

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ';' + os.environ['PATH']

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Editor import *

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('myappid')

class RFIDEUi(QMainWindow):

    def __init__(self):
        super(RFIDEUi, self).__init__()
        self.initMainUi()

    def initMainUi(self):
        self.tab_widget = QTabWidget()

        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.closeTab)

        self.resize(400,400)
        #self.showMaximized()


        self.new_tab1 = Editor(self)
        self.tab_widget.addTab(self.new_tab1,'test')

        self.toolbar = self.addToolBar('New')
        newAction = QAction('新增', self)
        newAction.triggered.connect(self.setValue)
        self.toolbar.addAction(newAction)

        self.setCentralWidget(self.tab_widget)

    def closeTab(self):
        i = self.tab_widget.currentIndex()
        self.tab_widget.removeTab(i)

    def setValue(self):
        self.new_tab1.get_value()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    rfide = RFIDEUi()
    rfide.show()
    sys.exit(app.exec_())
