import unittest

from PySide.QtGui import QAction
from PySide.QtGui import QApplication
from PySide.QtGui import QToolBar

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
