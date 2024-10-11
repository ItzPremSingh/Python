# Tic Tac Tie Game
from flask import Flask, render_template

app = Flask(__name__)

players_turn = {"X", "O"}
waiting_player = None


@app.route("/")
def index() -> str:
    return render_template("index.html")


