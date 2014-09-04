__author__ = 'anupama'

import jinja2
import simplejson as json

class Component:
    def __init__(self,json_file, section):
        templateloader = jinja2.FileSystemLoader( searchpath="./" )
        templateenv = jinja2.Environment( loader=templateloader )
        template_file = json_file
        template = templateenv.get_template( template_file )
        self.page = json.loads( template.render(  ))
        self.span = self.page["elements"][section]
        print self.span

    def parse(self):
        pass

    def load(self):
        for element in self.span:
            
        pass

cmp = Component("login.json","login-span")

