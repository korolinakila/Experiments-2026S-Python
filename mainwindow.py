from PySide6.QtWidgets import QMainWindow, QWidget

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    """
    This is the GUI as a whole, which is displayed at startup.

    Designed using .ui file:
    1. Create class.ui file
    2. Convert class.ui file to ui_class.py file using commandline:
    > pyside6-uic class.ui -o ui_class.py
    3. Define a Class in python
    4. Create Ui_Class in Class.__init__()
    5. Afterwards, call setupUi

    If in doubt, create C++ Designer Form Class and look its structure!
    """

    def __init__(self, parent: QWidget = None) -> None:
        """
        parent: when parent is closed, this widget is also closed
        """
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
