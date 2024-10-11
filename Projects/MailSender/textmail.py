from email.message import EmailMessage
from smtplib import SMTP, SMTPAuthenticationError
from socket import gaierror

from credentials import BODY, FROM_EMAIL, PASSWORD, SUBJECT, TO_EMAIL
from helper import error, serverName

MESSAGE = EmailMessage()

MESSAGE.set_content(BODY)
MESSAGE["Subject"] = SUBJECT
MESSAGE["From"] = FROM_EMAIL
MESSAGE["To"] = TO_EMAIL


if Host_Port := serverName(FROM_EMAIL):
    HOST, PORT = Host_Port

else:
    error("User email address in not in format")
    quit()

try:
    smtp = SMTP(HOST, PORT)

except gaierror:
    error("Connection failed!")
    quit()


statusCode, response = smtp.ehlo()
statusCode, response = smtp.starttls()

try:
    statusCode, response = smtp.login(FROM_EMAIL, PASSWORD)

except SMTPAuthenticationError:
    error("User credentials were incorrect")
    quit()


smtp.send_message(MESSAGE)
print("sended")
smtp.quit()
