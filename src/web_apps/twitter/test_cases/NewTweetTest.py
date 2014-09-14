from src.web_apps.twitter.components.post_login_home.tweet_box import TweetBox
import datetime

__author__ = 'anupama'


class NewTweetTest:
    def __init__(self):
        self.tweet_box = TweetBox()

    def new_tweet(self, tweet_message):
        self.tweet_box.tweet(tweet_message)


def tweet(test_input=None):
    print "test_input : " + str(test_input)
    NewTweetTest().new_tweet(test_input["tweet_message"] +"\n" + datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))
