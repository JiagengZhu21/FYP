import sys
from PyQt6.QtWidgets import QApplication
from manager import AppManager

app = QApplication(sys.argv)
window = AppManager()
window.show()
sys.exit(app.exec())
