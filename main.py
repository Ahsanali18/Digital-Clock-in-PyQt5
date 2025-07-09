# Python PyQt5 Digital Clock
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt, QUrl
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtMultimedia import QSoundEffect

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        clock_image_path = "Project#01 Digital Clock/clock_image.png"
        self.setWindowIcon(QIcon(clock_image_path))
        self.timer = QTimer(self)
        self.sound = QSoundEffect()
        self.initUI()

    # layout of digital clock
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(680,400,600,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 120px;"
                                      "color: white;")
        
        self.setStyleSheet("background-color: black")

        font_file_path = "C:/Users/Lenovo/Desktop/Python/Project#01 Digital Clock/DS-DIGIB.TTF"
        font_id = QFontDatabase.addApplicationFont(font_file_path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family,150)
        self.time_label.setFont(my_font)

        sound_file_path = "C:/Users./Lenovo./Desktop./Python./Project#01 Digital Clock/clock_sound.wav"
        self.sound.setSource(QUrl.fromLocalFile(sound_file_path))
        self.sound.setVolume(0.25)


        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
    
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
        self.sound.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
