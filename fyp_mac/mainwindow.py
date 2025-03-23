from PyQt6.QtCore import QCoreApplication, QRect,QUrl, Qt
from PyQt6.QtGui import QFont, QIcon,QPixmap,QDesktopServices
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget

class mainwindow(QWidget):

    def __init__(self,stack):
        super().__init__()

        self.stack = stack

        self.background = QLabel(self)
        self.background.setGeometry(QRect(230, 120, 761, 521))
        pixmap = QPixmap("sources/main_background.png")
        scaled_pixmap = pixmap.scaled(self.background.size(), Qt.AspectRatioMode.IgnoreAspectRatio)
        self.background.setPixmap(scaled_pixmap)

        self.sign = QLabel(self)
        self.sign.setGeometry(QRect(230, 20, 521, 101))
        font = QFont()
        font.setFamilies([u"Ink Free"])
        font.setPointSize(48)
        self.sign.setFont(font)
        self.sign.setStyleSheet("color: white;")

        self.start = QPushButton(self)
        self.start.setGeometry(QRect(30, 140, 191, 81))
        font1 = QFont()
        font1.setFamilies([u"Ink Free"])
        font1.setPointSize(28)
        self.start.setFont(font1)
        self.start.setStyleSheet(
            "QPushButton {"
            "    background-color: transparent;"  
            "    border: none;"  
            "    color: white;"  
            "}"
            "QPushButton:hover {"
            "    color: blue;" 
            "}"
        )

        self.tutotial = QPushButton(self)
        self.tutotial.setGeometry(QRect(30, 250, 191, 81))
        self.tutotial.setFont(font1)
        self.tutotial.setStyleSheet(
            "QPushButton {"
            "    background-color: transparent;"  
            "    border: none;"  
            "    color: white;" 
            "}"
            "QPushButton:hover {"
            "    color: blue;"  
            "}"
        )

        self.about = QPushButton(self)
        self.about.setGeometry(QRect(30, 360, 191, 81))
        self.about.setFont(font1)
        self.about.setStyleSheet(
            "QPushButton {"
            "    background-color: transparent;"  
            "    border: none;"  
            "    color: white;"   
            "}"
            "QPushButton:hover {"
            "    color: blue;"  
            "}"
        )

        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setGeometry(QRect(30, 470, 191, 81))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(
            "QPushButton {"
            "    background-color: transparent;"  
            "    border: none;"  
            "    color: white;"  
            "}"
            "QPushButton:hover {"
            "    color: blue;"  
            "}"
        )

        self.sign.setText(QCoreApplication.translate("mainwindow", u"WORDS & BLADES", None))
        self.start.setText(QCoreApplication.translate("mainwindow", u"[Start]", None))
        self.tutotial.setText(QCoreApplication.translate("mainwindow", u"[Tutorial]", None))
        self.about.setText(QCoreApplication.translate("mainwindow", u"[About]", None))
        self.pushButton_4.setText(QCoreApplication.translate("mainwindow", u"[Beta]", None))

        self.start.clicked.connect(self.startEvent)
        self.pushButton_4.clicked.connect(self.open_survey)
        self.about.clicked.connect(self.open_about)
        self.tutotial.clicked.connect(self.open_tutorial)

    def open_tutorial(self):

        self.stack.audioManager.click_effect()
        self.stack.setCurrentIndex(4)

    def open_survey(self):
        self.stack.audioManager.click_effect()
        url = QUrl("https://www.wjx.cn/vm/eJna8IY.aspx")
        QDesktopServices.openUrl(url)

    def open_about(self):
        from about import aboutWindow
        self.stack.audioManager.click_effect()
        self.about_page = aboutWindow()
        self.about_page.show()

    def startEvent(self):
        self.stack.audioManager.click_effect()
        self.stack.gameCSS()
        self.stack.setCurrentIndex(1)
