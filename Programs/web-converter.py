from WebApp import run, route, render
from converter import _convert


@route("/")
def home():
    return """Welcome to unit converter<br><a href="converter">Tryit now</a>"""


@route("/converter")
def conve():
    return render("converter.html", value=None)


@route("/converter", method="POST")
def value(data):
    _from = int(data["from"][0])
    to = int(data["to"][0])
    number = int(data["number"][0])

    return render("converter.html", value=_convert(_from, to, number))


run(port=8080)
