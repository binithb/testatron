#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='testatron',
      version='0.0.1',
      packages=find_packages(),
      install_requires=['robotframework-selenium2library', 'jinja2', 'simplejson'],
      )
