import sys

from PySide.QtGui import QApplication
from PySide.QtGui import QIcon
from PySide.QtGui import QMainWindow
from PySide.QtGui import QToolBar


class TableBrowser(QMainWindow):
    def __init__(self, parent=None):
        super(TableBrowser, self).__init__(parent)
        self.maakUi()
        # self.zetEigenschappen()

    def maakUi(self):
        self.voegActiesToe()
        self.voegToolBarToe()

    def voegActiesToe(self):
        self.voegActieNiewRecordToe()

    def voegActieNiewRecordToe(self):
        self.actieNieuwRecord = maakActie(
            QIcon('icons/Add_24x24.png'),
            "Niew",
            self,
            Qt.
        )

    def voegToolBarToe(self):
        self.toolBar = QToolBar()
        self.addToolBar(self.toolBar)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    tableBrowser = TableBrowser()
    tableBrowser.show()

    sys.exit(app.exec_())
