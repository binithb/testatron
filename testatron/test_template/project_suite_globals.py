__author__ = 'anupama'

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = None
web_app = None


def init():
    global driver
    global web_app
    binary = FirefoxBinary('/home/anupama/Downloads/sw/firefox/firefox')
    driver = webdriver.Firefox(firefox_binary=binary)
    web_app = "twitter"
    driver.get("http://www.twitter.com")

# def get_driver():
#     """
#     :return:
#     """
#     global driver
#     return driver
#
#
# def get_open_windows():
#     open_windows = driver.window_handles
#     print "open_windows start"
#     print open_windows
#     print "open_windows end------------------"
#     for window in open_windows:
#         print window
#     print "open_windows end-----------------2"
#     # driver = webdriver.PhantomJS()

# init()