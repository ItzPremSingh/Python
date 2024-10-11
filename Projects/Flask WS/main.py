from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

rooms = set()


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("create_room")
def handle_create_room(data):
    room = data.get("room")
    if room:
        if room not in rooms:
            rooms.add(room)
            emit("room_created", {"room": room}, broadcast=True)
        else:
            emit("error", {"error": "Room already exists"})


@socketio.on("join_room")
def handle_join_room(data):
    room = data.get("room")
    if room in rooms:
        join_room(room)
        emit("room_joined", {"room": room}, room=room)
    else:
        emit("error", {"error": "Room does not exist"})


@socketio.on("leave_room")
def handle_leave_room(data):
    room = data.get("room")
    if room in rooms:
        leave_room(room)
        emit("room_left", {"room": room}, broadcast=True)
    else:
        emit("error", {"error": "Room does not exist"})


# WebRTC signaling
@socketio.on("offer")
def handle_offer(data):
    room = data.get("room")
    if room:
        emit("offer", data, room=room)


@socketio.on("answer")
def handle_answer(data):
    room = data.get("room")
    if room:
        emit("answer", data, room=room)


@socketio.on("candidate")
def handle_candidate(data):
    room = data.get("room")
    if room:
        emit("candidate", data, room=room)


if __name__ == "__main__":
    socketio.run(app, host="160.202.1.9", debug=True)
