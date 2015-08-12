import sys

from PySide import QtCore
from PySide.QtGui import QAction
from PySide.QtGui import QApplication
from PySide.QtGui import QIcon
from PySide.QtGui import QMainWindow
from PySide.QtGui import QToolBar
from PySide.QtGui import QKeySequence


class TableBrowser(QMainWindow):
    def __init__(self, parent=None):
        super(TableBrowser, self).__init__(parent)
        self.maakUi()
        # self.zetEigenschappen()

    def maakUi(self):
        self.voegActiesToe()
        self.voegToolBarToe()
        self.voegStatusBarToe()

    def voegActiesToe(self):
        self.voegActieNiewRecordToe()

    def voegActieNiewRecordToe(self):
        self.actieNieuwRecord = self.maakActie(
            QIcon('icons/Add_24x24.png'),
            "Niew <Insert>",
            self,
            QKeySequence(QtCore.Qt.Key_Insert)
        )

    def maakActie(self, icon=None, tipTekst=None, parent=None, key=None):
        action = QAction(icon, tipTekst, parent)
        action.setShortcut(key)
        action.setStatusTip(tipTekst)
        action.setToolTip(tipTekst)
        return action

    def voegToolBarToe(self):
        self.toolBar = QToolBar()
        # self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.voegRecordActiesToe()
        self.addToolBar(self.toolBar)

    def voegRecordActiesToe(self):
        self.toolBar.addAction(self.actieNieuwRecord)

    def voegStatusBarToe(self):
        self.mainStatusBar = self.statusBar()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    tableBrowser = TableBrowser()
    tableBrowser.show()

    sys.exit(app.exec_())
