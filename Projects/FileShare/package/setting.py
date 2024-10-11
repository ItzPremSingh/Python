from os import environ, path
from pathlib import Path

DOWNLOAD_PATH = Path(environ["HOME"]) / "Downloads" / "File Share"
WORKING_DIR = Path("/".join(str(path.dirname(__file__)).split("/")[:-1]))
CURRENT_PATH = Path()

JAVASCRIPT_PATH = "static/scripts"
CSS_PATH = "static/styles"
HTML_PATH = "templates"
