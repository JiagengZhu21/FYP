from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1021, 662)
        self.picture = QLabel(Form)
        self.picture.setObjectName(u"picture")
        self.picture.setGeometry(QRect(0, 0, 1021, 662))
        self.next = QPushButton(Form)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(850, 30, 141, 61))
        font = QFont()
        font.setFamilies([u"Ink Free"])
        font.setPointSize(36)
        self.next.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.picture.setText("")
        self.next.setText(QCoreApplication.translate("Form", u"NEXT", None))
    # retranslateUi

class tutorial(QWidget, Ui_Form):

    def __init__(self,stack):
        super().__init__()
        self.setupUi(self)
        self.pictureIndex = 0
        self.pictureNum = 3
        self.stack = stack
        self.next.clicked.connect(self.nextEvent)

        pixmap = QPixmap(f"sources/tutorial/tutorial_{str(0)}.png")
        scaled_pixmap = pixmap.scaled(self.picture.size(), Qt.AspectRatioMode.IgnoreAspectRatio)
        self.picture.setPixmap(scaled_pixmap)

    def nextEvent(self):
        self.stack.audioManager.click_effect()

        self.pictureIndex += 1
        pixmap = QPixmap(f"sources/tutorial/tutorial_{str(self.pictureIndex)}.png")
        scaled_pixmap = pixmap.scaled(self.picture.size(), Qt.AspectRatioMode.IgnoreAspectRatio)
        self.picture.setPixmap(scaled_pixmap)

        if self.pictureIndex==self.pictureNum-1:
            self.next.setText("Back")
        if self.pictureIndex == self.pictureNum:
            self.reStart()

    def reStart(self):
        self.next.setText("NEXT")
        pixmap = QPixmap(f"sources/tutorial/tutorial_{str(0)}.png")
        scaled_pixmap = pixmap.scaled(self.picture.size(), Qt.AspectRatioMode.IgnoreAspectRatio)
        self.picture.setPixmap(scaled_pixmap)
        self.pictureIndex = 0
        self.stack.setCurrentIndex(0)
