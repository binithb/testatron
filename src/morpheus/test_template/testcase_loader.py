__author__ = 'anupama'

import jinja2
import simplejson as json
import os



class TestCaseLoader:
    JSON_KEY_TESTCASES = "test_cases"
    def __init__(self, json_file, test_case, webapp_path):
        test_case_loader = jinja2.FileSystemLoader(searchpath=webapp_path)
        template_env = jinja2.Environment(loader=test_case_loader)
        template_file = json_file
        template = template_env.get_template(template_file)
        self.test_suite = json.loads(template.render())
        self.span = self.test_suite[self.JSON_KEY_TESTCASES][test_case]
        self.props = {}
        print self.span

    def get_test_case(self):
        for element in self.span:
            self.props[element] = self.span[element]
        return self.props




# print os.getcwd()
# cmp = TestCaseLoader("login_test.json", "login_basic", "../../web_apps/twitter/test_input/")
# cmp.load()
# print cmp.props
#

