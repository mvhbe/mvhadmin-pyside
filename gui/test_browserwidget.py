import unittest
from PySide import QtGui
from browserwidget import  BrowserWidget


class TestBrowserWidget(unittest.TestCase):

    """Highlevel unittest van de browser widget"""

    app = QtGui.QApplication([])

    def setUp(self):
        self.widget = BrowserWidget()

    def tearDown(self):
        del self.widget
        self.widget = None

    def testHeeftToolBar(self):
        """Heeft een attribuut toolBar van het type QToolbar"""
        toolBarAanwezig = hasattr(self.widget, "toolBar")
        self.assertTrue(toolBarAanwezig)
        self.assertIsInstance(
            self.widget.toolBar, QtGui.QToolBar, "niet van het type 'QToolbar' !"
        )

    def testHeeftActieNiewRecord(self):
        """Heeft een actie 'NieuwRecord'"""
        actieAanwezig = hasattr(self.widget, "nieuwRecordAction")
        self.assertTrue(actieAanwezig)
        self.assertIsInstance(
            self.widget.nieuwRecordAction, QtGui.QAction, "niet van het type 'QAction' !"
        )

        # self.fail("Nog te implementeren !")

if __name__ == '__main__':
    unittest.main()
