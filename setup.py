#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


setup(name='testatron',
      version='0.0.0',
      packages=find_packages()
      )
