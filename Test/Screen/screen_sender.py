from vidstream import ScreenShareClient
import threading

port = input("Enter port of server: ")
port_int = int(port)
print("Connecting... Wait a second!!!")

sender = ScreenShareClient('192.168.1.9', port_int)

send_thread = threading.Thread(target=sender.start_stream)
send_thread.start()

while input("") != "STOP":
    continue

sender.stop_stream()
