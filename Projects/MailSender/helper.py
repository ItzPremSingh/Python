from re import search

DICT_OF_SERVER: dict[str, tuple[str, int]] = {
    "gmail": ("smtp.google.com", 587),
    "outlook": ("smtp-mail.outlook.com", 587),
    "hotmail": ("smtp-mail.outlook.com", 587),
    "yahoo": ("smtp.mail.yahoo.com", 587),
    "comcast": ("smtp.comcast.net", 587),
    "verizon": ("smtp.verizon.net", 465),
}


def validateMail(mail: str) -> str | None:
    """validate mail using mail"""

    if reMatch := search(r"^\w+@(?P<DomainName>[a-z]+)\.(com|in)$", mail):
        return reMatch.group("DomainName")


def serverName(mail: str) -> tuple[str, int] | None:
    """Find server name using mail"""

    if domainName := validateMail(mail):
        if domainName in DICT_OF_SERVER:
            return DICT_OF_SERVER[domainName]


def error(message: str) -> None:
    """Print error message"""

    print(f"ERROR: {message}")
    
# itzprem2008singh@gmail.com


print(serverName("name@outlook.com"))
