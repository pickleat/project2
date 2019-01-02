import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask import Flask, session, render_template, request, redirect, url_for, escape, flash
from flask_session import Session
import json


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

users = []
slackish = {}
channels = []

@app.route("/")
def index():
    print('you made it to the homepage')
    return render_template("layout.html")



@socketio.on('user joined')
def connect(user):
    if user not in users:
        users.append(user)
        print(user + ': has joined the room')
        print(users)
    if user in users: 
        print(user + ': has re-joined the room')
        print(users)
    obj = json.dumps(slackish)
    print(obj)
    emit('channels list', obj, broadcast=True)
    emit(user + ': has joined the room', broadcast=True)

    
@socketio.on('add new channel')
def newChannel(channelName):
    print(channelName)
    # checks if channel already exists
    if channelName in slackish.keys():
        print('already a channel')
    # creates new channel object
    if channelName not in slackish.keys(): 
        print('new channel created')
        slackish[channelName] = {'messages': []}
        obj = json.dumps(slackish)
        print(obj)
        emit('channels list', obj, broadcast=True)
        
        
# @socketio.on('broadcast')
# def everyting():
#     obj = json.dumps(slackish)
#     print(obj)
#     emit('channels list', obj, broadcast=True)


# @socketio.on('new channel')
# def channelCreation(data):
#     print('made it to channel creation')
#     # check if channel already exits, if not create a new channel
#     if data in channels:
#         print('channel name already used')
#     else: 
#         channels.append(data)
#         print('channel created')

# @socketio.on('message')
# def printMessage(msg):
#     print('message'+ msg)
#     emit(msg, broadcast=True)