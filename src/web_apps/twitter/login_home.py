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


from src.jataayu.test_template.web_component import WebComponent

class LoginHome(WebComponent):
    def __init__(self, json_file, section):
        super(LoginHome, self).__init__(json_file,section)

    def check_about(self, ):
        pass
        # print "self.username"
        # print self.username
        print "about"
        print self.about


login_home = LoginHome ("login.json", "footer")
login_home.check_about()

