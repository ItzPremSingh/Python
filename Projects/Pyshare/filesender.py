import socket
import os
import animation
import IP
from sizeformater import sizeFormat
from threading import Thread

argv = os.sys.argv
host = IP.IPAddress()
port = 8000

if argv[1::]: filename = argv[1]
else: 
    print(f"File Required!")
    quit()

if not os.path.exists(filename):
    print(f"\n\n{filename!r} File Not Found!")
    quit()

class Sender(Thread):
    def __init__(self, filename, length, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self.length = length
        self.byteSended = 0
        self.filename = filename

    def run(self):
        with open(self.filename, "rb+") as file:
            for filedata in file.readlines():
                client.send(filedata)
                self.byteSended += len(filedata)


fileLength = os.stat(filename).st_size
fileSize = sizeFormat(fileLength, 1)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

print(f"\nServer Start On ({host}, {port})")

anim = animation.Animation("wating", .3)
anim.start()

client, address = sock.accept()
anim.Running = False

print("Reciver Connected!")

client.send(f"{filename.split('/')[-1]}!!{fileLength}".encode())
response = client.recv(1024)

print(f"SENDING: {filename!r}\n")

sender = Sender(filename, fileLength)
sender.start()

animation.sleep(.2)

while True:
    byte = sender.byteSended
    percent = round(byte / fileLength * 100, 1)
    print(f"\r{percent}% {sizeFormat(byte, 1)}/{fileSize}")
    print("\033[F", end="\033[K")

    if byte == fileLength: break
    animation.sleep(.1)

client.send(b"File Sended")
sock.close()
print("File Sended")
