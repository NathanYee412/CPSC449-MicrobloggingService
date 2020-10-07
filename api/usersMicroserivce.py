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

class User(db.Model):

    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    hashed_password = db.Column(db.String(80), unique=True)
    
    def __init__(self, username, email, hashed_password):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password



@app.route('/createUser', methods=["POST"])
def createUser(username, email, password):
    db = sqlite3.connect('micro.db')
    
    #store user variables 
    username = request.json['username']
    email = request.json['email']
    hashed_password = request.json['hashed_password']

    #create new user object to pass into db
    newUser = User(username, email, hashed_password)

    #add new user to db 
    db.session.add(newUser)
    db.session.commit()

    return jsonify(new_user)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/auth')
def authenticateUser(username, hashed_password):
    user = User.query.filter_by(username=username).first()


def addFollower(usermame, userToFollow):
    #implement this
    return "username + ' is now following ' + userToFollow"
    
def removeFollower(username, usernameToRemove):
    #implement this
    return "username + ' is removed ' + usernameToRemove"


app.run()


    """
    from class user 

    def dataToDict(self):
        data = {
            'username' : self.username,
            'email' : self.email,
            'hashed_password' : self.hashed_password,
            '_links' : {
                'self' : url_for('api.get_user', id=self.id),
                'followers' : url_for('api.get_followers', id=self.id),
                'followed' : url_for('api.get_followed', id=self.id),
            }
        }
    """