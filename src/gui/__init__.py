# src/gui/__init__.py

from .main_screen import MainWindow

def run_gui():
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
