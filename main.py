import sys

from PySide6.QtWidgets import QApplication

from mainwindow import MainWindow


def main() -> None:
    """
    Main entry point for programm
    """
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
