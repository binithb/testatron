#!/usr/bin/env python
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


"""Module implementing the command line entry point for executing tests.

This module can be executed from the command line using the following
approaches::

    python -m morpheus.run
    python path/to/morpheus/run.py

"""

USAGE = """Jataayu

Version:  <VERSION>

Usage:  morpheus [options] data_sources


Options
=======

 -N --name name
Environment Variables
=====================

JATAAYU_OPTIONS           Space separated list of default options to be placed
                          in front of any explicit options on the command line.

Examples
========

# Simple test run with `morpheus` without options.
$ morpheus tests.html

"""

import sys

# if 'morpheus' not in sys.modules and __name__ == '__main__':
    import pythonpathsetter

# from morpheus.conf import RobotSettings
# from morpheus.output import LOGGER
from jataayu.utils import Application


class Jataayu(Application):

    def __init__(self):
        Application.__init__(self, USAGE, arg_limits=(1,),
                             env_options='JATAAYU_OPTIONS', logger=LOGGER)

    def main(self, datasources, **options):

        suite = TestSuiteBuilder(settings['SuiteNames'],
                                 settings['WarnOnSkipped'],
                                 settings['RunEmptySuite']).build(*datasources)
        # suite.configure(**settings.suite_config)
        result = suite.run(settings)
        LOGGER.info("Tests execution ended. Statistics:\n%s"
                    % result.suite.stat_message)

        return result.return_code

    def validate(self, options, arguments):
        return self._filter_options_without_value(options), arguments

    def _filter_options_without_value(self, options):
        return dict((name, value) for name, value in options.items() if value)


def run_cli(arguments):
    """Command line execution entry point for running tests.

    :param arguments: Command line arguments as a list of strings.

    For programmatic usage the :func:`run` function is typically better. It has
    a better API for that usage and does not call :func:`sys.exit` like this
    function.

    Example::

        from morpheus import run_cli

        run_cli(['--include', 'tag', 'path/to/tests.html'])
    """
    Jataayu().execute_cli(arguments)


def run(*datasources, **options):
    """Executes given Robot Framework data sources with given options.

    Data sources are paths to files and directories, similarly as when running
    `morpheus` command from the command line. Options are given as keyword
    arguments and their names are same as long command line options except
    without hyphens.

    Options that can be given on the command line multiple times can be
    passed as lists like `include=['tag1', 'tag2']`. If such option is used
    only once, it can be given also as a single string like `include='tag'`.

    To capture stdout and/or stderr streams, pass open file objects in as
    special keyword arguments `stdout` and `stderr`, respectively.

    A return code is returned similarly as when running on the command line.

    Example::

        from morpheus import run

        run('path/to/tests.html', include=['tag1', 'tag2'])
        with open('stdout.txt', 'w') as stdout:
            run('t1.txt', 't2.txt', report='r.html', log='NONE', stdout=stdout)

    Equivalent command line usage::

        morpheus --include tag1 --include tag2 path/to/tests.html
        morpheus --report r.html --log NONE t1.txt t2.txt > stdout.txt
    """
    return Jataayu().execute(*datasources, **options)


if __name__ == '__main__':
    run_cli(sys.argv[1:])

