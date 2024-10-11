from http.server import SimpleHTTPRequestHandler
from os import listdir, path
from re import search
from urllib.parse import unquote

from package.helper import (
    getFilePath,
    getUniqueFilePath,
    initialize,
    removeNonePrintAbleChar,
    send404,
    startserver,
)
from package.multipart import MultipartParser
from package.setting import CSS_PATH, CURRENT_PATH, HTML_PATH, JAVASCRIPT_PATH


class FileServer(SimpleHTTPRequestHandler):
    def sendFile(self, filePart: tuple[str, str], replace: dict[str, str] = {}) -> None:
        """send file content"""
        filename, extension = filePart

        filesPath = {
            ".html": HTML_PATH,
            ".css": CSS_PATH,
            ".js": JAVASCRIPT_PATH,
        }
        filesType = {
            ".html": "html",
            ".css": "css",
            ".js": "javascript",
        }

        self.send_response(200)
        self.send_header("Content-type", f"text/{filesType[extension]}")
        self.end_headers()

        filePath = getFilePath(f"{filesPath[extension]}/{filename}{extension}")

        if not path.exists(filePath):
            send404(self)

        with open(filePath, "rb") as f:
            content = str(f.read().decode())
            for placeholder, value in replace.items():
                content = content.replace(placeholder, value)

            self.wfile.write(content.encode())
            f.close()

    def sendBootstrap(self, fileType: str, filename: str) -> None:
        """send bootstrap file"""

        fileObject = getFilePath(f"bootstrap/{fileType}/{filename}")

        if not path.exists(fileObject):
            send404(self)
            return

        self.send_response(200)
        self.send_header("Content-type", f"text/{fileType}")
        self.end_headers()

        with open(fileObject, "rb") as f:
            self.wfile.write(f.read())
            f.close()

    def do_GET(self) -> None:
        if self.path == "/":
            self.send_response(302)
            self.send_header("Location", "/home")
            self.end_headers()

        elif reMatch := search(r"^/(upload|about|home|setting)/?$", self.path):
            self.sendFile((reMatch.group(1), ".html"))

        elif reMatch := search(
            r"^/static/(?P<type>style|script)/(?P<name>\w+)(?P<ext>\.\w+)/?$", self.path
        ):
            self.sendFile(reMatch.groups()[1::])  # type: ignore

        elif reMatch := search(
            r"^/bootstrap/(?P<type>css|javascript)/(?P<filename>.+)/?$", self.path
        ):
            self.sendBootstrap(*reMatch.groups())

        elif search(r"^/favicon\.ico/?$", self.path):
            self.send_response(200)
            self.send_header("Content-type", "image/x-icon")
            self.end_headers()
            with open(getFilePath("assets/favicon.ico"), "rb") as f:
                self.wfile.write(f.read())

        elif search(r"^/download/?$", self.path):
            fileList = ""

            for f in listdir():
                if path.isfile(f):
                    # <div class="file-label" data-file="{ f }">{ f }</div>

                    fileList += f'<div class="file-label" data-file="{f}">{f}</div>'

            self.sendFile(
                ("download", ".html"), {"{{ fileList }}": fileList or "No Files"}
            )

        elif reMatch := search(r"^/downloadfile=(?P<filename>.+)/?$", self.path):
            fileName = unquote(reMatch.group("filename"))

            filePath = CURRENT_PATH / fileName

            if not filePath.exists():
                send404(self)
                return

            with open(CURRENT_PATH / fileName, "rb") as f:
                fileContent = f.read()
                f.close()

            self.send_response(200)
            self.send_header("Content-type", "application/octet-stream")
            self.send_header(
                "Content-Disposition",
                "attachment; filename={}".format(fileName),
            )
            self.send_header("Content-Length", str(len(fileContent)))
            self.end_headers()

            self.wfile.write(fileContent)

        elif reMatch := search(r"^/file/(?P<filename>.+)/?$", self.path):
            filename = reMatch.group("filename")
            filepath = getFilePath(filename)

            if path.exists(filepath):
                with open(filepath, "rb") as f:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(f.read())

            else:
                send404(self)

        else:
            send404(self)

    def do_POST(self) -> None:
        if search(r"^/uploadfile/?$", self.path):
            initialize()

            if reMatch := search("boundary=(.+)", self.headers["Content-Type"]):
                boundary = reMatch.group(1)

            else:
                send404(self)
                return

            form = MultipartParser(
                self.rfile, boundary, int(self.headers["Content-Length"])
            )
            file = form.get("files")
            if file is not None:
                if name := file.filename:
                    file.save_as(getUniqueFilePath(removeNonePrintAbleChar(name)))

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Files uploaded successfully")

        else:
            send404(self)


if __name__ == "__main__":
    Server, host, port = startserver(FileServer)
    print(f"Server running on http://{host}:{port}")

    try:
        Server.serve_forever()

    except KeyboardInterrupt:
        print("Server shutdown")
        Server.shutdown()
