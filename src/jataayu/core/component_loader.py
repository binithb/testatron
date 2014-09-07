__author__ = 'anupama'

import jinja2
import simplejson as json


class ComponentLoader:
    def __init__(self, json_file, section):
        templateloader = jinja2.FileSystemLoader(searchpath="./")
        template_env = jinja2.Environment(loader=templateloader)
        template_file = json_file
        template = template_env.get_template(template_file)
        self.page = json.loads(template.render())
        self.span = self.page["elements"][section]
        self.props = {}
        print self.span

    def load(self):
        for element in self.span:
            print element
            print self.span[element]
            print self.span[element]["props"]
            print self.span[element]["props"]["loc"]
            self.props[element] = self._get_locator_by_type(self.span[element]["props"]["loc"])

    def _get_locator_by_type(self,locator):

        css_type, uniqueid = locator[0,1], locator[1]
        if (1 == css_type.length && 0 < uniqueid.length):
            if ('.' == css_type):
                elem = driver.find_element_by_id("signin-email")
            elif ('#' == css_type):
                elem = driver.fin("signin-email")
            else:
                print "unsupported location menthod"

        print elem.__dict__

cmp = ComponentLoader("login.json", "login-span")
cmp.load()


