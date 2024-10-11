from datetime import datetime
from http.server import SimpleHTTPRequestHandler
from os import makedirs, path
from pathlib import Path
from re import findall, sub
from socketserver import TCPServer
from subprocess import run

from .setting import DOWNLOAD_PATH, WORKING_DIR


def initialize() -> None:
    """initialize the server"""

    if not DOWNLOAD_PATH.exists():
        makedirs(DOWNLOAD_PATH, exist_ok=True)


def getIP() -> list[str]:
    """Return all IP addresses"""
    try:
        result = run(["ip", "a"], capture_output=True, text=True)
        if result.returncode != 0:
            print("Error executing ip command.")
            return []

        output = result.stdout
        ipMatches = findall(r"inet (\d+\.\d+\.\d+\.\d+)", output)

        return ipMatches
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def getServerIP() -> str:
    """return server ip"""

    return getIP()[-1]


def getFilePath(filename: str) -> str:
    """This function returns the absolute file path for a given filename."""
    return path.join(WORKING_DIR, filename)


def getUniqueFilePath(filename: str) -> Path:
    """return file path for a given filename"""

    filePath = DOWNLOAD_PATH / filename

    if filePath.exists():
        return getUniqueFilePath(str(datetime.now().time()) + "_" + filename)

    return filePath


def removeNonePrintAbleChar(text: str) -> str:
    """remove none print able characters"""

    word = "".join(filter(lambda x: ord(x) < 128, text))
    word = sub(r"\s{2,}", "", word)

    if not word:
        word = "file"

    return word


def startserver(
    FileServer, HOST: str = getServerIP(), PORT: int = 8000
) -> tuple[TCPServer, str, int]:
    """start sever to given host and port"""
    try:
        return TCPServer((HOST, PORT), FileServer), HOST, PORT

    except OSError:
        return startserver(FileServer, HOST, PORT + 1)


def send404(request: SimpleHTTPRequestHandler) -> None:
    """send file content"""

    request.send_response(404)
    request.send_header("Content-type", "text/html")
    request.end_headers()

    filePath = getFilePath("templates/error.html")

    with open(filePath, "rb") as f:
        content = str(f.read().decode())

        request.wfile.write(content.encode())
        f.close()

    return


def getHtml(filename: str) -> str:
    """return file type"""

    _type = {
        "jpg": "<img src='{filename}' width='200'>",
        "jpeg": "<img src='{filename}' width='200'>",
        "png": "<img src='{filename}' width='200'>",
        "gif": "<img src='{filename}' width='200'>",
        "svg": "<img src='{filename}' width='200'>",
        "avi": "<video controls width='400'><source src='{filename}' type='video/mp4'></video>",
        "mkv": "<video controls width='400'><source src='{filename}' type='video/mp4'></video>",
        "mov": "<video controls width='400'><source src='{filename}' type='video/mp4'></video>",
        "mp4": "<video controls width='400'><source src='{filename}' type='video/mp4'></video>",
        "wav": "<audio controls><source src='{filename}' type='audio/mpeg'></audio>",
        "ogg": "<audio controls><source src='{filename}' type='audio/mpeg'></audio>",
        "mp3": "<audio controls><source src='{filename}' type='audio/mpeg'></audio>",
        "pdf": "<a href='{filename}'>{filename}</a> (PDF)",
        "txt": "<a href='{filename}'>{filename}</a> (Text)",
    }

    return _type.get(filename.split(".")[-1], "")


class HtmlTypeCreater:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __str__(self) -> str:
        return getHtml(self.filename)
