import flask
from flask_api import FlaskAPI
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

"""
getUserTimeline(username)
Returns recent tweets from a user.

getPublicTimeline()
Returns recent tweets from all users.

getHomeTimeline(username)
Returns recent tweets from all users that this user follows.

postTweet(username, text)
Post a new tweet.

"""

def getUserTimeline(username):
    tweets = []
    return tweets

def getPublicTimeline():
    return tweets

def getHomeTimeline(username):
    return recentTweets

def postTweet(username, text):
    print('tweet posted')

@app.route('/', methods=['GET'])
def home():
    return "<h1>CPSC 449 PROJECT 2</h1><p>Back-end microservices project for a microblogging service similar to Twitter.</p>"