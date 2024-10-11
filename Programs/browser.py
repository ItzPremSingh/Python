from subprocess import run


def dinoGame() -> None:
    url = "chrome://dino/"
    run(["xdg-open", url])


def openBrowser(search: str) -> None:
    url = f"https://duckduckgo.com/?q={search.replace(' ', '+')}"
    run(["xdg-open", url])


dinoGame()
