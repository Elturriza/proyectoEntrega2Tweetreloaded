USE tweetreloaded;
CREATE TABLE replies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tweet_id INT,
    content TEXT,
    person VARCHAR(255),
    FOREIGN KEY (tweet_id) REFERENCES tweets(id)
);