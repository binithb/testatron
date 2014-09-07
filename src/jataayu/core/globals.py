__author__ = 'anupama'
from selenium import webdriver


def init():
    """
    :return:
    """

    :rtype : nothing
    """
    global  driver = webdriver.Firefox()
    # driver = webdriver.PhantomJS()
    driver.get("http://www.twitter.com")
