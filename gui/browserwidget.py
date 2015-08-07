from PySide import QtCore
from PySide.QtGui import QAction
from PySide.QtGui import QApplication
from PySide.QtGui import QHBoxLayout
from PySide.QtGui import QIcon
from PySide.QtGui import QToolBar
from PySide.QtGui import QWidget


class BrowserWidget(QWidget):

    def __init__(self, parent=None):
        super(BrowserWidget, self).__init__(parent)
        self.maakUi()
        self.zetEigenschappen()

    def maakUi(self):
        self.maakVertikaleLayout()
        self.maakToolBar()

    def maakVertikaleLayout(self):
        self.layout = QHBoxLayout(self)

    def maakToolBar(self):
        self.toolBar = QToolBar()
        self.toolBar.setToolButtonStyle = QtCore.Qt.ToolButtonTextBesideIcon
        self.maakNieuwRecordAction()
        self.toolBar.addAction(self.nieuwRecordAction)
        self.layout.addWidget(self.toolBar)

    def maakNieuwRecordAction(self):
        self.nieuwRecordAction = QAction(
            "Nieuw", self.toolBar
        )
        self.nieuwRecordAction.setIcon(QIcon("icons/New_24x24.png"))
        self.nieuwRecordAction.setIconText("Nieuw")

    def zetEigenschappen(self):
        # self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 600, 600)
        # self.setCentralWidget(self.tableView)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    browserWidget = BrowserWidget()
    browserWidget.show()

    sys.exit(app.exec_())
