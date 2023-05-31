import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
    #Tweet create
    def tweet(self,person,content):
        query = f"INSERT INTO tweets (person,content) VALUES (%s,%s)"
        cursor = self.connection.cursor()
        cursor.execute(query,(person,content))
        self.connection.commit()
        cursor.close()
    
    #Tweet reply
    def insert_reply(self, person, tweet_id, reply_content):
        query = f"INSERT INTO replies (person, tweet_id, content) VALUES (%s, %s, %s)"
        values = (person, tweet_id, reply_content)
        cursor = self.connection.cursor()
        cursor.execute(query,values)
        self.connection.commit()
        cursor.close()
    #Get tweets
    def get_recent_tweets(self, limit=10):
        query = f"SELECT t.id, t.person, t.content, r.person AS reply_person, r.content AS reply_content " \
                f"FROM tweets t LEFT JOIN replies r ON t.id = r.tweet_id ORDER BY t.id DESC LIMIT {limit}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        
        tweets = []
        current_tweet = None
        for row in data:
            tweet_id = row[0]
            tweet_person = row[1]
            tweet_content = row[2]
            reply_person = row[3]
            reply_content = row[4]
            
            if not current_tweet or current_tweet['id'] != tweet_id:
                current_tweet = {'id': tweet_id, 'person': tweet_person, 'content': tweet_content, 'replies': []}
                tweets.append(current_tweet)
            
            if reply_person and reply_content:
                reply = {'person': reply_person, 'content': reply_content}
                current_tweet['replies'].append(reply)
        
        return tweets
    
    #Disconnect
    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data
