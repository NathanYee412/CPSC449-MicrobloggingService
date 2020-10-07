import flask
from flask_api import FlaskAPI
from flask import request, jsonify
from werkzeug import check_password_hash, generate_password_hash
import sqlite3


app = flask.Flask(__name__)
app.config["DEBUG"] = True

DATABASE = '/project2.db'


class User(db.Model):
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.hashed_password = generate_password_hash(password, "sha256")

    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password

    def get_hash_pw(self):
        return self.hashed_password


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv


@app.route('/createUser', methods=["POST"])
def createUser(username, email, password):
    con = sqlite3.connect('project2.db')
    cur = con.cursor()

    #create new user object to pass into db
    newUser = User(username, email, password)

    #add new user to db 
    cur.execute('INSERT INTO users VALUES (?,?,?,?)', newUser.username,newUser.email,newUser.get_hash_pw)
    con.session.commit()
    con.close()

    return jsonify(newUser)



@app.route('/auth')
def authenticateUser(username, hashed_password):
    auth = False
    #query database to get users hashed pw
    password = query_db('select password from user where pw_hash = ?', [hashed_password], one=True)
    
    #check if both hased passwords match 
    if password == hashed_password:
        auth = True
    
    return auth


def addFollower(usermame, userToFollow):
    con = sqlite3.connect('project2.db')
    cur = con.cursor()
    cur.execute('insert into follower (followee, follower) values (?, ?)', [username, userToFollow])
    con.session.commit()
    con.close()
    

def removeFollower(username, usernameToRemove):
    userid = query_db('select user_id from user where username = ?', [username], one=True)
    followerid = query_db('select user_id from user where username = ?', [usernameToRemove], one=True)
    
    con = sqlite3.connect('project2.db')
    cur = con.cursor()
    cur.execute('delete from followerID where followeeID = ? and follower = ?', [userid, followerid)
    cur.commit()
    con.close()


app.run()

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
    from class user 

    
    # username = db.Column(db.String(80), unique=True)
    # email = db.Column(db.String(120), unique=True)
    # hashed_password = db.Column(db.String(80), unique=True)


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
