from vidstream import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import socket
import threading
import sys


# IP my device is 192.168.1.3
# GUI
class Chat_GUI(QMainWindow):
    def __init__(self):
        super(Chat_GUI, self).__init__()
        uic.loadUi("chatgui.ui", self)
        self.show()

        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.connect(ip_address, port)

        self.btnConnect.clicked.connect(self.get_Connect)
        self.btnVoice.clicked.connect(self.get_Voice)
        self.btnCamera.clicked.connect(self.get_Camera)
        self.btnScreen.clicked.connect(self.get_Screen)
        self.btnSend.clicked.connect(self.send_Message)
        self.btnExit.clicked.connect(self.exit)

    def get_Connect(self):
        if str(self.txtIP.text()) == "":
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Thông báo")
            msg_box.setText("Vui lòng nhập IP Address!")
            msg_box.exec()

        elif str(self.txtPort.text()) == "":
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Thông báo")
            msg_box.setText("Vui lòng nhập Port!")
            msg_box.exec()

        elif str(self.txtUsername.text()) == "":
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Thông báo")
            msg_box.setText("Vui lòng nhập tên!")
            msg_box.exec()

        else:
            dialog = QMessageBox()
            dialog.setText(
                f"Bạn thật sự muốn kết nối?")
            dialog.setWindowTitle("Thông báo")
            dialog.addButton(QPushButton("Có"), QMessageBox.YesRole)  # value 0
            dialog.addButton(QPushButton("Không"), QMessageBox.NoRole)  # value 1

            if dialog.exec() == 0:
                try:
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Thông báo")
                    msg_box.setText("Kết nối thành công!!!")
                    msg_box.exec()

                    self.btnVoice.setEnabled(True)
                    self.btnCamera.setEnabled(True)
                    self.btnScreen.setEnabled(True)
                    self.txtDisplay.setEnabled(True)
                    self.lneMessage.setEnabled(True)
                    self.btnSend.setEnabled(True)

                    self.txtIP.setEnabled(False)
                    self.txtPort.setEnabled(False)
                    self.btnConnect.setEnabled(False)
                    self.txtUsername.setEnabled(False)
                except:
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Thông báo")
                    msg_box.setText("Kết nối không thành công! Vui lòng thử lại!")
                    msg_box.exec()

    @staticmethod
    def get_Voice():
        try:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Thông báo")
            msg_box.setText("Đang kết nối đến Voice. Vui lòng chờ...")
            msg_box.exec()
        except:
            pass

    @staticmethod
    def get_Camera():
        try:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Thông báo")
            msg_box.setText("Đang kết nối đến Camera. Vui lòng chờ...")
            msg_box.exec()
        except:
            pass

    @staticmethod
    def get_Screen():
        try:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Thông báo")
            msg_box.setText("Đang kết nối đến Màn hình. Vui lòng chờ...")
            msg_box.exec()
        except:
            pass

    @staticmethod
    def send_Message():
        try:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Thông báo")
            msg_box.setText("Gửi thành công!")
            msg_box.exec()
        except:
            pass

    @staticmethod
    def exit():
        dialog = QMessageBox()
        dialog.setText(f"Bạn thật sự muốn thoát?")
        dialog.setWindowTitle("Thông báo")
        dialog.addButton(QPushButton("Có"), QMessageBox.YesRole)  # value 0
        dialog.addButton(QPushButton("Không"), QMessageBox.NoRole)  # value 1
        if dialog.exec() == 0:
            QApplication.exit()

    def closeEvent(self, event):
        close = QMessageBox.question(self, "QUIT", "Bạn có thật sự muốn thoát?", QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# Run GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Chat_GUI()
    window.show()
    sys.exit(app.exec_())
