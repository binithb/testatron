__author__ = 'anupama'

import time
import jinja2
import simplejson as json
from Selenium2Library import Selenium2Library
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger

s2l_handle = None

def get_s2l():
    global s2l_handle
    if not s2l_handle:
        try:
            s2l_handle = BuiltIn().get_library_instance("Selenium2Library")
        except RuntimeError:
            s2l_handle = Selenium2Library()
    return s2l_handle


class S2L(object):
    def __init__(self):
        self.s2l = get_s2l()

    def got_to(self, url="http://google.com"):
        self.s2l.go_to(url)


class ComponentLoader(S2L):
    JSON_KEY_VISIBLE = "visible"
    JSON_KEY_PROPS = "props"
    JSON_KEY_LOC = "loc"
    JSON_KEY_ELEMENTS = "elements"
    JSON_KEY_TYPE = "list"
    def __init__(self, path, json_file, section):
        super(ComponentLoader, self).__init__()
        template_loader = jinja2.FileSystemLoader(searchpath=path)
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(json_file)
        self.page = json.loads(template.render())
        self.span = self.page[self.JSON_KEY_ELEMENTS][section]
        self.props = {}
        logger.debug(self.span)
        self.driver = self.s2l._current_browser()

    def load(self):
        for element in self.span:
            self.detect_element(element)

    def detect_element(self, element, make_visible=False):
            logger.debug(element)
            logger.debug(self.span[element])
            props = self.span[element][self.JSON_KEY_PROPS]
            logger.debug(props)
            if self.JSON_KEY_VISIBLE in props:
                    props[self.JSON_KEY_VISIBLE] = make_visible
                    if not props[self.JSON_KEY_VISIBLE]:
                        logger.debug("skipping invisible element")
                        return None

            if self.JSON_KEY_TYPE in props and props[self.JSON_KEY_TYPE]:
                self.s2l.wait_until_element_is_visible("xpath=" + self.span[element][self.JSON_KEY_PROPS][self.JSON_KEY_LOC], 30)
                self.props[element] = self.driver.find_elements_by_xpath\
                    (self.span[element][self.JSON_KEY_PROPS][self.JSON_KEY_LOC])
                if not self.props[element]:
                    raise AssertionError("failed to find elements with locator " + self.span[element][self.JSON_KEY_PROPS][self.JSON_KEY_LOC])
            else:
                logger.debug(self.span[element][self.JSON_KEY_PROPS][self.JSON_KEY_LOC])
                self.props[element] = self._get_locator_by_type(self.span[element][self.JSON_KEY_PROPS][self.JSON_KEY_LOC])
                return self.props[element]


    def _get_locator_by_type(self, locator):
        logger.debug("locator %s " % locator)
        locator_type, uniqueid = locator[0:1], locator[1:]
        logger.debug("locator_type %s, uniqueid %s" % (locator_type, uniqueid))
        logger.debug("waiting 30 s for element")
        if 1 == len(locator_type) and 0 < len(uniqueid):
            if '#' == locator_type and ' ' not in uniqueid:
                elem = self.driver.find_element_by_id(uniqueid)
            elif '#' == locator_type and ' ' in uniqueid:
                self.s2l.wait_until_element_is_visible("css=" + locator_type + uniqueid, 30)
                elem = self.driver.find_element_by_css_selector(locator_type+uniqueid)
            elif '.' == locator_type and ' ' not in uniqueid:
                elem = self.driver.find_element_by_class_name(uniqueid)
            elif '.' == locator_type and ' ' in uniqueid:
                self.s2l.wait_until_element_is_visible("css=" + locator_type + uniqueid, 30)
                elem = self.driver.find_element_by_css_selector(locator_type+uniqueid)
            elif '/' == locator_type:
                self.s2l.wait_until_element_is_visible("xpath=" + locator_type + uniqueid, 30)
                elem = self.driver.find_element_by_xpath(locator_type+uniqueid)
            elif ' ' in uniqueid:
                self.s2l.wait_until_element_is_visible("css=" + locator_type + uniqueid, 30)
                elem = self.driver.find_element_by_css_selector(locator_type+uniqueid)
            else:
                logger.debug("unsupported location finder method")
                elem = None

        if elem:
            highlight(elem)
            logger.debug(elem.__dict__)
        return elem


def highlight(element):
    parent_ = element._parent
    def apply_style(s):
        parent_.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(.3)
    apply_style(original_style)

