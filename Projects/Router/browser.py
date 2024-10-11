from pathlib import Path
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

CHROME_DRIVER_PATH = Path().home() / "Python" / "Chrome Driver" / "chromedriver"

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

chrome_service = Service(executable_path=str(CHROME_DRIVER_PATH))

driver = Chrome(options=chrome_options, service=chrome_service)


driver.get("http://192.168.1.1/")

sleep(1)

driver.add_cookie(
    {
        "domain": "192.168.1.1",
        "httpOnly": False,
        "name": "ecntToken",
        "path": "/",
        "sameSite": "Lax",
        "secure": False,
        "value": "28b60d4cb7636e4e817a8ab1fdb96226f",
    }
)

sleep(1)

driver.get("http://192.168.1.1/cgi-bin/content.asp")

input("Press Enter to continue...")

driver.quit()
