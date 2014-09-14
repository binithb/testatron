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


from component_loader import ComponentLoader
import project_suite_globals as project_suite_globals

class WebComponent(object):
    def __init__(self, class_name, section):
        print "class_name : %s " % class_name
        web_component_json_file = str(class_name)[str(class_name).rfind('.')+1:-2] + ".json"
        print "web_component_json_file %s " % web_component_json_file
        print "cwd :%s " % os.getcwd()
        print "project_suite_globals.web_app :%s " % project_suite_globals.web_app
        web_component_json_path = os.path.join(os.getcwd(), "src", "web_apps", project_suite_globals.web_app, "components")

        self.component_loader = ComponentLoader(web_component_json_path, web_component_json_file, section)
        self.component_loader.load()
        print self.component_loader.props
        for key, element in self.component_loader.props.items():
            print ("key %s element %s" ) % (key, element)
            # self.__dict__[key] = element
            self.objectify(key, self.component_loader.props)
        print(self)
        print(self.__dict__)
        # print self.username
        # self.component_loader.driver.quit()

    def objectify(self, key, dict):
        self.__dict__[key] = dict [key]


# self.component_loader = WebComponent("Login.json", "login-span")


