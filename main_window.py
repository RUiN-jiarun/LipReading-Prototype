# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QEventLoop

# import Opencv module
import cv2

from ui_main_window import *

class EmittingStr(QtCore.QObject):
    # string transmit signal
    textWritten = QtCore.pyqtSignal(str) 
    def write(self, text):
      self.textWritten.emit(str(text))


class MainWindow(QWidget):
    # class constructor



    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.isRecording=False

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        # self.ui.control_bt.clicked.connect(self.test_bt)
        self.ui.control_bt.setCheckable(True)
        self.ui.control_bt.clicked[bool].connect(self.set_cont_bt)

        for i in range(3):
            self.ui.listWidget.item(i).setSizeHint(QtCore.QSize(100,34))
            listFont = QtGui.QFont()
            listFont.setBold(True)
            listFont.setPointSize(10)
            self.ui.listWidget.item(i).setFont(listFont)
            self.ui.listWidget.item(i).setText(str(i)+". None")

        # output redirect
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)


    def test_bt(self):
        print("pressed")

    def set_cont_bt(self, pressed):

        if pressed:
            self.ui.control_bt.setText("Stop")
            self.isRecording = True
        else:
            self.ui.control_bt.setText("Start")
            self.isRecording = False

    # output cmd
    def outputWritten(self, text):
        cursor = self.ui.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.textBrowser.setTextCursor(cursor)
        self.ui.textBrowser.ensureCursorVisible()


    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    def setImg(self,image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image=cv2.resize(image,(self.ui.image_label.width(),self.ui.image_label.height()),cv2.INTER_LINEAR)
        # get image infos
        height, width, channel = image.shape

        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            print('start')
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("结束录制")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            print('stop')
            # update control_bt text
            self.ui.control_bt.setText("开始录制")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())