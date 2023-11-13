import threading
import socket
from random import randint
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

ip_address = '10.60.10.86'  # localhost
# ip_address = socket.gethostbyname(socket.gethostname())

port = randint(0, 65535)  # Port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_address, port))
server.listen()

clients = []
nicknames = []


class Server_GUI(QMainWindow):
    def __init__(self):
        super(Server_GUI, self).__init__()
        uic.loadUi("servergui.ui", self)
        self.show()

        self.txtIP_Server.setText(ip_address)
        self.txtPort_Server.setText(str(port))

    def closeEvent(self, event):
        close = QMessageBox.question(self, "QUIT", "Bạn có thật sự muốn thoát?", QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# broadcast
def broadcast(message):
    for client in clients:
        client.send(message)


# handle
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            window.txtDisplay.setText(f"{nicknames[clients.index(client)]}\n")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


# receive
def receive():
    while True:
        client, address = server.accept()
        window.txtDisplay.setText(f"Địa chỉ kết nối: {address}\n")

        client.send("NAME".encode('utf-8'))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        # print(f"Tên người dùng: {nickname}")
        window.txtDisplay.setText(f"Tên người dùng: {nickname}\n")
        broadcast(f"{nickname} kết nối đến server!\n".encode('utf-8'))
        client.send("Kết nối đến server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


# Run GUI
app = QApplication(sys.argv)
window = Server_GUI()
window.txtDisplay.setText("Server đang chạy...")
window.show()
sys.exit(app.exec_())
receive()
