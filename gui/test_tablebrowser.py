import unittest

from PySide.QtGui import QAction
from PySide.QtGui import QApplication
from PySide.QtGui import QToolBar
from PySide.QtGui import QStatusBar

from tablebrowser import  TableBrowser


class TestTableBrowser(unittest.TestCase):

    """Highlevel unittest van de table browser"""

    app = QApplication([])

    def setUp(self):
        self.browser = TableBrowser()

    def tearDown(self):
        del self.browser
        self.browser = None

    def testHeeftToolBar(self):
        """Heeft een attribuut toolBar van het type QToolBar"""
        toolBarAanwezig = hasattr(self.browser, "toolBar")
        self.assertTrue(toolBarAanwezig)
        self.assertIsInstance(
            self.browser.toolBar, QToolBar, "niet van het type 'QToolBar' !"
        )

    def testHeeftStatusBar(self):
        """Heeft een attribuut mainStatusBar van het type QStatusBar"""
        statusBarAanwezig = hasattr(self.browser, "mainStatusBar")
        self.assertTrue(statusBarAanwezig)
        self.assertIsInstance(
            self.browser.mainStatusBar, QStatusBar, "niet van het type 'QStatusBar' !"
        )

    def testHeeftActieNiewRecord(self):
        """Heeft een actie 'actieNieuwRecord'"""
        actieAanwezig = hasattr(self.browser, "actieNieuwRecord")
        self.assertTrue(actieAanwezig)
        self.assertIsInstance(
            self.browser.actieNieuwRecord, QAction, "niet van het type 'QAction' !"
        )

        # self.fail("Nog te implementeren !")

if __name__ == '__main__':
    unittest.main()
