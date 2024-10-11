from os import environ
from pathlib import Path

BODY = Path(Path(__file__).parent / "textfile.txt").read_text()
PASSWORD = environ.get("OUTLOOK_MAIL_SECRET_CODE") or ""
FROM_EMAIL = "noob24dev@outlook.com"
TO_EMAIL = "itzprem2008singh@gmail.com"


SUBJECT = "Subject"
