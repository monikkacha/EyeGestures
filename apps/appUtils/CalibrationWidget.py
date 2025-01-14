import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide2.QtCore import Qt, QTimer, QRect
from PySide2.QtGui import QTransform
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore
from screeninfo import get_monitors

class WarningPill(QWidget):
    def __init__(self, position, text, angle = 0):
        super(WarningPill, self).__init__()

        width = 200
        height= 200

        # Set up the window attributes
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        self.setGeometry(position[0], position[1], width, height)
        self.setStyleSheet("background-color: #99ffff00; border-radius: 100;")

        # Add a label for displaying text
        self.angle = angle
        self.text = text
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 0, width, height)

    def disappear(self):
        self.hide()

    def close_event(self):
        self.close()

    def show_again(self):
        self.setStyleSheet("background-color: #99ffff00; border-radius: 100;")


class CalibrationWidget():
    def __init__(self):
        self.dict = {"left": 2, "right": 3, "top" : 0 , "bottom" : 1}

        self.monitor = list(filter(lambda monitor: monitor.is_primary == True ,get_monitors()))[0]

        # Create warning pills on each edge and add them to the layout
        self.warning_pills = [
            WarningPill((self.monitor.x + self.monitor.width/2 - 100,
                         self.monitor.y + 0), "LOOK HERE", 0),
            WarningPill((self.monitor.x + self.monitor.width/2 - 100,
                         self.monitor.y + self.monitor.height - 200), "LOOK HERE", 0),
            WarningPill((self.monitor.x + 0,
                         self.monitor.y + self.monitor.height/2 - 100), "LOOK HERE", 0),
            WarningPill((self.monitor.x + self.monitor.width - 200,
                         self.monitor.y + self.monitor.height/2 -100 ), "LOOK HERE", 0)
        ]

        for pill in self.warning_pills:
            pill.show()

    def close_event(self):
        for pill in self.warning_pills:
            pill.close_event()

    def disappear_pill(self,pill):
        self.warning_pills[
            self.dict[pill]].disappear()

    def disappear(self):
        for pill in self.warning_pills:
            pill.disappear()

    def show_pill(self,pill):
        self.warning_pills[
            self.dict[pill]].show()

    def show_again(self):
        for pill in self.warning_pills:
            pill.show_again()
