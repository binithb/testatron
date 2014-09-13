__author__ = 'anupama'

import jinja2
import simplejson as json
import globals as globals


class ComponentLoader:
    JSON_KEY_VISIBLE = "visible"
    JSON_KEY_PROPS = "props"
    JSON_KEY_LOC = "loc"
    JSON_KEY_ELEMENTS = "elements"
    def __init__(self, json_file, section):
        template_loader = jinja2.FileSystemLoader(searchpath="./")
        template_env = jinja2.Environment(loader=template_loader)
        template_file = json_file
        template = template_env.get_template(template_file)
        self.page = json.loads(template.render())
        self.span = self.page[self.JSON_KEY_ELEMENTS][section]
        self.props = {}
        print self.span

    def load(self):
        for element in self.span:
            self.detect_element(element)

    def detect_element(self, element, make_visible=False):
            print element
            print self.span[element]
            props = self.span[element][self.JSON_KEY_PROPS]
            print props
            if self.JSON_KEY_VISIBLE in props :
                    props[self.JSON_KEY_VISIBLE] = make_visible
                    if not props[self.JSON_KEY_VISIBLE]:
                        print "skipping invisible element"
                        return None

            print self.span[element][self.JSON_KEY_PROPS][self.JSON_KEY_LOC]
            self.props[element] = self._get_locator_by_type(self.span[element][self.JSON_KEY_PROPS][self.JSON_KEY_LOC])
            return self.props[element]


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
            elif ' ' in uniqueid:
                elem = self.driver.find_element_by_css_selector(css_type+uniqueid)
            else:
                print "unsupported location finder method"
                elem = None

        if elem:
            print elem.__dict__
        return elem

# cmp = ComponentLoader("Login.json", "login-span")
# cmp.load()
# print cmp.props


