from web_apps.twitter.components.post_login_home.global_actions import GlobalActions

__author__ = 'anupama'


class GlobalNav:
    def __init__(self):
        self.global_actions = GlobalActions()


def check_exists(test_input=None):
    print "test_input : " + str(test_input)
    GlobalNav()
