__author__ = 'anupama'

import jinja2
import simplejson as json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ComponentLoader:
    def __init__(self,json_file, section):
        templateloader = jinja2.FileSystemLoader( searchpath="./" )
        template_env = jinja2.Environment( loader=templateloader )
        template_file = json_file
        template = template_env.get_template( template_file )
        self.page = json.loads( template.render(  ))
        self.span = self.page["elements"][section]
        self.props = {}

        print self.span

    def load(self):
        for element in self.span:
            print element
            print self.span[element]
            print self.span[element]["props"]
            print self.span[element]["props"]["loc"]
            self.props[element] = self._get_element(self.span[element]["props"]["loc"])
        pass
    def _get_element(self,loc):
        #driver = webdriver.PhantomJS()
        driver.get("http://www.twitter.com")
        elem = driver.find_element_by_id("signin-email")
        print elem.__dict__

    def _get_locator_by_type(self, locator):
        if ('.' == locator[0]):
            return
        elif('#' == locator[0])::





cmp = ComponentLoader("login.json","login-span")
cmp.load()


