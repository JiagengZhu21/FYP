import time
from PyQt6.QtCore import QRect, Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QPixmap, QTextCursor
from PyQt6.QtWidgets import QLabel, QPushButton, QTextBrowser, QTextEdit, QWidget, QApplication

import language

class chating(QThread):
    response_signal = pyqtSignal(tuple)
    def __init__(self, user_text):
        super().__init__()
        self.user_text = user_text

    def run(self):
        reply = language.chat_with_model(self.user_text)
        self.response_signal.emit(reply)

class gamewindow(QWidget):

    def __init__(self,stack):
        super().__init__()

        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setGeometry(QRect(120, 10, 781, 451))
        self.textBrowser.setStyleSheet("""
                      QTextBrowser {
                          background-color: #242827;
                      }
                   """)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QRect(190, 470, 641, 171))

        self.side1 = QLabel(self)
        self.side1.setGeometry(QRect(0, 10, 121, 451))
        p1 = QPixmap("sources/side1.jpg")
        pixmap1 = p1.scaled(self.side1.size(), Qt.AspectRatioMode.IgnoreAspectRatio)
        self.side1.setPixmap(pixmap1)

        self.side2 = QLabel(self)
        self.side2.setGeometry(QRect(900, 10, 121, 451))
        p2 = QPixmap("sources/side2.jpg")
        pixmap2 = p2.scaled(self.side2.size(), Qt.AspectRatioMode.IgnoreAspectRatio)
        self.side2.setPixmap(pixmap2)

        self.round = QLabel(self)
        self.round.setGeometry(QRect(10, 470, 171, 31))
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(18)
        self.round.setFont(font1)
        self.round.setText("Rounds Remain")

        self.number = QLabel(self)
        self.number.setGeometry(QRect(60, 510, 81, 101))
        font2 = QFont()
        font2.setFamilies([u"MV Boli"])
        font2.setPointSize(36)
        self.number.setFont(font2)
        self.number.setWordWrap(False)
        self.number.setMargin(0)

        self.label = QLabel(self)
        self.label.setGeometry(QRect(850, 470, 61, 61))
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(950, 470, 61, 61))
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(850, 560, 61, 61))
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QRect(950, 560, 61, 61))

        self.send = QPushButton(self)
        self.send.setGeometry(QRect(770, 580, 51, 51))
        self.send.setStyleSheet("""
                      QPushButton {
                          border: none;
                          border-radius: 25px;
                          background-color: #FF5733; 
                          color: white;
                      }
                      QPushButton:hover {
                          background-color: #95a5a6;  
                     } 
                  """)
        self.send.setText("send")

        font = QFont()
        font.setFamilies([u"Ink Free"])
        font.setPointSize(20)
        self.back = QPushButton(self)
        self.back.setGeometry(QRect(10, 10, 101, 41))
        self.back.setText("Back")
        self.back.setFont(font)

        fonta = QFont()
        fonta.setFamilies(["MV Boli"])
        fonta.setPointSize(12)
        self.textBrowser.setFont(fonta)
        self.textEdit.setFont(fonta)

        self.stack = stack

        self.nums_words = 0
        self.nums_rounds = 10
        self.labels = [self.label,self.label_2,self.label_3,self.label_4]
        self.number.setText(str(self.nums_rounds))

        self.printStart()

        self.send.clicked.connect(self.sendEvent)
        self.back.clicked.connect(self.backEvent)

    def printStart(self):

        with open("sources/open.txt", "r", encoding="utf-8") as file:
            text = file.read()
        self.textBrowser.setText(text)

    def nextState(self):

        if self.nums_rounds==0 and self.nums_words<4:
            self.reStart()
            self.close()
            self.stack.outcomeCSS()
            self.stack.setCurrentIndex(3)
            return
        if self.nums_words == 4:
            self.reStart()
            self.close()
            self.stack.outcomeCSS()
            self.stack.setCurrentIndex(2)
            return
        self.nums_rounds -= 1
        self.number.setText(str(self.nums_rounds))

    def reStart(self):
        language.reStart()
        self.textEdit.show()
        self.textBrowser.clear()
        for label in self.labels:
            label.clear()
        self.nums_words = 0
        self.nums_rounds = 15
        self.send.setText("send")
        self.number.setText(str(self.nums_rounds))
        self.send.setEnabled(True)
        self.printStart()

    def printLabel(self,name):

        pixmap = QPixmap(f"sources/words/{name}.png")
        scaled_pixmap = pixmap.scaled(self.labels[self.nums_words].size(), Qt.AspectRatioMode.IgnoreAspectRatio)
        self.labels[self.nums_words].setPixmap(scaled_pixmap)
        self.nums_words += 1
        if self.nums_words == 4:
            self.textEdit.hide()
            self.send.setText("WIN")

    def sendMessage(self):

        user_text = self.textEdit.toPlainText()
        if not user_text:
            self.send.setEnabled(True)
            return
        self.textBrowser.append(f"You: {user_text}\n")
        self.textEdit.clear()
        self.textBrowser.append("King: ")

        QApplication.processEvents()

        self.chat_thread = chating(user_text)
        self.chat_thread.response_signal.connect(self.dealResponse)
        self.chat_thread.start()


    def dealResponse(self,reply):

        self.chat_thread.exit()
        reply_text = reply[0]
        outcome = reply[1]
        word = reply[2]
        positive = reply[3]
        self.respond_text = reply_text
        self.printResponse(reply_text)
        if positive == False or positive=="false":
            self.nextState()
            if self.nums_rounds == 0 and self.nums_words < 4:
                self.textEdit.hide()
                self.send.setText("LOSE")
        if outcome:
            self.printLabel(word)

    def printResponse(self,text):

        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)

        for char in text:
            cursor.insertText(char)
            self.textBrowser.setTextCursor(cursor)
            QApplication.processEvents()
            time.sleep(0.01)

        self.textBrowser.append("")
        self.send.setEnabled(True)

    def sendEvent(self):
        self.send.setEnabled(False)
        self.stack.audioManager.click_effect()
        self.nextState()
        self.sendMessage()

        if self.nums_rounds==0 and self.nums_words<4:
            self.textEdit.hide()
            self.send.setText("LOSE")

    def backEvent(self):
        self.reStart()
        self.stack.audioManager.click_effect()
        self.stack.mainCSS()
        self.stack.setCurrentIndex(0)
