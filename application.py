import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask import Flask, session, render_template, request, redirect, url_for, escape, flash
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

slackish = {'users': [], 'channels': []}
users = []

@app.route("/")
def index():
    return render_template("layout.html")  

# @socketio.on('logged on')
# def loggedOn(username):
#     return render_template("layout.html", username=username)  

@socketio.on('connection')
def connect_handler(data, user):
    users.append(user)
    print(users)
    emit('my response',
            {'message': '{0} has joined'.format(user)},
            broadcast=True)

@socketio.on('channelCreation')
def channelCreation(data):
    # check if channel already exits, if not create a new channel
    if data in slackish['channels']:
        print('error')
    else: 
        slackish['channels'].append(data)
        print('channel created')

# @app.route("/signout") #there's an issue with the route here, that is making it redirect to /signout insead of just back to the homepage. 
# def signout():
#     session.pop('username', None)
#     return render_template("layout.html")