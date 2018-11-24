import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask import Flask, session, render_template, request, redirect, url_for, escape, flash
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)



@app.route("/", methods=['GET', 'POST'])
# def index():
#     return (render_template("layout.html"))  

# @app.route("/login", )
def login():
    # Sign in procedure, checks database for BOTH.
    if request.method == 'POST':
        session['username'] = request.form['username']
        return render_template("layout.html")
    else: 
        return render_template("layout.html")

@app.route("/signout") #there's an issue with the route here, that is making it redirect to /signout insead of just back to the homepage. 
def signout():
    session.pop('username', None)
    return redirect(url_for(render_template("layout.html")))

# @socketio.on('connect')
# def connect_handler():
#     if current_user.is_authenticated:
#         emit('my response',
#              {'message': '{0} has joined'.format(current_user.name)},
#              broadcast=True)
#     else:
#         return False  # not allowed here