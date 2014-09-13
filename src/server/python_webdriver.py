__author__ = 'anupama'
# Copyright 2014 Anupama Kattiparambil Prakasan
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import importlib
# import globals

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class PythonWebDriver(object):
    def __init__(self):
        binary = FirefoxBinary('/home/anupama/Downloads/sw/firefox/firefox')
        self.driver = webdriver.Firefox(firefox_binary=binary)
        # globals.init()
        # self.driver = globals.driver

    def register_web_driver(self, home_page):
        self.driver.get(home_page)
        # username = self.driver.find_element_by_id("signin-email")
        # print "username is"
        #     print username
        # raise AssertionError("Given strings are not strings.")

    def register_webapp(self, webapp):
        pass

    def register_module(self, module):
        pass

    def execute_function(self, function, class_name=None, web_app=None, **kwargs):
        class_ = _get_class(class_name, web_app)
        if class_:
            return _execute_function(function, kwargs)


def _get_class(class_name, web_app):
    module_name = "src.web_apps." + web_app
    import src.web_apps.twitter.test_cases.LoginTest
    LoginTest.login_test()


    print module_name
    try:
        module = importlib.import_module(module_name)
        try:
            class_ = getattr(module, class_name)()
        except AttributeError:
            raise AssertionError('class does not exist')
    except ImportError:
        raise AssertionError('module does not exist')
    return class_ or None


def _execute_function(class_name, function_name):
    try:
        function = getattr(class_name, function_name)
    except AttributeError:
        raise AssertionError('function does not exist')
    return function()


if __name__ == '__main__':
    import sys
from robotremoteserver import RobotRemoteServer
RobotRemoteServer(PythonWebDriver(), *sys.argv[1:])
