import os
import time
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

names = []
channels = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_name", methods=["POST"])
def add_name():
    name = request.form.get("name")
    if name in names:
        return jsonify({"success": False})
    else:
        names.append(name)
        print(name + " added")
        return jsonify({"success": True})


@app.route("/get_channels", methods=["POST"])
def get_channels():
    if channels == {}:
        return jsonify({"success": False})
    else:
        return jsonify({"success": True, "channels": channels})


@app.route("/get_messages", methods=["POST"])
def get_messages():
    channel = request.form.get("channel")
    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end")) or (start + 9)
    readed = 0
    print("requested messeges for channel:" + channel)
    print(start)
    print(end)
    if channel not in channels:
        return jsonify({"success": False})
    mens = channels[channel]["messages"][start:end]
    print(mens)
    readed = len(mens)
    print("messages readed:")
    print(readed)
    return jsonify({
        "success": True,
        "messages": mens,
        "readed": readed
    })


@socketio.on("publish channel")
def emit_test2(data):
    channelId = data["channelId"]
    channelName = data["channelName"]
    if channelId in channels:
        return jsonify({"success": False})
    channels[channelId] = {}
    channels[channelId]["name"] = channelName
    channels[channelId]["messages"] = []
    print("channel added")
    print(channels)
    emit("broadcast channel", {"channelId": channelId, "channelName": channelName}, broadcast=True)


@socketio.on("publish message")
def emit_test(data):
    channelId = data["channelId"]
    message = data["message"]
    name = data["name"]
    if channelId in channels:
        messageToAdd = {"name": name, "text": message}
        channels[channelId]["messages"].insert(0, messageToAdd)
    else:
        print("no such channel in channels")
    print(channels)
    emit("broadcast message", {"channelId": channelId, "message": message, "name": name}, broadcast=True)


# cd C:\Users\spa3cap\Documents\GitHub\project2
# venv\Scripts\activate
# pip3 install -r requirements.txt
# set FLASK_APP=app.py
# set FLASK_ENV=development
