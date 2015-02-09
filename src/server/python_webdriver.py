import os

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
import src.testatron.test_template.project_suite_globals as project_suite_globals


from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class PythonWebDriver(object):
    def __init__(self):
        binary = FirefoxBinary('/home/anupama/Downloads/sw/firefox/firefox')
        self.driver = webdriver.Firefox(firefox_binary=binary)
        project_suite_globals.driver = self.driver

    def register_web_driver(self, web_app, home_page):
        self.driver.get(home_page)
        project_suite_globals.web_app = web_app
        # username = self.driver.find_element_by_id("signin-email")
        # print "username is"
        #     print username
        # raise AssertionError("Given strings are not strings.")

    def register_webapp(self, webapp):
        pass

    def register_module(self, module):
        pass

    def execute_function(self, function, module_name=None, **kwargs):
        module = _get_module(module_name)
        if module:
            return _execute_function(module, function, **kwargs)


def _get_module(class_name):
    web_app = project_suite_globals.web_app
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    print (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    # import web_apps.twitter.test_cases.LoginTest as LoginTest

    # import pdb ; pdb.set_trace()
    # print "executing test"
    # LoginTest.login_test()
    # print "executed test"

    try:
        module_name = "src.web_apps." + web_app + ".test_cases." + class_name
        print module_name
        module = importlib.import_module(module_name)
        print "module %s " % module
        # try:
        #     print "class_name %s " % class_name
        #     class_ = getattr(module, class_name)()
        #     print "class %s " % class_
        # except AttributeError:
        #     raise AssertionError('class does not exist')
    except ImportError:
        raise AssertionError('module does not exist')

    return module or None


def _execute_function(module_name, function_name, **kwargs):
    try:
        function = getattr(module_name, function_name)
    except AttributeError:
        raise AssertionError('function does not exist')
    print "function %s " % function
    print "kwargs : " + str(kwargs)
    args_dict = None
    if "kwargs" in kwargs:
        args_dict = kwargs["kwargs"]
    return function(args_dict)


if __name__ == '__main__':
    import sys
from robotremoteserver import RobotRemoteServer
RobotRemoteServer(PythonWebDriver(), *sys.argv[1:])
