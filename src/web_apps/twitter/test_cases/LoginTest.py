from src.web_apps.twitter.components.login import Login

__author__ = 'anupama'


class LoginTest:
    def __init__(self, test_input):
        self.login = Login()
        self.test_input = test_input

    def login_test(self):
        self.login.login("netsgr8_4us@yahoo.com" , "thisispassword")
        # self.login.login(self.test_input.username, self.test_input.password)

    #
    #
    # def tweet (self):
    #     login = Login ("Login.json", "login-span")
    #     login.login("netsgr8_4us@yahoo.com" , "thisispassword")
    #     new_tweet = NewTweet ("logged_in_home.json", "new_tweet")
    #     new_tweet.tweet("auto tweet")

# print os.getcwd()
def login_test():
    Login().login_test()