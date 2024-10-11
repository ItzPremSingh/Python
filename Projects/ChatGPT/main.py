from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from setting import CHROME_DRIVER_PATH

# Configure Chrome options
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")
options.add_argument("--start-maximized")
# Uncomment the next line to run Chrome in headless mode (more detectable)
# options.add_argument("--headless")

# Set a custom User-Agent string
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(str(CHROME_DRIVER_PATH)), options=options)

# Modify the navigator.webdriver property
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
    },
)

# Disable WebRTC to prevent IP leaks
# driver.execute_cdp_cmd("WebRTC.setLocalDescription", {"description": ""})

# Remove the 'automation' tag from Chrome's window
# driver.execute_script(
#     "Object.defineProperty(window, 'chrome', { get: () => undefined })"
# )
# driver.execute_script("""
#     Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
#     Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });
# """)


driver.get("https://www.chatgpt.com")

input("Press Enter to continue...")

driver.quit()
