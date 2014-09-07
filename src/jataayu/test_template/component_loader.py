__author__ = 'anupama'

import jinja2
import simplejson as json

import globals as globals


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
        globals.init()

    def load(self):
        for element in self.span:
            print element
            print self.span[element]
            print self.span[element]["props"]
            print self.span[element]["props"]["loc"]
            self.props[element] = self._get_locator_by_type(self.span[element]["props"]["loc"])

    def _get_locator_by_type(self,locator):

        print ("locator %s ") % locator
        css_type, uniqueid = locator[0:1], locator[1:]
        print ("css_type %s, uniqueid %s") % (css_type, uniqueid)
        self.driver = globals.get_driver()
        if (1 == len(css_type) and 0 < len(uniqueid)):
            if ('#' == css_type):
                elem = self.driver.find_element_by_id(uniqueid)
            elif ('.' == css_type):
                elem = self.driver.find_element_by_class_name(uniqueid)
            else:
                print "unsupported location finder method"

        print elem.__dict__
        return elem

# cmp = ComponentLoader("login.json", "login-span")
# cmp.load()
# print cmp.props


