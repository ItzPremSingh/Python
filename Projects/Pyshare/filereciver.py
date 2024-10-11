import socket
import os
from threading import Thread
from sizeformater import sizeFormat
from time import sleep, time

argv = os.sys.argv
host = "127.0.0.1"
port = 8000

if argv[1::]: host = argv[1]
if argv[2::]: port = int(argv[2])

class Reciver(Thread):
    def __init__(self, filename, length, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self.length = length
        self.byteRecived = 0
        self.filename = filename

    def run(self):
        with open(self.filename, "ab+") as file:
            while True:
                data = sock.recv(1024)
                if data.endswith(b"File Sended"):
                    break

                self.byteRecived += file.write(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host, port))

except:
    print(f"Can't Connect To ({host}, {port})")
    quit()


fileData = sock.recv(1024).decode().split("!!")
fileLength = int(fileData[1])
filename = fileData[0]
fileSize = sizeFormat(fileLength, 1)

if os.path.exists(filename):
    date = str(int(time()))

    filesplit = filename.split(".")
    fileExt = filesplit[1] if filesplit[1::] else ""
    filename = filesplit[0] + "_" + date + "." + fileExt

sock.send(b"DATASENDED\r\n")

print(f"RECIVING: {filename!r}\n")

reciver = Reciver(filename, fileLength)
reciver.start()

sleep(.2)

while True:
    byte = reciver.byteRecived
    percent = round(byte / fileLength * 100, 1)
    print(f"\r{percent}% {sizeFormat(byte, 1)}/{fileSize}")
    print("\033[F", end="\033[K")
    
    if byte == fileLength: break
    sleep(.1)
    
print("File Recived!")
