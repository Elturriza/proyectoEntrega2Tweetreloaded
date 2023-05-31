
from flask import Flask, render_template, request, redirect, url_for
from service import MyService
import csv
import datetime

app = Flask(__name__)
my_service = MyService()

def log_action(action,person):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('log.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, action,person])

app = Flask(__name__)
#Post tweet
@app.route('/tweet', methods=['POST'])
def tweet():
    person = request.form.get('person')
    tweet_content = request.form.get('content')    
    my_service.create_something('tweet',0,person,tweet_content)
    log_action('tweet',person)
    return redirect(url_for('home'))

#Post answer tweet
@app.route('/anstweet/<int:tweet_id>/reply', methods=['POST'])
def anstweet(tweet_id):
    person = request.form.get('person_reply')
    reply_content = request.form.get('content_reply')    
    my_service.create_something('reply',tweet_id,person,reply_content)
    log_action('reply',person)
    return redirect(url_for('home'))


#Panel home de inicio
@app.route('/',methods=['GET'])
def home():
    tweets = my_service.get_recent_tweets()
    return render_template('home.html', tweets=tweets)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=80)