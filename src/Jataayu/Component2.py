__author__ = 'anupama'
__author__ = 'anupama'

from src.Jataayu.component_loader import ComponentLoader

class Component2:
    def __init__(self,json_file, section):
        self.component= ComponentLoader(json_file,section)

    def parse(self):
        pass

