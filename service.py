from dbcon import Database
import os
class Tweet:
    def __init__(self, person, content):
        self.person = person
        self.content = content

class Reply(Tweet):
    def __init__(self, person,content, tweet_id):
        super().__init__(person ,content)
        self.tweet_id = tweet_id

class MyService:
    def __init__(self):
        mysql_host = os.environ.get('DB_HOST', 'db')  
        mysql_user = 'root'
        mysql_password = 'root'
        mysql_database = 'tweetreloaded'
        self.db = Database(mysql_host, mysql_user, mysql_password, mysql_database)

    def create_something(self, action,tweet_id ,person, content):
        if action == 'tweet':
            newTweet = Tweet(person, content)
            self.create_tweet(newTweet)
        else:
            newReply = Reply(person,content,tweet_id)
            self.create_reply(newReply)

    def create_tweet(self, tweet):
        self.db.connect()
        self.db.tweet(tweet.person, tweet.content)
        self.db.disconnect()

    def create_reply(self, reply):
        self.db.connect()
        self.db.insert_reply(reply.person, reply.tweet_id, reply.content)
        self.db.disconnect()


    #Get tweets
    def get_recent_tweets(self, limit=10):
        self.db.connect()
        tweets = self.db.get_recent_tweets(limit)
        self.db.disconnect()
        return tweets
