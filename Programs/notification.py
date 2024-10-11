import time

from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="Remainder",
        message="Time over",
        timeout=2,
    )

    time.sleep(7)
