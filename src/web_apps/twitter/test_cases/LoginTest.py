from src.web_apps.twitter.components.pre_login_home.login_span import LoginSpan

__author__ = 'anupama'


class LoginTest:
    def __init__(self):
        self.login_span = LoginSpan()

    def login_test(self, username, password):
        self.login_span.login(username, password)
        # self.login.login(self.test_input.username, self.test_input.password)

def login_test(test_input=None):
    LoginTest().login_test("netsgr8_4us@yahoo.com" ,"thisispassword")

