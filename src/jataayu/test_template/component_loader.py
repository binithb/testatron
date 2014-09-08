__author__ = 'anupama'

import jinja2
import simplejson as json

import globals as globals


class ComponentLoader:
    JSON_KEY_VISIBLE = "visible"
    JSON_KEY_PROPS = "props"
    JSON_KEY_LOC = "loc"
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
            self.props[element] = self.detect_element(element)

    def detect_element(self, element):
            print element
            print self.span[element]
            props = self.span[element][self.JSON_KEY_PROPS]
            print props
            if self.JSON_KEY_VISIBLE in props and False == props[self.JSON_KEY_VISIBLE]:
                print "skipping invisible element"
            else:
                print self.span[element][self.JSON_KEY_PROPS][self.JSON_KEY_LOC]
                return self._get_locator_by_type(self.span[element][self.JSON_KEY_PROPS][self.JSON_KEY_LOC])


    def _get_locator_by_type(self, locator):

        print "locator %s " % locator
        css_type, uniqueid = locator[0:1], locator[1:]
        print "css_type %s, uniqueid %s" % (css_type, uniqueid)
        self.driver = globals.get_driver()
        if 1 == len(css_type) and 0 < len(uniqueid):
            if '#' == css_type:
                elem = self.driver.find_element_by_id(uniqueid)
            elif '.' == css_type and ' ' not in uniqueid:
                elem = self.driver.find_element_by_class_name(uniqueid)
            elif '.' == css_type and ' ' in uniqueid:
                elem = self.driver.find_element_by_css_selector(css_type+uniqueid)
            else:
                print "unsupported location finder method"
                elem = None

        if elem:
            print elem.__dict__
        return elem

# cmp = ComponentLoader("login.json", "login-span")
# cmp.load()
# print cmp.props


