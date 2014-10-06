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


from src.morpheus.test_template.web_component import WebComponent

__author__ = 'anupama'

class TweetBox(WebComponent):
    def __init__(self):
        super(TweetBox, self).__init__(self.__class__)

    def tweet(self, tweet_message):
        self.tweet_box.send_keys(tweet_message)
        self.component_loader.detect_element("tweet_button", make_visible=True)
        self.objectify("tweet_button", self.component_loader.props)
        self.tweet_button.click()



# login = Login ("pre_login_home.json", "login-span")
# login.login("netsgr8_4us@yahoo.com" , "thisispassword")
# new_tweet = NewTweet ("post_login_home.json", "new_tweet")
# new_tweet.tweet("auto tweet")
# # TODO 1  # make driver common for all classes in a test, # write all classes for one .json file in one py file

def new_tweet(test_input=None):
    TweetBox().tweet("I  am a Robot")
