from PyQt6.QtCore import QCoreApplication, QMetaObject, QRect
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QPushButton, QWidget

class Ui_Win(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setFixedSize(400, 300)
        self.win = QLabel(Form)
        self.win.setObjectName(u"win")
        self.win.setGeometry(QRect(80, 60, 281, 91))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(36)
        font.setBold(True)
        self.win.setFont(font)
        self.restart = QPushButton(Form)
        self.restart.setObjectName(u"restart")
        self.restart.setGeometry(QRect(50, 220, 91, 31))
        self.home = QPushButton(Form)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(260, 220, 91, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.win.setText(QCoreApplication.translate("Form", u"VICTORY!", None))
        self.restart.setText(QCoreApplication.translate("Form", u"Restart", None))
        self.home.setText(QCoreApplication.translate("Form", u"Home", None))
    # retranslateUi


class Ui_Lost(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setFixedSize(400, 300)
        self.lose = QLabel(Form)
        self.lose.setObjectName(u"win")
        self.lose.setGeometry(QRect(100, 70, 211, 91))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(36)
        font.setBold(True)
        self.lose.setFont(font)

        self.restart = QPushButton(Form)
        self.restart.setObjectName(u"restart")
        self.restart.setGeometry(QRect(50, 220, 91, 31))
        self.home = QPushButton(Form)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(260, 220, 91, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lose.setText(QCoreApplication.translate("Form", u"DEFEAT!", None))
        self.restart.setText(QCoreApplication.translate("Form", u"Restart", None))
        self.home.setText(QCoreApplication.translate("Form", u"Home", None))
    # retranslateUi

class win(QWidget, Ui_Win):

    def __init__(self,stack):
        super().__init__()
        self.setupUi(self)
        self.stack = stack
        self.home.clicked.connect(self.toHome)
        self.restart.clicked.connect(self.toGame)

    def toHome(self):
        self.stack.audioManager.click_effect()
        self.close()
        self.stack.mainCSS()
        self.stack.setCurrentIndex(0)

    def toGame(self):
        self.stack.audioManager.click_effect()
        self.close()
        self.stack.gameCSS()
        self.stack.setCurrentIndex(1)

class lose(QWidget, Ui_Lost):

    def __init__(self,stack):
        super().__init__()
        self.setupUi(self)
        self.stack = stack
        self.home.clicked.connect(self.toHome)
        self.restart.clicked.connect(self.toGame)

    def toHome(self):
        self.stack.audioManager.click_effect()
        self.close()
        self.stack.mainCSS()
        self.stack.setCurrentIndex(0)

    def toGame(self):
        self.stack.audioManager.click_effect()
        self.close()
        self.stack.gameCSS()
        self.stack.setCurrentIndex(1)
