from datetime import datetime
from json import load
from pathlib import Path
from re import search
from time import sleep

from PIL import Image, ImageDraw, ImageFont

config = (
    lambda configPath: load(open(configPath)) if Path(configPath).exists() else {}
)(Path(__file__).parent / "config.json")


def extractRgbaValue(rgbaString: str) -> tuple[int, int, int, int]:
    pattern = r"rgba\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([\d.]+)\s*\)"

    match = search(pattern, rgbaString)

    if match:
        r = int(match.group(1))
        g = int(match.group(2))
        b = int(match.group(3))
        a = int(match.group(4))

        return r, g, b, a
    else:
        raise ValueError("Invalid RGBA string format, in config.json file")


def createClockImage(timeStr: str, filePath: str) -> None:
    """
    Creates an attractive image with the specified time string and saves it to the given file path using configuration from the JSON file.

    Args:
        timeStr (str): The time string to display on the image (in "HH:MM" format).
        filePath (str): The path where the image will be saved.
        configPath (str): The path to the JSON configuration file.
    """

    backgroundColor: str = config.get("background_color", "rgba(255, 225, 225, 0)")
    shadowOffset: tuple[int, int] = tuple(config.get("shadow_offset", (2, 2)))  # type: ignore
    borderThickness: int = config.get("border_thickness", 2)
    borderColor: str = config.get("border_color", "black")
    shadowColor: str = config.get("shadow_color", "gray")
    textColor: str = config.get("text_color", "white")
    fontSize: int = config.get("font_size", 20)
    height: int = config.get("height", 100)
    width: int = config.get("width", 200)

    image = Image.new("RGBA", (width, height), extractRgbaValue(backgroundColor))
    draw = ImageDraw.Draw(image)

    draw.rectangle(
        [
            borderThickness // 2,
            borderThickness // 2,
            width - borderThickness // 2,
            height - borderThickness // 2,
        ],
        outline=borderColor,
        width=borderThickness,
    )

    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", fontSize
        )
    except IOError:
        font = ImageFont.load_default()

    textBBox = draw.textbbox((0, 0), timeStr, font=font)
    textWidth = textBBox[2] - textBBox[0]
    textHeight = textBBox[3] - textBBox[1]
    position = (
        (width - textWidth) // 2,
        (height - textHeight) // 2 - 5,
    )

    draw.text(
        (position[0] + shadowOffset[0], position[1] + shadowOffset[1]),
        timeStr,
        fill=shadowColor,
        font=font,
    )
    draw.text(position, timeStr, fill=textColor, font=font)

    image.save(filePath)


def updateIcon() -> None:
    """Updates the clock icon in the system tray with the current time.

    This function runs an infinite loop, updating the clock icon every minute.
    """

    def imageWithTime() -> None:
        """Creates the clock image with the current time and saves it to the specified file."""
        createClockImage(
            datetime.now().strftime("%I:%M %p"),
            str(Path().home() / "Desktop" / "clock_icon.png"),
        )

    imageWithTime()
    sleep(60 - datetime.now().second)

    while True:
        imageWithTime()
        sleep(60)


if __name__ == "__main__":
    updateIcon()
