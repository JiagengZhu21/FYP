from PyQt6.QtWidgets import QApplication, QStackedWidget
from mainwindow import mainwindow
from game import gamewindow
from decision import win, lose
from PyQt6.QtGui import QIcon
from tutorial import tutorial
from audio import AudioManager

class AppManager(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.audioManager = AudioManager()

        self.game_window = gamewindow(self)
        self.main_window = mainwindow(self)
        self.win_window = win(self)
        self.lose_window = lose(self)
        self.tutorial = tutorial(self)

        self.mainCSS()
        self.addWidget(self.main_window)
        self.addWidget(self.game_window)
        self.addWidget(self.win_window)
        self.addWidget(self.lose_window)
        self.addWidget(self.tutorial)

        self.setWindowTitle("WORDS & BLADES")
        self.setCurrentIndex(0)

    def mainCSS(self):
        self.audioManager.play_bgm("sources/audio/menu.mp3")
        self.setFixedSize(991, 641)
        self.setStyleSheet("""
                           background-color: #000918;
                           """)
        self.setWindowIcon(QIcon("sources/icon.icns"))
    def gameCSS(self):
        self.audioManager.play_bgm("sources/audio/game.mp3")
        self.setFixedSize(1021, 662)
        self.setStyleSheet("""
                           background-color: #2B312F;
                           """)
    def outcomeCSS(self):

        self.setFixedSize(400, 300)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AppManager()
    window.show()
    sys.exit(app.exec())