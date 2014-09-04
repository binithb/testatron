__author__ = 'anupama'

import jinja2
import simplejson as json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Component:
    def __init__(self,json_file, section):
        templateloader = jinja2.FileSystemLoader( searchpath="./" )
        templateenv = jinja2.Environment( loader=templateloader )
        template_file = json_file
        template = templateenv.get_template( template_file )
        self.page = json.loads( template.render(  ))
        self.span = self.page["elements"][section]
        self.props = {}

        print self.span

    def parse(self):
        pass

    def load(self):
        for element in self.span:
            print element
            print self.span[element]
            print self.span[element]["props"]
            print self.span[element]["props"]["loc"]
            self.props[element] = self._get_element(self.span[element]["props"]["loc"])
        pass
    def _get_element(self,loc):
        driver = webdriver.Firefox()
        #driver = webdriver.PhantomJS()
        driver.get("http://www.twitter.com")
        elem = driver.find_element_by_id("signin-email")
        print elem.__dict__

        pass

cmp = Component("login.json","login-span")
cmp.load()


