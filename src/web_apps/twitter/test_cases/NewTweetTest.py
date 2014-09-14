from src.web_apps.twitter.components.post_login_home.tweet_box import TweetBox

__author__ = 'anupama'


class NewTweetTest:
    def __init__(self):
        self.tweet_box = TweetBox()

    def new_tweet(self, tweet_message):
        self.tweet_box.tweet(tweet_message)

def tweet(test_input=None):
    NewTweetTest().new_tweet("I m a Robot who can tweet")