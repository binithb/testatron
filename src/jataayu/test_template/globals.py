__author__ = 'anupama'
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

global  driver

def init():
    """
    :return:
    """
    global  driver
    binary = FirefoxBinary('/home/anupama/Downloads/sw/firefox/firefox')
    driver = webdriver.Firefox(firefox_binary=binary)
    driver.get("http://www.twitter.com")
    username = driver.find_element_by_id("signin-email")
    print "username is"
    print username
    # username.send_keys("123")


def get_driver():
    """
    :return:
    """
    global driver
    return driver


def get_open_windows():
    open_windows = driver.window_handles
    print "open_windows start"
    print open_windows
    print "open_windows end------------------"
    for window in open_windows:
        print window
    print "open_windows end-----------------2"
    # driver = webdriver.PhantomJS()

# init()