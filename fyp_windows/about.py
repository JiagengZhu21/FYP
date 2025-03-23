from PyQt6.QtCore import QCoreApplication, QRect
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QLabel, QPushButton, QTextBrowser, QWidget


class aboutWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(549, 389)
        font = QFont()
        font.setFamilies([u"Ink Free"])
        font.setPointSize(28)
        self.setFont(font)

        self.setWindowIcon(QIcon("sources/icon.ico"))

        self.back = QPushButton(self)
        self.back.setGeometry(QRect(430, 320, 101, 51))
        font1 = QFont()
        font1.setFamilies([u"Ink Free"])
        font1.setPointSize(26)
        self.back.setFont(font1)
        self.back.setStyleSheet(
            "QPushButton {"
            "    background-color: transparent;"  
            "    border: none;"  
            "    color: white;"  
            "}"
            "QPushButton:hover {"
            "    color: blue;"  
            "}"
        )

        self.label = QLabel(self)
        self.label.setGeometry(QRect(210, 20, 121, 51))
        font2 = QFont()
        font2.setFamilies([u"Ink Free"])
        font2.setPointSize(36)
        self.label.setFont(font2)

        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setGeometry(QRect(0, 70, 551, 251))
        font3 = QFont()
        font3.setFamilies([u"Ink Free"])
        font3.setPointSize(14)
        self.textBrowser.setFont(font3)
        self.textBrowser.setStyleSheet("""
                    QTextBrowser {
                        background-color: #000918; 
                        color: white; 
                        padding: 5px; 
                        border: none;
                    }
                 """)
        self.setStyleSheet("""background-color: #000918;
                           """)

        self.setWindowTitle(QCoreApplication.translate("about", u"ABOUT", None))
        self.back.setText(QCoreApplication.translate("about", u"[Back]", None))
        self.label.setText(QCoreApplication.translate("about", u"About", None))
        with open("sources/about.txt", "r", encoding="utf-8") as file:
            text = file.read()
        self.textBrowser.setText(text)

        self.back.clicked.connect(self.close)