import flask
from flask_api import FlaskAPI
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

"""
createUser(username, email, password)
Registers a new user account.

authenticateUser(username, hashed_password)
Returns true if the password matches the username.

addFollower(username, usernameToFollow)
Start following a new user.

removeFollower(username, usernameToRemove)
Stop following a user.

"""


"""

1. need to figure out which database we're supposed to use
2. is the database preloaded with data? 

"""

# db = sqlite3.connect('project2.db')
# Not sure if Users is supposed to be a class 
class Users(db.Model):

    # username = db.Column(db.String, primary_key=True)
    # password = db.Column(db.String)
    # hashed_password = (db.string)

    def createUser(username, email, password):
        #implement this
        return "<p>User has been created</p>"

    def authenticateUser(username, hashed_password):
        #implement this
        return False

    def addFollower(usermame, userToFollow):
        #implement this
        return "username + ' is now following ' + userToFollow"
        
    def removeFollower(username, usernameToRemove):
        #implement this
        return "username + ' is removed ' + usernameToRemove"


@app.route('/', methods=['GET'])
def home():
    return "<h1>CPSC 449 PROJECT 2</h1><p>Back-end microservices project for a microblogging service similar to Twitter.</p>"

app.run()